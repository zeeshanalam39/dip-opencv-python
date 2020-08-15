x = ['apple', 'banana', 'mango', 'orange', 'peach', 'grapes']
def createNewList(l):
    newList = []
    i = 1
    while i < 6:
        newList.append(l[i])
        i = i + 1
        if i % 2 == 1:
            i = i + 1
    print(newList)

createNewList(x)

