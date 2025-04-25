import json;

output_data = []
filename = ''

def digest_data(file):
    global output_data
    if file: # user selected file 
        fob=open(file,'r')
        raw = fob.read().split('\n')
        output_data="["
        for line in raw:
            output_data += '{'
            for word in line.split(','):
                if word == 'question' or word == 'type' or word == 'text' or word == 'answers':
                    output_data += '"'+word+'":'
                elif word == '[' or word == ']':
                    output_data += word
                else:
                    output_data += '"'+word+'",'
            output_data+='},'
        output_data+=']'
        output_data = output_data.replace(',}','}').replace(',]',']')
        output_data = json.loads(output_data)
        return output_data
    else: # user cancel the file browser window
        return None

def regurgitate_data(saveFile):
    global output_data, filename
    
    # put data from txt in output_data and have the user responses in 'response'
    filename = saveFile.split('\n')[0]
    # read info from csv saved in data
    fob=open(filename,'r')
    raw = fob.read().split('\n')
    output_data="["
    for line in raw:
        output_data += '{'
        for word in line.split(','):
            if word == 'question' or word == 'type' or word == 'text' or word == 'answers':
                output_data += '"'+word+'":'
            elif word == '[' or word == ']':
                output_data += word
            else:
                output_data += '"'+word+'",'
        output_data+='},'
    output_data+=']'
    output_data = output_data.replace(',}','}').replace(',]',']')
    output_data = json.loads(output_data)

    # get saved data
    dataset = saveFile.split('\n')[2:-1]
    index = 0
    for line in output_data:
        if line['type'] != 'title':
            line['response'] = json.loads(dataset[index])['response']
            index = index + 1