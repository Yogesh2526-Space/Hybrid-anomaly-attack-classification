import tkinter
from tkinter import *
from server import run_server
import analyze_attack
import pandas as pd
import os
import csv
from plot import plot_hist

# ==============================
# 🎨 WINDOW SETUP
# ==============================
root = Tk()
root.resizable(False, False)
root.title('INTRUSION DETECTION SYSTEM - Server')

HEIGHT = 550
WIDTH = 350

SCREEN_WIDTH = root.winfo_screenwidth()
SCREEN_HEIGHT = root.winfo_screenheight()

X_POS = 900
Y_POS = int((SCREEN_HEIGHT / 2) - (HEIGHT / 2) - 30)

root.geometry('%dx%d+%d+%d' % (WIDTH, HEIGHT, X_POS, Y_POS))

canvas = Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

vals = None  # Global variable

# ==============================
# 🚀 MAIN FUNCTION
# ==============================
def call_server():
    global vals

    label_analyse.config(text="Receiving File...")
    root.update()

    try:
        # Start server
        vals = run_server()

        ip_value = vals[0]
        port_value = vals[1]
        file_name = vals[2]

        # Display values
        Label(frame, text=ip_value, bg='#97e6e1', font=12).place(x=200, y=100)
        Label(frame, text=port_value, bg='#97e6e1', font=12).place(x=200, y=150)

        label_analyse.config(text="Analyzing...")
        root.update()

        # Analyze file
        result = analyze_attack.analyze(
            ip=ip_value,
            port=port_value,
            filename=file_name
        )

        # Show result
        Label(frame, text=result, bg='#97e6e1',
              font=("Arial", 12, "bold")).place(x=70, y=450)

        label_analyse.config(text="Analysis Complete")

    except Exception as e:
        label_analyse.config(text="Error Occurred")
        print("Error:", e)


# ==============================
# 📊 STATISTICS WINDOW (FIXED)
# ==============================
def stat():
    file_path = os.path.join(os.getcwd(), "file_detail.csv")

    if not os.path.exists(file_path):
        print("No data found")
        return

    try:
        df = pd.read_csv(file_path)

        last_10 = df.tail(10)
        last_10.to_csv('last_10.csv', index=False)

        report_window = tkinter.Toplevel(root)
        report_window.title("Last 10 Records")

        with open("last_10.csv", newline="") as file:
            reader = csv.reader(file)
            for r, row in enumerate(reader):
                for c, value in enumerate(row):
                    Label(report_window,
                          text=value,
                          width=20,
                          height=2,
                          relief=RIDGE).grid(row=r, column=c)

        Button(report_window,
               text="Visualization",
               bg="red",
               fg="white",
               command=graph).grid(row=30, column=2)

    except Exception as e:
        print("Error in statistics:", e)


# ==============================
# 📈 GRAPH
# ==============================
def graph():
    plot_hist()


# ==============================
# 🎨 UI DESIGN
# ==============================
frame = Frame(root, bg='#97e6e1')
frame.place(relx=0, rely=0, relwidth=1, relheight=1)

Label(frame, text="Server Ready",
      bg='#97e6e1',
      font=("Arial", 18, "bold")).place(x=80, y=20)

Label(frame, text="IP Address:",
      bg='#97e6e1',
      font=("Arial", 12)).place(x=40, y=100)

Label(frame, text="Port Number:",
      bg='#97e6e1',
      font=("Arial", 12)).place(x=40, y=150)

label_analyse = Label(frame,
                      text="Waiting...",
                      bg='#97e6e1',
                      font=("Arial", 12))
label_analyse.place(x=110, y=250)

Button(frame, text='DETECT ATTACKS',
       font=("Arial", 12),
       padx=30,
       bg="#4CAF50",
       fg="white",
       command=call_server).place(x=70, y=325)

Button(frame, text='STATISTICS',
       font=("Arial", 12),
       padx=40,
       bg="#2196F3",
       fg="white",
       command=stat).place(x=90, y=400)


# ==============================
# 🚀 START GUI
# ==============================
root.mainloop()