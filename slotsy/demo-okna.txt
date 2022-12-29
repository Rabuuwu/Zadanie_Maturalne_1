# # tkinter             pip install tk
# import tkinter as tk

# window = tk.Tk()
# window.title("Slotsy v 1.0")
# window.geometry("800x600")

# newlabel = tk.Label(text = " Visit Pythonista Planet to improve your Python skills ")
# newlabel.grid(column=400,row=300)

# window.mainloop()

# # WxPython            pip install -U wxPython

# import wx

# a=wx.App()
# wx.Frame(None, title="Hello World").Show()
# a.MainLoop()

# # PyQT                python pip install pyQt5  python pip install pyQt5Designer
# from PyQt5 import QtWidgets
# from PyQt5.QtWidgets import QApplication, QMainWindow
# import sys


# class MyWindow(QMainWindow):
#     def __init__(self):
#         super(MyWindow,self).__init__()
#         self.initUI()

#     def button_clicked(self):
#         self.label.setText("you pressed the button")
#         self.update()

#     def initUI(self):
#         self.setGeometry(200, 200, 300, 300)
#         self.setWindowTitle("Tech With Tim")

#         self.label = QtWidgets.QLabel(self)
#         self.label.setText("my first label!")
#         self.label.move(50,50)

#         self.b1 = QtWidgets.QPushButton(self)
#         self.b1.setText("click me!")
#         self.b1.clicked.connect(self.button_clicked)

#     def update(self):
#         self.label.adjustSize()


# def window():
#     app = QApplication(sys.argv)
#     win = MyWindow()
#     win.show()
#     sys.exit(app.exec_())

# window()

# PyGUI                   pip install dearpygui
# from dearpygui.core import *
# from dearpygui.simple import *

# #ustawienia okna
# set_main_window_size(600,600)
# set_global_font_scale(1.25)
# set_theme("Dark") # Dark/Light/Classic/Dark2/Grey/Dark Grey/Cherry/Purple/Gold/Red

# with window("Test", width=300, height=200):
#     print("GUI")

# start_dearpygui()


# PySimpleGUI               pip install PySimpleGUI
# import PySimpleGUI as sg

# sg.theme('DarkAmber')   # Add a touch of color
# # All the stuff inside your window.
# layout = [  [sg.Text('Some text on Row 1')],
#             [sg.Text('Enter something on Row 2'), sg.InputText()],
#             [sg.Button('Ok'), sg.Button('Cancel')] ]

# # Create the Window
# window = sg.Window('Window Title', layout)
# # Event Loop to process "events" and get the "values" of the inputs
# while True:
#     event, values = window.read()
#     if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
#         break
#     print('You entered ', values[0])
# window.close()

# Kivy
#nie znalazłem NORMALNEJ instalacji a co dopiero robienie apki
