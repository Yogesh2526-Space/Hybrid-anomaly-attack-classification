import socket
import os
from datetime import datetime

def run_server():
    s = socket.socket()

    # ✅ reuse port
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    host = "127.0.0.1"
    port = 9999

    s.bind((host, port))
    s.listen(1)

    print("🚀 Server Listening...")

    conn, addr = s.accept()
    print("🔗 Connection from:", addr)

    # ==============================
    # 📥 STEP 1: Receive filename
    # ==============================
    filename = conn.recv(1024).decode().strip()

    if not filename:
        filename = "received_file.txt"

    print("📂 Receiving file:", filename)

    # ==============================
    # 📁 STEP 2: Ensure Data folder
    # ==============================
    data_folder = "Data"
    if not os.path.exists(data_folder):
        os.makedirs(data_folder)

    # ==============================
    # 🕒 STEP 3: Add timestamp (VERY IMPORTANT)
    # ==============================
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    new_filename = f"{timestamp}_{filename}"

    filepath = os.path.join(data_folder, new_filename)

    # ==============================
    # 💾 STEP 4: Save file
    # ==============================
    with open(filepath, "wb") as f:
        while True:
            data = conn.recv(1024)
            if not data:
                break
            f.write(data)

    print("✅ File Received Successfully:", new_filename)

    conn.close()
    print("🔒 Connection Closed")

    # ==============================
    # 🔁 STEP 5: Return values
    # ==============================
    return [addr[0], addr[1], new_filename]