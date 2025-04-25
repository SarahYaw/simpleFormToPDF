# Simple Form To PDF  (*^‿^*)
*Base task:* import a csv of questions and options into this program, answer the questions, export a pdf of the filled out form
## Libraries ʕ•ᴥ•ʔ
- os
- datetime
- reportlab
- tkinter
- json
## Other Details (ㆁᴗㆁ✿)
I've included a base csv set called `dummy_data.csv` that I've been using to test. The `2025-04-12.pdf` is the output of the dummy csv questions when I filled it out. The `save_data.txt` is where the program memory is so don't delete it once you run the program or you have to start over.

In the csv, multiple choice answer sets have to be formatted like so:
```
type,multiple,question,question_text_here,answers,[,option_one,option_two,option_three,]
```
I could not figure out a way to parse the option set without including the brackets that wasn't adding a whole other `elif word == 'answer` case that would get ugly pretty fast.

I've built this as a base for a project I'm building for a relative who has to fill out the same form every other week who's just editing PDFs all the time, hopefully this makes things easier. I'm going to make a private fork off of this so I can specify it to their situation but I figured someone else out there might think this is convenient. Feel free to snag a copy and edit it however. Any part that I looked up a lot for I put the link in the code right near it
