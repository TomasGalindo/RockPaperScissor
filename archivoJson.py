import os
import json
def lecturaJSON():
    print("Lectura JSON")
    fileObject = open("data.json","r")
    jsonContent = fileObject.read()
    aList = json.loads(jsonContent)
    print(type(aList))
    for element in aList:
        print(element)

    return aList

def escrituraJSON(info):
    print("EscrituraJSON")

    jsonString = json.dumps(info)
    jsonFile = open("data.json","w")
    jsonFile.write(jsonString)
    jsonFile.close()



"""
MIS PRUEBAS
"""


#if(os.path.exists('file.txt')):
"""
Aqui iría todo el proceso de cuando existe el archivo
"""
#else:
"""
tengo que crear el archivo
"""

"""
Aqui ya haría lo mismo """
aDict = [{"Nombre":"Juan","Victorias":0,"Derrotas": 0, "PartidasJugadas":0,"%Victorias":0},{"Nombre":"Paco","Victorias":0,"Derrotas": 0, "PartidasJugadas":0,"%Victorias":0}]
escrituraJSON(aDict)
myList = lecturaJSON()

print(type(myList))
for element in myList:
    print(element)

print("FIN")
#print(os.path.exists('file.txt'))
