import os
import json
NAME_FILE = "data2.json"
def lecturaJSON():
    print("Lectura JSON")
    fileObject = open(NAME_FILE,"r")
    jsonContent = fileObject.read()
    aList = json.loads(jsonContent)

    return aList

def escrituraJSON(info):
    print("EscrituraJSON")

    jsonString = json.dumps(info)
    jsonFile = open(NAME_FILE,"w")
    jsonFile.write(jsonString)
    jsonFile.close()
