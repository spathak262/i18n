import os
import json

def getFolders():
    return os.listdir("./public/translations")

def checkForDuplicates(keys, allKeys):
    for key in keys:
        if key in allKeys:
            raise Exception("Error occured. key ' %s ' already exists" % (key) )

def merge(folder):
    result = {}
    allKeys = []
    for fileName in os.listdir("./public/translations/" + folder):
        with open("./public/translations/% s/% s"%(folder, fileName), "r") as inFile:
            jsonData = json.load(inFile)
            checkForDuplicates(jsonData.keys(), allKeys)
            allKeys.extend(jsonData.keys())
            result = dict(result.items() | jsonData.items())

    with open('public/locales/' + folder + '/translation.json', 'a') as output_file:
        json.dump(result, output_file)

folders = getFolders()

if os.path.exists("public/locales"):
    os.rmdir("public/locales")

os.mkdir("public/locales")

for folder in folders:
    if not os.path.exists("public/locales/" + folder):
        os.mkdir("public/locales/" + folder)
    merge(folder)