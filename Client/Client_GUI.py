from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import client
import glob
import os


root = Tk()
root.resizable(False, False)
root.iconbitmap("client_icon.ico")
root.title('INTRUSION DETECTION SYSTEM - Client')

HEIGHT = 600
WIDTH = 400
SCREEN_WIDTH = root.winfo_screenwidth() # width of the screen
SCREEN_HEIGHT = root.winfo_screenheight() # height of the screen
X_POS = 60
Y_POS = (SCREEN_HEIGHT/2) - (HEIGHT/2) - 30

root.geometry('%dx%d+%d+%d' % (WIDTH, HEIGHT, X_POS, Y_POS))

canvas = Canvas(root, height = HEIGHT, width = WIDTH)
canvas.pack()

global resp_text_conn, resp_text_file
global client_ip, client_port
global filename

resp_text_conn = ''
resp_text_file = ''


def client_connect(client_ip, client_port):
    resp_text_conn = 'Connection Status'
    label_resp1 = Label(upper_frame, text = resp_text_conn, bg='#97e6e1', font=30)
    label_resp1.place(x = 0,y = 120, relx=0.5, rely=0.5, anchor=CENTER)
    print ("IP Address : " +client_ip +"\nPort Number : " +client_port)
    client.connect_to_server(client_ip,int(client_port))
    messagebox.showinfo ("Client Information",("IP Address : " +client_ip + "\nPort Number : " +client_port))
    resp_text_conn = 'Connection Successful'
    label_resp1 = Label(upper_frame, text = resp_text_conn, bg='#97e6e1', font=30)
    label_resp1.place(x = 0,y = 120, relx=0.5, rely=0.5, anchor=CENTER)

def select_file():
    global filename
    wd = os.getcwd() + "././Data"
    filename =  filedialog.askopenfilename(initialdir = wd,title = "Select file",filetypes = ())
    print (filename)

def send_file():
    global filename
    resp_text_file = 'File Status'
    label_resp2 = Label(lower_frame, text = resp_text_file, bg='#97e6e1', font=30)
    label_resp2.place(x = 0,y = 0, relx=0.5, rely=0.35, anchor=CENTER)
    client.send_file_to_server(filename)
    resp_text_file = 'File Successfully Sent'
    label_resp2 = Label(lower_frame, text = resp_text_file, bg='#97e6e1', font=30)
    label_resp2.place(x = 0,y = 0, relx=0.5, rely=0.35, anchor=CENTER)

# UPPER FRAME

upper_frame = Frame(root, bg='#97e6e1')
upper_frame.place(relx=0.5, rely=0.02, relwidth=1, relheight=0.5, anchor='n')

label_IP = Label(upper_frame, text ='Enter the IP Address', bg='#97e6e1', font=30)
label_IP.place(x = 20,y = 50)

entry_IP = Entry(upper_frame,font=30)
entry_IP.place(x = 200,y = 50)


label_Port = Label(upper_frame, text ='Enter the Port Number', bg='#97e6e1', font=30)
label_Port.place(x = 20,y = 120)

entry_Port = Entry(upper_frame,font=30)
entry_Port.place(x = 200,y = 120)

connect_btn = Button(upper_frame, text ='Connect', font = 30, padx=30, command=lambda : client_connect(entry_IP.get(),entry_Port.get() ))
connect_btn.place(x = 0,y = 60, relx=0.5, rely=0.5, anchor=CENTER)

# LOWER FRAME

lower_frame = Frame(root, bg='#97e6e1')
lower_frame.place(relx=0.5, rely=0.55, relwidth=1, relheight=1, anchor='n')

label_File = Label(lower_frame, text ='Select the File to be Transmitted', bg='#97e6e1', font=30)
label_File.place(x = 20,y = 50)

select_btn = Button(lower_frame, text ='...', font = 30, command=select_file)
select_btn.place(x = 280,y = 45)

send_btn = Button(lower_frame, text ='SEND', font = 30, padx=50, command=lambda : send_file())
send_btn.place(x = 0,y = 0, relx=0.5, rely=0.25, anchor=CENTER)

root.mainloop()
