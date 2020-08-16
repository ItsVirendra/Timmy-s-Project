import os.path
import json

class CRUD_operations:
    def __init__(self):
        self.showsList = []
        self.lists = []
        if os.path.isfile("files.json"):
            with open("files.json","r") as files:
                self.showsList = json.load(files)
                files.close()
        else:
            print("Hello User, there's no data. Creating new file")
            with open("files.json",'w') as files:
                files.close()
    
    def createNewShow(self):
        showName = input("Enter the name of show : ")
        showType = int(input("Mention the type of show (1: Movie / 2: TV): "))
        entryName = dict()
        entryName["name"] = showName
        entryName["types"] = showType
        self.showsList.append(entryName)
        
    def getRecords(self):
        print("\n \n ------ List ------ \n")
        print ("{:<10} {:<10}".format("Name", "Type"))
        for k in self.showsList:
            print ("{:<10} {:<10}".format(k["name"] , "Movie" if k["types"] == 1 else "TV"))
    
    def deleteRecord(self):
        print("delete a record")
        
    def updateRecord(self):
        print("update a record")
        
    def dump(self):
        if os.path.isfile("files.json"):
            with open("files.json", "w") as openFile:
                json.dump(self.showsList, openFile, indent=4)
            print("File exists")
        else:
            print("File not found, creating new one")
            with open("files.json", "w") as openFile:
                json.dump(self.showsList, openFile, indent=4)
                openFile.close()