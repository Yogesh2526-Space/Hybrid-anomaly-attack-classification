import socket
import os
import time

def connect_to_server(host, port):
    global s
    s = socket.socket()
    s.connect((host, port))

def send_file_to_server(fname):
    global s

    # ✅ Extract filename
    filename = os.path.basename(fname)

    # ✅ STEP 1: Send filename first
    s.send(filename.encode())
    time.sleep(1)   # ⚠ Important (prevents mixing with file data)

    # ✅ STEP 2: Send file content
    with open(fname, "rb") as f:
        while True:
            data = f.read(1024)
            if not data:
                break
            s.send(data)

    print("File Sent Successfully")
    s.close()