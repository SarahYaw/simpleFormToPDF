import data

# initialize crap
saveFile = None

# see if save file exists
def checkForSaveFile():
    global saveFile
    try:
        saveFile = open('save_data.txt')
        return True
    except: 
        print('NO FILE')
        return False

isSaveState = checkForSaveFile()

# save info in save file to form
# might be able to just do this in checkForSaveFile but get this working first
def initializeSaveState():
    global saveFile
    with open('save_data.txt', 'r') as file:
        saveData = ''
        for line in file:
            datum = line.rstrip().split('? ')
            if len(datum) > 1:
                saveData += '{"question":"'+datum[0]+'", "response":"'+datum[1]+'"}\n'
            else:
                saveData += datum[0]+'\n'
        data.regurgitate_data(saveData)

def createSaveState(results, filename):
    with open('save_data.txt', 'w') as file:
        file.write(filename + '\n\n')
        for line in results:
            file.write(line +'\n')
