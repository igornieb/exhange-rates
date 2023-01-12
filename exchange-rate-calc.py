from tkinter import *
from ttkwidgets.autocomplete import AutocompleteCombobox
import requests

class ExchangeRate:
    currency1=""
    curency2=""
    def __init__(self,c1,c2):
        self.currency1=c1
        self.curency2=c2
    def return_exchange_rate(self):
        url = 'https://api.exchangerate.host/convert?from='+self.currency1+'&to='+self.curency2+''
        response = requests.get(url)
        data = response.json()
        return data['result']

def convert(frame, input, output,amount):
    try:
        e=ExchangeRate(input.get(),output.get())
        amount="%.2f" %(amount*e.return_exchange_rate())
        return Label(frame, text=str(amount)+" "+e.curency2).grid(row=4, column=1, sticky="ew")
    except:
        return Label(frame, text="Error :(").grid(row=4, column=1, sticky="ew")


def menu():
    try:
        url = 'https://api.exchangerate.host/symbols'
        response = requests.get(url)
        data = response.json()
        currencies=list(data['symbols'])
    except:
        exit()
    window = Tk()
    window.title("exchange-rates")
    #window.iconbitmap('logo.ico')
    frame= Frame(width=250, height=250)
    frame.pack(fill="both", expand=True, padx=20, pady=20)
    input=StringVar()
    output=StringVar()
    amount=StringVar()
    Label(frame, text="Input").grid(row=1, column=0, sticky="ew")
    AutocompleteCombobox(frame, textvariable=input, completevalues=currencies).grid(row=2,column=0)
    Label(frame, text="Output").grid(row=1, column=2, sticky="ew")
    AutocompleteCombobox(frame, textvariable=output, completevalues=currencies).grid(row=2,column=2)
    Label(frame, text="Amount").grid(row=3, column=0, sticky="ew")
    Entry(frame, text="0", textvariable=amount).grid(row=3, column=1, sticky="ew")
    Button(frame, text="Convert", command=lambda:convert(frame,input,output,float(amount.get()))).grid(row=5, column=1, sticky="ew")
    Button(frame, text="Exit", command=lambda:exit()).grid(row=6, column=1, sticky="ew")
    mainloop()


if __name__=="__main__":
    menu()