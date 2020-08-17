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
        delRecord = input("Please mention the TV/Movie name : ")
        lists = [x for x in self.showsList if x["name"] == delRecord]
        if(len(lists) > 0):
            print(str(len(lists)) +" Records Found")
            for i in lists:
                self.showsList.remove(i)
            print("Records Deleted")
        else:
            print("No Records Found")

        
    def updateRecord(self):
        updateRecord = input("Please mention the TV/Movie name : ")
        lists = [x for x in self.showsList if x["name"] == updateRecord]
        if(len(lists) == 0):
            print("No records found")
        else:
            replaceRecord = input("Mention the replaced name for selected one : ")
            for k in self.showsList:
                if(k["name"] == updateRecord):
                    k["name"] = replaceRecord
        
    def dump(self):
        if os.path.isfile("files.json"):
            with open("files.json", "w") as openFile:
                json.dump(self.showsList, openFile, indent=4)
                openFile.close()
        else:
            print("File not found, creating new one")
            with open("files.json", "w") as openFile:
                json.dump(self.showsList, openFile, indent=4)
                openFile.close()