import json;

output_data = []

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
