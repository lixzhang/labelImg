import sys
import os
import json
from xml.etree import ElementTree
from xml.etree.ElementTree import Element, SubElement
from lxml import etree
import codecs
from libs.constants import DEFAULT_ENCODING


JSON_EXT = '.json'
ENCODE_METHOD = DEFAULT_ENCODING

class JSONWriter:

    def __init__(self, foldername, filename, imgSize,databaseSrc='Unknown', localImgPath=None):
        self.foldername = foldername
        self.filename = filename
        self.databaseSrc = databaseSrc
        self.imgSize = imgSize
        self.boxlist = []
        self.localImgPath = localImgPath
        self.verified = False

    def addBndBox(self, xmin, ymin, xmax, ymax, name, difficult):
        bndbox = {'xmin': xmin, 'ymin': ymin, 'xmax': xmax, 'ymax': ymax}
        bndbox['name'] = name
        bndbox['difficult'] = difficult
        self.boxlist.append(bndbox)

    def save(self, targetFile=None):
        result = {}
        result["language"] = "unknown"
        result["regions"] = []

        for box in self.boxlist:
            xmin = box['xmin']
            xmax = box['xmax']
            ymin = box['ymin']
            ymax = box['ymax']
            boxName = box['name']

            vertices = [(xmin, ymin), (xmax, ymin), (xmax, ymax), (xmin, ymax)]
            text     = boxName
            data = {}
            data['vertices'] = vertices
            data['text'] = text
            result["regions"].append(data)
            
        out_file = None
        if targetFile is None:
            out_file = codecs.open(
                self.filename + JSON_EXT, 'w', encoding=ENCODE_METHOD)
        else:
            out_file = codecs.open(targetFile, 'w', encoding=ENCODE_METHOD)
        print("target file", targetFile)
        print("file", self.filename)
        print('outfile', out_file)
        json.dump(result, out_file) 
        out_file.close()


class JsonReader:

    def __init__(self, filepath):
        # shapes type:
        # [labbel, [(x1,y1), (x2,y2), (x3,y3), (x4,y4)], color, color, difficult]
        self.shapes = []
        self.filepath = filepath
        self.verified = False
        try:
            self.parseJsonFormat()
        except:
            pass

    def getShapes(self):
        return self.shapes

    def addShape(self, label, xmin, ymin, xmax, ymax, difficult):

        points = [(xmin, ymin), (xmax, ymin), (xmax, ymax), (xmin, ymax)]
        self.shapes.append((label, points, None, None, difficult))

    def parseJsonFormat(self):
        with open(self.filepath) as json_f:
            ocr_result = json.load(json_f)        

        for region in ocr_result["regions"]:
            xmin = min([x[0] for x in region['vertices']])
            ymin = min([x[1] for x in region['vertices']])
            xmax = max([x[0] for x in region['vertices']])
            ymax = max([x[1] for x in region['vertices']])
            label = region['text'] 
            # Caveat: difficult flag is discarded when saved as yolo format.
            self.addShape(label, xmin, ymin, xmax, ymax, False)