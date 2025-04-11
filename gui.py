from tkinter import *
from data import OUTPUT_DATA as data

# GUI help from https://www.geeksforgeeks.org/create-first-gui-application-using-python-tkinter/

window = Tk()
window.title("Form To PDF")

# set window size to fullscreen
width= window.winfo_screenwidth()               
height= window.winfo_screenheight() 
window.geometry("%dx%d" % (width, height))

# all widgets shown in window go below vvv

inputs = []
# go through each item in the dataset and display properly
index = 0
# index seperate from for loop so i can make the checkboxes build right
for item in data:
    index = index + 1
    # if we're at a section header, display that accordingly
    if item['type'] == 'title':
        subtitle = Label(window, text=item['text'], font=('Arial', 20, 'bold'))
        subtitle.grid(column=0, row=index, sticky='WE', columnspan=3)
        continue
    
    # for each q/a spit out a label and an entry method
    lbl = Label(window, text=item['question'], justify='left', font=('Arial', 16))
    lbl.grid(column=0, row=index, sticky='W', padx=4)

    if item['type'] == "string" or item['type'] == 'number':
        # if string or number, show a text box to get the data
        input = Entry(window, width=20, justify='left', font=('Arial', 16))
        input.grid(column=1, row=index, sticky='WE', columnspan=3, padx=4)
        inputs.append(input)
    else:
        # if multiple choice show all choices in rows of 4 max
        checkbox_values = []
        for ind, option in enumerate(item['answers']):
            checkbox_value = BooleanVar(value=False)
            button = Checkbutton(window, text=option, justify='left', font=('Arial', 16), variable=checkbox_value)
            col = ind
            row = index
            if ind % 4 == 0 and ind != 0:
                index=index+1
            if ind >= 4:
                col = ind-4
                row=index
            button.grid(column=(1+col), row=row, sticky='W', padx=4)
            checkbox_values.append(checkbox_value)
        inputs.append(checkbox_values)

# function to remove the subtitles from the data object so you only have the questions
def dataNoTitles(datum):
    if datum['type'] != 'title':
        return True

# function that's called on submit button click
def clicked():
    outputs = []
    questions = list(filter(dataNoTitles, data))
    print(questions)
    for number, question in enumerate(questions):
        print(number, question)
        if question['type']!='multiple':
            outputs.append(question['question'] + " " + inputs[number].get())
        else:
            options = question['answers']
            options_chosen = []
            for ind, option in enumerate(options):
                if inputs[number][ind].get() == True:
                    options_chosen.append(option)
            outputs.append(question['question'] + " " + str(options_chosen))

    # for now display the form data until we build PDF making
    output = Message(window, font=('Arial', 16), text=outputs, width=1000)
    output.grid(column=0, row=12, columnspan=5,sticky='W', padx=4)

# submit label and button and output
end_lbl = Label(window, text="Click the button below when you're ready to generate your PDF", font=('Arial', 16), padx=4)
btn = Button(window, text = "Create PDF" , font=('Arial', 16),fg = "black", command=clicked)
end_lbl.grid(column=0, row=10, sticky='W', padx=4, columnspan=4)
btn.grid(column=1, row=11, sticky='W')

# display the actual window
window.mainloop()