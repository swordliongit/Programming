
import PySimpleGUI as sg
from main import operator_main
# import threading
from multiprocessing import Process
import concurrent.futures

from queue import Queue

from tkthread import threading


# fetch_warning = sg.PopupNoTitlebar('Devam etmek icin modemleri kurgulayin, kurgulama bittiyse OK\'a basin.', button_type=sg.POPUP_BUTTONS_OK, grab_anywhere=True)
# if fetch_warning == "OK":
#     # check if user wants to continue
#     continue_execution = sg.popup_yes_no('Degistirilen ayarlari uygulamak icin devam etmek istiyor musunuz?', no_titlebar=True, grab_anywhere=True)
#     if continue_execution == 'No':
#         exit()


#def fetch_confirmation(event):


def button_function(output, x_hotel_name, target_ip): 
    
    thread = threading.Thread(target=operator_main, args=(output, x_hotel_name, target_ip))
    thread.start()
    window.refresh()
    

layout = [
    [sg.Text("Otel adı girin"), sg.Button("Başlat", key="button", button_color=('white', 'green'), size=(6, 2))],
    [sg.InputText()],
    [sg.Text("ip menzilini girin")],
    [sg.InputText()],
    [sg.Multiline(size=(160, 80), key="output")]
]

window = sg.Window("Modem Configuration Program", layout, size=(300, 200))

window.finalize()

button = window.Element("button")
button.set_tooltip("Click this button to start configuring modems")
output = window.Element("output") #sg.Multiline

while True:
    event, values = window.read()
    if event == "button":
        button_function(output, values[0], values[1])
    elif event == sg.WIN_CLOSED:
        break
    


window.close()


















"""
def maincaller(output):

    main(output) # XXX MAIN CALL -->> PROGRAM STARTS HERE !!!
    window.refresh()    

def button_function(output):  #Call main function while still being able to log into screen
    
    thread = threading.Thread(target=maincaller, args=(output,))
    thread.start()
    
    print("Button clicked!")

layout = [
    [sg.Button("Start", key="button", button_color=('white', 'green'), size=(10, 2)), sg.Text("<-- Start auto config")],
    [sg.Multiline(size=(160, 80), key="output")]
]

window = sg.Window("Modem Configuration Program", layout, size=(700, 600))

window.finalize()

button = window.Element("button")
button.set_tooltip("Click this button to start configuring modems")
output = window.Element("output") #sg.Multiline

while True:
    event, values = window.read()
    if event == "button":
        button_function(output)
    elif event == sg.WIN_CLOSED:
        break

window.close()
"""


