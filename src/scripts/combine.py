import os
import json

def getFolders():
    return os.listdir("./src/resources")

def checkForDuplicates(keys, allKeys):
    for key in keys:
        if key in allKeys:
            raise Exception("Error occured. key ' %s ' already exists" % (key) )

def merge(folder):
    result = {}
    allKeys = []
    for fileName in os.listdir("./src/resources/" + folder):
        with open("./src/resources.% s/% s"%(folder, fileName), r) as inFile:
            jsonData = json.load(inFile)
            checkForDuplicates(jsonData.keys(), allKeys)
            allKeys.append(jsonData.keys())
            result = dict(result.items() + jsonData.items())

    with open('build/locales/' + folder + '/translation.json', 'a') as output_file:
        json.dump(result, output_file)

folders = getFolders()

if not os.path.exists("build"):
    os.mkdir("build")

if not os.path.exists("build/locales"):
    os.mkdir("build/locales")

for folder in folders:
    if not os.path.exists("build/locales/" + folder):
        os.mkdir("build/locales/" + folder)
    merge(folder)