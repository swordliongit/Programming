import tkinter as tk
import time

from tkinter import messagebox

fetch_warning = messagebox.askokcancel("Devam etmek icin modemleri kurgulayin, kurgulama bittiyse OK'a basin.")
if fetch_warning:
    continue_execution = messagebox.askyesno("Degistirilen ayarlari uygulamak icin devam etmek istiyor musunuz?")
    if not continue_execution:
        exit()
        
messagebox.askokcancel()


requests
selenium
scapy