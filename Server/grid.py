
import tkinter
import csv
import pandas as pd
import os
from plot import plot_hist


def graph():
    plot_hist()


def disp_grid():
    window = tkinter.Tk()
    WIDTH = window.winfo_screenwidth() - 70
    HEIGHT = 450
    window.geometry(f'{WIDTH}x{HEIGHT}')
    window.title("Intrusion Detection System - Last 10 - Report")




    read_file = pd.read_csv(
        str(os.getcwd()) + "\\file_detail.txt", delimiter='\t')
    df = pd.DataFrame(read_file, columns=[
        "IP_Address", "Port_Number", "File_Name", "TimeStamp", "File_Hash", "Type"])

    df.to_csv('./last_10.csv', encoding='utf-8',
              mode='w', header=True, index=False)

    last_10 = pd.read_csv('file_detail.csv', sep = ',')
    last_10 = last_10.tail(10)
    print (last_10)

   
    last_10.to_csv('./last_10.csv', encoding='utf-8',
              mode='a', header=False, index=False)


                 

    with open("last_10.csv", newline="") as file:
        reader = csv.reader(file)
        r = 10
        for col in reader:
            c = 2
            for row in col:
                label = tkinter.Label(
                    window, width=30, height=2, text=row, relief=tkinter.RIDGE)
                label.grid(row=r, column=c)
                c += 1
            r += 1

    btn = tkinter.Button(window, text='Visualization',
                         bg='#ef2f23', fg='white', command=graph)
    btn.grid(row=30, column=4, columnspan=2, pady=20)
    window.mainloop()


disp_grid()
