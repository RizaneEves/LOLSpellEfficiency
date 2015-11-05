from Tkinter import *
from PIL import ImageTk
from Calculation import getHighestScore
from ImageHandler import *
import json
import urllib2

"""
Uses Tkinter library to create a simple GUI for our program. Also is the main file that is compiled
to run this program.
"""


top = Tk()                                                  # Initialize window
top.title("LOLSpellEfficiency")                             # Give the window the title "LOLSpellEfficiency"
top.geometry("600x600")                                     # Sets the window's dimensions to 600x600






"""
Loads the AP, AD, and CDR input fields into a GUI frame and allows the program to collect data from the user.
"""
def loadInputFields(frame):
    AP_Label = Label(frame, text="AP" , fg = "blue")            # Set the AP label to blue
    AD_Label = Label(frame, text="AD", fg = "red")              # Set the AD label to red
    CDR_Label = Label(frame, text="CDR (enter a number between 0 and 0.4)", fg = "green")          # Set the CDR label to green

    AP_Label.grid(row=0, column=0)                              # Place AP label on the top left of the frame
    AD_Label.grid(row=1, column=0)                              # Place AD label below the AP label
    CDR_Label.grid(row=2, column=0)                             # Place CDR label below the AD label

    AP_Entry = Entry(frame)                                     # Initialize the AP entry field
    AD_Entry = Entry(frame)                                     # Initialize the AD entry field
    CDR_Entry = Entry(frame)                                    # Initialize the CDR entry field

    AP_Entry.grid(row=0, column=1)                              # Place the AP entry field next to AP label
    AP_Entry.insert(0, "0")                                     # Initialize this field to 0
    AD_Entry.grid(row=1, column=1)                              # Place the AD entry field next to AD label
    AD_Entry.insert(0, "0")                                     # Initialize this field to 0
    CDR_Entry.grid(row=2, column=1)                             # Place the CDR entry field next to the CDR label
    CDR_Entry.insert(0, "0")                                    # Initialize this field to 0

    return [AP_Entry, AD_Entry, CDR_Entry]                      # Return these entries to be used by our program

"""
Loads the Calculate button which launches the program into the frame.
Takes 2 frames as an input, on which the resulting champion and spell images and descriptions will be outputted.
"""
def loadButton(frame, entries, championFrame, spellFrame):
    """
    The line below initializes our button, names it "Calculate!" and stores the command to execute the program.
    The lambda keyword prevents the program to start executing as soon as we open and rather start
    when we click the button.
    """
    Enter_Button = Button(frame, text="Calculate!", command = lambda: executeProgram(entries, championFrame, spellFrame))
    Enter_Button.pack(side=TOP)             # Place the button on the top of this frame


"""
Executes our main program based on user entries and loads the results from the Riot API.
"""
def executeProgram(entries, championFrame, spellFrame):


    for widget in championFrame.winfo_children():       # Destroy everything that previously existed in this frame
        widget.destroy()                                # This allows us to use our program repeatedly.

    for widget in spellFrame.winfo_children():          # Destroy everything that previously existed in this frame
        widget.destroy()                                # This also allows us to replace old results with new results.

    AP = float(entries[0].get())                        # Get the AP entered by the user.
    AD = float(entries[1].get())                        # Get the AD entered by the user.
    CDR = float(entries[2].get())                       # Get the CDR entered by the user.
    data = getChampionData()                            # Get Riot API champion data.
    result = getHighestScore(data, AP, AD, CDR)         # Use champion data and inputs to calculate the most efficient spell.

    champPhoto = ImageTk.PhotoImage(getChampionImage(result[0]))    # Get the resulting champion's image
    champLabel = Label(championFrame, image=champPhoto)             # Store this image on a frame.
    champLabel.image = champPhoto
    champLabel.pack(side = TOP)                                     # Place this image on the top of the frame

    champName = Label(championFrame, text = "Champion: " + result[0])       # Get the resulting champion's name
    champName.pack(side = BOTTOM)                                           # Show this name below our champion image.

    spellPhoto = ImageTk.PhotoImage(getSpellImage(result[2]))               # Get the resulting spell's image
    spellLabel = Label(spellFrame, image=spellPhoto)
    spellLabel.image = spellPhoto


    spellText = Text(spellFrame, wrap=WORD)                                        # Initialize our output message
    spellText.insert(INSERT, "Spell: " + result[1] + "\n" + "\n")                  # Start our output message with spell name
    spellText.insert(INSERT, "Spell description: " + result[3] + "\n" + "\n")      # Insert spell description
    spellText.insert(INSERT, result[4])                                            # Insert reason
    spellLabel.pack(side=TOP)                                                      # Place spell image at the top of the spell frame
    spellText.pack(side=BOTTOM)                                                    # Place the output message below the spell image.



"""
Parse Riot API champion data and returns a dictionary based on this data.
"""
def getChampionData():
    URL = "https://global.api.pvp.net/api/lol/static-data/na/v1.2/champion?champData=all&api_key=8e8904b4-c112-4b0f-bd1e-641649d9e569"
    return json.load(urllib2.urlopen(URL))

# Initialize and place outer GUI frames.

inputFrame = Frame(top)         # Initialize the input frame which contains entry fields and their labels
inputFrame.pack()               # Place this frame at the top of the window

buttonFrame = Frame(top)        # Initialize the frame which contains the button
buttonFrame.pack()              # Place this below the input frame

championFrame = Frame(top)      # Initialize the frame which contains our resulting champion's image and name
spellFrame = Frame(top)         # Place this below the button.
championFrame.pack()            # Initialize the frame which contains the spell image and output message
spellFrame.pack()               # Place this below the champion frame.

entries = loadInputFields(inputFrame)                               # Load input fields into input frame and store user entries
loadButton(buttonFrame, entries, championFrame, spellFrame)         # Load the button with the command to execute the program

top.mainloop()                                                      # Constantly keep this GUI open until we close the program
