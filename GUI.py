from Tkinter import *
from PIL import ImageTk
from Calculation import getHighestScore
from ImageHandler import *
import json
import urllib2

top = Tk()
top.title("LOLSpellEfficiency")
top.geometry("600x600")
top.configure(background = "blue")


# Code to add widgets will go here...
count = 0


def loadInputFields(frame):
    AP_Label = Label(frame, text="AP" , fg = "blue")
    AD_Label = Label(frame, text="AD", fg = "red")
    CDR_Label = Label(frame, text="CDR", fg = "green")

    AP_Label.grid(row=0, column=0)
    AD_Label.grid(row=1, column=0)
    CDR_Label.grid(row=2, column=0)

    AP_Entry = Entry(frame)

    AD_Entry = Entry(frame)

    CDR_Entry = Entry(frame)

    AP_Entry.grid(row=0, column=1)
    AP_Entry.insert(0, "0")
    AD_Entry.grid(row=1, column=1)
    AD_Entry.insert(0, "0")
    CDR_Entry.grid(row=2, column=1)
    CDR_Entry.insert(0, "0")

    return [AP_Entry, AD_Entry, CDR_Entry]


def loadButton(frame, entries, championFrame, spellFrame):
    Enter_Button = Button(frame, text="Calculate!", command = lambda: executeProgram(entries, championFrame, spellFrame))
    Enter_Button.pack(side=TOP)



def executeProgram(entries, championFrame, spellFrame):

    for widget in championFrame.winfo_children():
        widget.destroy()

    for widget in spellFrame.winfo_children():
        widget.destroy()

    AP = float(entries[0].get())
    AD = float(entries[1].get())
    CDR = float(entries[2].get())
    data = getChampionData()
    result = getHighestScore(data, AP, AD, CDR)

    champPhoto = ImageTk.PhotoImage(getChampionImage(result[0]))
    champLabel = Label(championFrame, image=champPhoto)
    champLabel.image = champPhoto
    champLabel.pack(side = TOP)

    champName = Label(championFrame, text = "Champion: " + result[0])
    champName.pack(side = BOTTOM)

    spellPhoto = ImageTk.PhotoImage(getSpellImage(result[2]))
    spellLabel = Label(spellFrame, image=spellPhoto)
    spellLabel.image = spellPhoto


    spellText = Text(spellFrame, wrap=WORD)
    spellText.insert(INSERT, "Spell: " + result[1] + "\n" + "\n")
    spellText.insert(INSERT, "Spell description: " + result[3] + "\n" + "\n")
    spellText.insert(INSERT, result[4])
    spellLabel.pack(side=TOP)
    spellText.pack(side=BOTTOM)




def getChampionData():
    URL = "https://global.api.pvp.net/api/lol/static-data/na/v1.2/champion?champData=all&api_key=8e8904b4-c112-4b0f-bd1e-641649d9e569"
    return json.load(urllib2.urlopen(URL))


inputFrame = Frame(top)
inputFrame.pack()

buttonFrame = Frame(top)
buttonFrame.pack()

championFrame = Frame(top)
spellFrame = Frame(top)
championFrame.pack()
spellFrame.pack()

entries = loadInputFields(inputFrame)
loadButton(buttonFrame, entries, championFrame, spellFrame)

top.mainloop()
