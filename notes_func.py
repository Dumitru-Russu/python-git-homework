from os import system
from datetime import datetime
notes = [
    {
        "text": "table 1, 2 soups",
        "when": "19:10",
    },
    {
        "text": "bill to table 2",
        "when": "19:20",
    },
    {
        "text": "call mom",
        "when": None
    }
]


def clear():
    system("cls")





def showNotes(pnotes):
    now = datetime.now()
    h, m = now.hour, now.minute
    for note in pnotes:
        warning = ""
        if note["when"] != None:
            fragments = note["when"].split(":")
            nh, nm= int(fragments[0]), int(fragments[1])
            if (h== nh and nm-m < 5) or (h==nh-1 and nm-m+60 < 5):
                warning = "( 5 or less min left !!! )"

        print(f"{note['text']} {warning}")










def addNote(pnotes):
    text = input("enter text: ")
    time= input("At what time do you want it? ")

    pos_yn = input("Do you want it on a specific position?(yes/no) ")
    if pos_yn =="yes":
        pos_number= int(input("Which one? "))
        pnotes.insert(pos_number-1, {"text":text, "when":time})
    else:
        pnotes.append( {"text":text, "when":time} )

def deleteNote(pnotes):
    idx = int(input("Which one deleted? ")) - 1
    pnotes.pop(idx)

clear()

addNote(notes)
deleteNote(notes)
showNotes(notes)