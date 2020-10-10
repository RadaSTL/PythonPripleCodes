import json
import tkinter as tk
import urllib.request
import random as r
import time as t
from termcolor import colored
import threading as thd


# print(json.dumps(data, indent=5))


def update_label(label1, label2, label3):
    def run():
        USD,EUR,GBP=0,0,0
        for i in range(10):
            jsonData = urllib.request.urlopen("https://api.coindesk.com/v1/bpi/currentprice.json")
            data = json.loads(jsonData.read())
            print(data)
            BPIVal = data.get("bpi")
            USDVal = BPIVal.get("USD")
            USDVal = USDVal.get("rate_float")
            GBPVal = BPIVal.get("GBP")
            GBPVal = GBPVal.get("rate_float")
            EURVal = BPIVal.get("EUR")
            EURVal = EURVal.get("rate_float")
            prevUSD = USD
            USD = USDVal
            if USD > prevUSD:
                label1.config(fg="green")
            elif USD < prevUSD:
                label1.config(fg="red")
            else:
                label1.config(fg="black")
            strUSDVal.set(str(USD))

            prevGBP = GBP
            GBP = GBPVal
            if GBP > prevGBP:
                label2.config(fg="green")
            elif GBP < prevGBP:
                label2.config(fg="red")
            else:
                label2.config(fg="black")
            strGBPVal.set(str(GBP))

            prevEUR = EUR
            EUR = EURVal
            if EUR > prevEUR:
                label3.config(fg="green")
            elif EUR < prevEUR:
                label3.config(fg="red")
            else:
                label3.config(fg="black")
            strEURVal.set(str(EUR))
            mainWindow.update()
            t.sleep(5)
    thread = thd.Thread(target=run)
    thread.start()


mainWindow = tk.Tk()
mainWindow.title("BitCoin Follower")
strUSDVal = tk.StringVar(mainWindow)
strGBPVal = tk.StringVar(mainWindow)
strEURVal = tk.StringVar(mainWindow)
testBtn = tk.Button(mainWindow, text="Exit", width=25, command=mainWindow.destroy)
testCanvas = tk.Frame(mainWindow, width=50, bg="white")
CurLabelUSD = tk.Label(testCanvas, text="USD:")
CurLabelUSDVal = tk.Label(testCanvas, textvariable=strUSDVal)
CurLabelGBPVal = tk.Label(testCanvas, textvariable=strGBPVal)
CurLabelEURVal = tk.Label(testCanvas, textvariable=strEURVal)
connectButton = tk.Button(mainWindow, text="Connect", width=25, command=lambda: update_label(CurLabelUSDVal,CurLabelGBPVal,CurLabelEURVal))
CurLabelGBP = tk.Label(testCanvas, text="GBP:")
CurLabelEUR = tk.Label(testCanvas, text="EUR:")
# testBtn.config(text="Click")

testCanvas.pack()
CurLabelUSD.grid(row=0, column=0)
CurLabelUSDVal.grid(row=0, column=1)
CurLabelGBP.grid(row=1, column=0)
CurLabelGBPVal.grid(row=1, column=1)
CurLabelEUR.grid(row=2, column=0)
CurLabelEURVal.grid(row=2, column=1)
connectButton.pack()
testBtn.pack()
mainWindow.mainloop()
