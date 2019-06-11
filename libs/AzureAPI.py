from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys
import time 

import libs.dialog_ui as dialog_ui
import os
import requests
import time
# If you are using a Jupyter notebook, uncomment the following line.
#%matplotlib inline
from io import BytesIO
import json 
import logging 
import shutil 


# logging.basicConfig()
logger = logging.getLogger(__name__)


__appname__ = 'labelImg'

class AzureAPI(QDialog, dialog_ui.Ui_Dialog):
    def __init__(self, subkey=None):
        QDialog.__init__(self)
        self.setupUi(self)
        
        self.browseButton.clicked.connect(self.browse_file)
        self.scoreButton.clicked.connect(self.scoreImages)
        self.closeButton.clicked.connect(self.close)
        if subkey: 
            self.subscriptionkey.setText(subkey)

    def browse_file(self):
        image_folder = QFileDialog.getExistingDirectory(self,
                                                     '%s - Open Directory' % __appname__, ".",
                                                     QFileDialog.ShowDirsOnly | QFileDialog.DontResolveSymlinks)
        self.imagefolder.setText(QDir.toNativeSeparators(image_folder))
        
    def scoreImages(self):
        subscription_key = self.subscriptionkey.text()
        assert subscription_key
        imagefolder = self.imagefolder.text()
        vision_base_url = "https://southcentralus.api.cognitive.microsoft.com/vision/v2.0/"
        text_recognition_url = vision_base_url + "read/core/asyncBatchAnalyze"
        headers  = {'Ocp-Apim-Subscription-Key': subscription_key, "Content-Type": "application/octet-stream",}
        params   = {'mode' : 'Printed'} # Printed, Handwritten
        logger.info("mode: {}".format(params["mode"]))

        def recognize_text(image_path):
            image_data = open(image_path, "rb").read()
            response = requests.post(text_recognition_url, headers=headers, params=params, data=image_data)

            # The recognized text isn't immediately available, so poll to wait for completion.
            analysis = {}
            poll = True
            while (poll):
                response_final = requests.get(
                    response.headers["Operation-Location"], headers=headers)
                analysis = response_final.json()
                # print(analysis)
                time.sleep(1)
                if ("recognitionResults" in analysis):
                    poll= False 
                if ("status" in analysis and analysis['status'] == 'Failed'):
                    poll= False
                    
            polygons=[]
            if ("recognitionResults" in analysis):
                # Extract the recognized text, with bounding boxes.
                polygons = [(line["boundingBox"], line["text"])
                    for line in analysis["recognitionResults"][0]["lines"]]

            return polygons

        def save_results(image_path, polygons, dest_txt):
            result = {}
            result["language"] = "unknown"
            result["regions"] = []

            with open(dest_txt, 'w') as outfile:
                json.dump(result, outfile) 

            for polygon in polygons:
                vertices = [(polygon[0][i], polygon[0][i+1]) for i in range(0,len(polygon[0]),2)]
                text     = polygon[1]
                data = {}
                data['vertices'] = vertices
                data['text'] = text
                result["regions"].append(data)

            with open(dest_txt, 'w') as outfile:
                json.dump(result, outfile) 

            return

        def process_images(src_dir, dest_dir, service="readapi"):

            if not os.path.exists(dest_dir):
                os.makedirs(dest_dir)

            n_images = 0
            for fname in os.listdir(src_dir):
                ext = fname.split('.')[1]
                if ext == "jpg":
                    n_images += 1
            
            ind_image = 0
            for fname in os.listdir(src_dir):
                logger.info("processing image {}".format(fname))
                f, ext = fname.split('.')
                if ext == "jpg":
                    image_path = os.path.join(src_dir, fname)  
                    polygons = recognize_text(image_path)
                    dest_txt = os.path.join(dest_dir, f+".json")
                    save_results(image_path, polygons, dest_txt)
                    ind_image += 1
                    print("value of ind", ind_image)
                    self.report(ind_image, n_images) 
 
        process_images(imagefolder, imagefolder)
        logger.info("done")                

    def report(self, ind_image, n_images):
        if n_images > 0:
            percent = ind_image * 100 / n_images 
            self.progress.setValue(int(percent))
            
if __name__ == "__main__":
    app = QApplication(sys.argv)
    dialog = AzureAPI()
    dialog.show()
    app.exec_()
