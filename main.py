from phase1_function import CRUD_operations

selOpt = 0
showsLists = CRUD_operations()



def options():
    message = """Hello User, enter the number for the action
    1. Add new record
    2. Edit record
    3. Delete record
    4. Show all records
    5. Exit"""
    print(message)
    try:
        selOpt = int(input("Select Option: "))
    except:
        print("Input must be a number")
    if(selOpt == 1):
        showsLists.createNewShow()
        showsLists.dump()
    elif(selOpt == 2):
        print("edit")
        showsLists.dump()
    elif(selOpt == 3):
        print("Delete")
        showsLists.dump()
    elif(selOpt == 4):
        showsLists.getRecords()
    elif(selOpt == 5):
        exit()
    else:
        print("Incorrect option")
    print("\n")
    options()


if __name__ == "__main__":
    options()