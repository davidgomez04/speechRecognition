import speech
import browser as wb
import tkinter as tk

window = tk.Tk()
window.title('Speech UI')
 
window.geometry('500x500')

def print_selection():
    value = lb.get(lb.curselection())   
    inputVar.set(value)  
 
lb = tk.Listbox(window, height = 10, width = 40)

mic_list = speech.computerMicList()

i = 1
for mic, index in mic_list.items():
    lb.insert(i, mic)
    i = i + 1
lb.pack()

inputVar = tk.StringVar()
label = tk.Label(window, font=('Arial', 12), width=40, textvariable=inputVar)
label.pack()

b1 = tk.Button(window, text='Select Mic', width=15, height=2, command=print_selection)
b1.pack()

speechBt = tk.Button(window, text='Run Speech UI', width=15, height=2, command=speech.run)
speechBt.pack()
 
window.mainloop()



        