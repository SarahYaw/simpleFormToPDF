# initialize crap
saveFile = None

# save info in save file to form
def initializeSaveState():
    print('initialize save state')

# see if save file exists
def checkForSaveFile():
    global saveFile
    try:
        saveFile = open('save_data.txt')
        print('FILE REAL')
        return True
    except: 
        print('NO FILE')
        return False

isSaveState = checkForSaveFile()

def createSaveState(results, filename):
    with open('save_data.txt', 'w') as file:
        file.write(filename + '\n\n')
        for line in results:
            file.write(line +'\n')
