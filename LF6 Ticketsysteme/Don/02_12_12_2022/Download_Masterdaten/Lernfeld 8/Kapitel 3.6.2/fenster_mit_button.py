import tkinter
from tkinter import ttk

def btnClose_click():
    frmMain.destroy()
#------------------------------------------
# Erzeugen des Hauptfensters
#------------------------------------------
frmMain = tkinter.Tk()
frmMain.title("Ein Fenster mit Button")
frmMain.wm_geometry('400x200')
#-------------------------------------------------------------------
# Erzeugen und initialisieren des Button "btnClose"
#-------------------------------------------------------------------
btnClose = ttk.Button(frmMain, text = "Beenden", command = btnClose_click)
btnClose.place(x=160,y=80)
#------------------------------------------
# Endlosscheife
#------------------------------------------
frmMain.mainloop()