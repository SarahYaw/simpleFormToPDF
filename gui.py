from tkinter import *
from tkinter import filedialog
from pdf_maker import makePDF
import data

# GUI help from https://www.geeksforgeeks.org/create-first-gui-application-using-python-tkinter/

window = Tk()
window.title("Form To PDF")

# set window size to fullscreen
width= window.winfo_screenwidth()               
height= window.winfo_screenheight() 
window.geometry("%dx%d" % (width, height))

# frame that all the widgets go on
frame = Frame(window)
frame.grid(column=0, row=0)

def import_file():
    global loading_label
    file = filedialog.askopenfilename(filetypes=[("CSV files", ".csv")])
    loading_label.grid(column=1, row=3, sticky='WE', columnspan=3)
    digested = data.digest_data(file)
    if (digested == None):
        loading_label = Label(frame, text='No file chosen, please try again.', font=('Arial', 14, 'bold'))
        loading_label.grid(column=1, row=3, sticky='WE', columnspan=3)
    else: 
        loading_label = Label(frame, text="Loading...", font=('Arial', 14, 'bold'))
        loading_label.grid(column=1, row=3, sticky='WE', columnspan=3)

import_label = Label(frame, text="Please upload your csv", font=('Arial', 20, 'bold'))
import_label.grid(column=1, row=0, sticky='WE', columnspan=3)
loading_label = Label(frame, text="Loading...", font=('Arial', 14, 'bold'))
import_button = Button(frame, text="Import File", command=import_file)
import_button.grid(column=1, row=2, sticky='WE', columnspan=3)

# while loop until we get input csv
while (len(data.output_data)==0):
    window.after(500)
    window.update()

# kill import screen widgets
for item in frame.winfo_children():
    item.destroy()

# re-initialize the data so it's not empty
formSet = data.output_data

inputs = []
# go through each item in the dataset and display properly
index = 0
# index seperate from for loop so i can make the checkboxes build right
for item in formSet:
    index = index + 1
    # if we're at a section header, display that accordingly
    if item['type'] == 'title':
        subtitle = Label(frame, text=item['text'], font=('Arial', 20, 'bold'))
        subtitle.grid(column=0, row=index, sticky='WE', columnspan=3)
        continue
    
    # for each q/a spit out a label and an entry method
    lbl = Label(frame, text=item['question'], justify='left', font=('Arial', 16))
    lbl.grid(column=0, row=index, sticky='W', padx=4)

    if item['type'] == "string" or item['type'] == 'number':
        # if string or number, show a text box to get the data
        input = Entry(frame, width=20, justify='left', font=('Arial', 16))
        input.grid(column=1, row=index, sticky='WE', columnspan=3, padx=4)
        inputs.append(input)
    else:
        # if multiple choice show all choices in rows of 4 max
        checkbox_values = []
        for ind, option in enumerate(item['answers']):
            checkbox_value = BooleanVar(value=False)
            button = Checkbutton(frame, text=option, justify='left', font=('Arial', 16), variable=checkbox_value)
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

# function to remove the subtitles from the formSet object so you only have the questions
def dataNoTitles(datum):
    if datum['type'] != 'title':
        return True

# function that's called on submit button click
def clicked():
    outputs = []
    questions = list(filter(dataNoTitles, formSet))
    for number, question in enumerate(questions):
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
    output = Message(frame, font=('Arial', 16), text="Generating...", width=1000)
    output.grid(column=0, row=12, columnspan=5,sticky='W', padx=4)
    makePDF(outputs)
    # kill form screen widgets
    for item in frame.winfo_children():
        item.destroy()
    finished = Message(frame, font=('Arial', 16), text="File created!", width=1000)
    finished.grid(column=0, row=0, columnspan=5,sticky='W', padx=4)

# submit label and button and output
end_lbl = Label(frame, text="Click the button below when you're ready to generate your PDF", font=('Arial', 16), padx=4)
btn = Button(frame, text = "Create PDF" , font=('Arial', 16),fg = "black", command=clicked)
end_lbl.grid(column=0, row=10, sticky='W', padx=4, columnspan=4)
btn.grid(column=1, row=11, sticky='W')

# display the actual window
window.mainloop()