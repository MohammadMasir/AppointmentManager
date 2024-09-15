'''
# TODO My Method....
class ListItem():
    def __init__(self, itemName):
        self.itemName = itemName
        self.nextItem = None

    def listItems(self, listLength, callCounter=None):
        if listLength == 0:
            print(f"{1}.",self.itemName)
        else:
            listLength -= callCounter
            print(f"{listLength + 1}.",self.itemName)

class TodoList():
    def __init__(self):
        self.listTop = None
        self.list_len = 0

    def listEmpty(self):
        return self.listTop is None

    def addItem(self, listItem):
        self.list_len += 1
        if self.listEmpty():
            self.listTop = listItem
        else:
            listItem.nextItem = self.listTop
            self.listTop = listItem

    def showList(self):
        if self.listEmpty():
            print("List is empty..")
        else:
            pointer = self.listTop
            call_counter = 0
            while pointer.nextItem != None:
                call_counter += 1
                pointer.listItems(self.list_len, call_counter)
                pointer = pointer.nextItem
            if pointer.nextItem == None:
                pointer.listItems(listLength = 0)

toDolist = TodoList()
tasks = ["Pray", "Excercise", "Study", "News", "Drink 2 Litre water daily."]

for task in tasks:
    list_item = ListItem(task)
    toDolist.addItem(list_item)

toDolist.showList()
'''

# ==-=--==-===----==--==-=-======-=-=-=-=-=-=======-----------======-=-===-=----- #

'''
# TODO Another method... (Showing the List Top to bottom, Like MyMethod but with more efficient DataStructures used.);
class ListItem():
    def __init__(self, itemName):
        self.itemName = itemName
        self.nextItem = None

    def listItems(self, itemNumber):
        print(f"{itemNumber}. {self.itemName}")

class TodoList():
    def __init__(self):
        self.listTop = None
        self.list_len = 0

    def listEmpty(self):
        return self.listTop is None

    def addItem(self, listItem):
        self.list_len += 1
        if self.listEmpty():
            self.listTop = listItem
        else:
            listItem.nextItem = self.listTop
            self.listTop = listItem

    def showList(self):
        if self.listEmpty():
            print("List is empty..")
        else:
            pointer = self.listTop
            for i in range(self.list_len, 0, -1):
                pointer.listItems(i)
                pointer = pointer.nextItem

toDolist = TodoList()
tasks = ["Pray", "Exercise", "Study", "News", "Drink 2 Litre water daily."]

for task in tasks:
    list_item = ListItem(task)
    toDolist.addItem(list_item)

toDolist.showList()
'''

# ==-=--==-===----==--==-=-======-=-=-=-=-=-=======-----------======-=-===-=----- #

'''
# TODO Method-II.. (Showing List bottom to Top);
class ListItem():
    def __init__(self, itemName):
        self.itemName = itemName
        self.nextItem = None

    def listItems(self, itemNumber):
        print(f"{itemNumber}. {self.itemName}")

class TodoList():
    def __init__(self):
        self.listTop = None
        self.list_len = 0

    def listEmpty(self):
        return self.listTop is None

    def addItem(self, listItem):
        self.list_len += 1
        if self.listEmpty():
            self.listTop = listItem
        else:
            listItem.nextItem = self.listTop
            self.listTop = listItem

    def showList(self):
        if self.listEmpty():
            print("List is empty..")
        else:
            pointer = self.listTop
            for i in range(1, self.list_len + 1):
                pointer.listItems(i)
                pointer = pointer.nextItem

toDolist = TodoList()
tasks = ["Pray", "Exercise", "Study", "News", "Drink 2 Litre water daily."]

for task in tasks:
    list_item = ListItem(task)
    toDolist.addItem(list_item)

toDolist.showList()
'''