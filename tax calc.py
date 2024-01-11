'''
my tax calculator works by taking a number from the user, putting it through multiple functions that represent
the different federal income tax brackets, and returning the sum of the results from every bracket
'''

import tkinter as tk
from tkinter import messagebox

#this does the calculations for every bracket
def first_bracket(income):
    if income >= 9700:
        return 970
    else:
        return income * 0.1
        
def second_bracket(income):
    if income >= 39475:
        return 3573
    elif income <= 9700:
        return 0
    elif income > 9700:
        return (income - 9700) * 0.12

def third_bracket(income):
    if income >= 84200:
        return 9839.5
    elif income <= 39475:
        return 0
    if income > 39475:
        return (income - 39475) * 0.22

def fourth_bracket(income):
    if income >= 160725:
        return 18366
    elif income <= 84200:
        return 0
    if income > 84200:
        return (income - 84200) * 0.24

def fifth_bracket(income):
    if income >= 204100:
        return 13880
    elif income <= 160725:
        return 0
    if income > 160725:
        return (income - 160725) * 0.32

def sixth_bracket(income):
    if income >= 510301:
        return 107170.35
    elif income <= 204100:
        return 0
    if income > 204100:
        return (income - 204100) * 0.35

def seventh_bracket(income):
    if income > 510300:
        return (income - 510300) * 0.37
    else:
        return 0
#this combines the equations for every bracket to get one final $ amount

def calculator(income):
    yearly_federal_income_tax = 0.
    yearly_federal_income_tax += first_bracket(income)
    yearly_federal_income_tax += second_bracket(income)
    yearly_federal_income_tax += third_bracket(income)
    yearly_federal_income_tax += fourth_bracket(income)
    yearly_federal_income_tax += fifth_bracket(income)
    yearly_federal_income_tax += sixth_bracket(income)
    yearly_federal_income_tax += seventh_bracket(income)
    return yearly_federal_income_tax

#this creates the GUI
class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):

#takes the users input, puts it through the calculator function, and returns the result in the form of a new window
        def get_income(income):
            income = float(self.text_box.get())
            messagebox.showinfo('result', 'you owe $' + str(calculator(income)) + ' in federal income tax')

#makes attributes of the GUI
        self.prompt = tk.Label(master=root, text='enter your yearly taxable income followed by the enter key')
        self.prompt.anchor('n')
        self.prompt.pack()
        self.text_box = tk.Entry(master=root)
        self.text_box.bind( '<Return>' , get_income)        
        self.text_box.pack()




root = tk.Tk()
app = Application(master=root)
app.mainloop() 

#prints the amount of tax you would pay on the values 9700, 39475, 100000, and 1000000
print(calculator(9700))
print(calculator(39475))
print(calculator(100000))
print(calculator(1000000))