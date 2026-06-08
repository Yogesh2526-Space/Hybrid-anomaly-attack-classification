import binascii
import os
import time
import hashlib
import csv
import math
from sklearn.ensemble import IsolationForest

# ==============================
# 📁 BASE PATH
# ==============================
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CSV_PATH = os.path.join(BASE_DIR, "file_detail.csv")

# ==============================
# 🔐 ENTROPY
# ==============================
def calculate_entropy(data):
    if len(data) == 0:
        return 0

    freq = {}
    for byte in data:
        freq[byte] = freq.get(byte, 0) + 1

    entropy = 0
    for count in freq.values():
        p = count / len(data)
        entropy -= p * math.log2(p)

    return entropy


# ==============================
# 🧠 ANALYZE FUNCTION
# ==============================
def analyze(ip="127.0.0.1", port="9999", filename="received_file.txt"):

    filepath = os.path.join("Data", filename)

    if not os.path.exists(filepath):
        print("File not found:", filepath)
        return "Error"

    with open(filepath, 'rb') as f:
        content = f.read()
        content_hex = binascii.hexlify(content).decode('utf-8')
        file_hash = hashlib.md5(content).hexdigest()

    # ==============================
    # 📊 FEATURES
    # ==============================
    file_size = len(content)
    unique_bytes = len(set(content))
    entropy = calculate_entropy(content)

    features = [[file_size, unique_bytes, entropy]]

    # ==============================
    # 🤖 MODEL
    # ==============================
    model = IsolationForest(contamination=0.2, random_state=42)

    train_data = [
        [500, 100, 3.5],
        [800, 150, 4.0],
        [1200, 200, 4.5],
        [2000, 250, 5.0],
        [300, 50, 2.0],
        [100, 20, 1.5]
    ]

    model.fit(train_data)
    prediction = model.predict(features)

  
    # ==============================
    # 🔍 SIGNATURE-BASED DETECTION
    # ==============================

    # Convert file to hex string
    content_hex = binascii.hexlify(content).decode('utf-8')

    def check(signature):
        return signature.lower() in content_hex.lower()

    # ------------------------------
    # SIGNATURES
    # ------------------------------
    search_string_virus = "56 69 72 75 73 20 44 42 20 49 6e 69 74 69 61 6c 69 7a 69 6e 67".replace(" ", "")
    search_string_mime = "4d 61 6e 20 49 6e 20 4d 69 64 64 6c 65 20 44 42 20 49 6e 69 74 69 61 6c 69 7a 69 6e 67".replace(" ", "")
    search_string_dos = "44 65 6e 69 61 6c 20 6f 66 20 53 65 72 76 69 63 65 20 44 42 20 49 6e 69 74 69 61 6c 69 7a 69 6e 67".replace(" ", "")
    search_string_ping1 = "70 69 6e 67 20 2d 63 20 35 30".replace(" ", "")
    search_string_ping2 = "70 69 6e 67 20 2d 6e 20 35 30".replace(" ", "")
    search_string_AV1 = "65 6c 65 63 74 20 2a 20 66 72 6f 6d 20 41 6e 74 69 56 69 72 75 73 50 72 6f 64 75 63 74 22".replace(" ", "")
    search_string_AV2 = "48 4b 45 59 5f 4c 4f 43 41 4c 5f 4d 41 43 48 49 4e 45".replace(" ", "")

    # ------------------------------
    # CHECK SIGNATURES
    # ------------------------------
    if check(search_string_virus):
        res = "Virus File"
        print("🔴 Virus Signature Found")

    elif check(search_string_mime):
        res = "Man In Middle File"
        print("🔴 MITM Attack Found")

    elif check(search_string_dos):
        res = "DOS File"
        print("🔴 DOS Attack Found")

    elif check(search_string_ping1) or check(search_string_ping2):
        res = "DDoS Attack File"
        print("🔴 DDoS Attack Found")

    elif check(search_string_AV1) or check(search_string_AV2):
        res = "AV Evasion File"
        print("🔴 Antivirus Evasion Found")

    # ------------------------------
    # 🤖 ML FALLBACK
    # ------------------------------
    elif prediction[0] == -1:
        res = "Anomaly Detected"
        print("🟡 ML Anomaly Detected")

    else:
        res = "Normal File"
        print("🟢 Normal File")

        print("📍 CSV PATH:", CSV_PATH)  # DEBUG

    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")

    safe_row = [
        str(ip),
        str(port),
        str(filename),
        str(timestamp),
        str(file_hash),
        str(res)
    ]

    try:
        print("✍ Writing to CSV...")  # DEBUG

        file_exists = os.path.isfile(CSV_PATH)

        with open(CSV_PATH, 'a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)

            if not file_exists:
                print("🆕 Creating new CSV file")  # DEBUG
                writer.writerow([
                    "IP_Address",
                    "Port_Number",
                    "File_Name",
                    "TimeStamp",
                    "File_Hash",
                    "Type"
                ])

            writer.writerow(safe_row)

        print("✅ CSV WRITE SUCCESS")  # DEBUG

    except Exception as e:
        print("❌ CSV WRITE ERROR:", e)
        
        # # ==============================
        # # 💾 SAFE CSV WRITE (FIXED)
        # # ==============================
        # file_exists = os.path.isfile(CSV_PATH)
        # timestamp = time.strftime("%Y-%m-%d %H:%M:%S")

        # # 🚀 CLEAN VALUES (IMPORTANT FIX)
        # safe_row = [
        #     str(ip).replace(",", ""),
        #     str(port).replace(",", ""),
        #     str(filename).replace(",", ""),  #str(filename).replace(",", "_"),
        #     str(timestamp).replace(",", ""),
        #     str(file_hash).replace(",", ""),
        #     str(res).replace(",", "")
        # ]

        # with open(CSV_PATH, 'a', newline='', encoding='utf-8') as file:
        #     writer = csv.writer(file)

        #     if not file_exists:
        #         writer.writerow([
        #             "IP_Address",
        #             "Port_Number",
        #             "File_Name",
        #             "TimeStamp",
        #             "File_Hash",
        #             "Type"
        #         ])

        #     writer.writerow(safe_row)

        # with open('file_detail.txt', 'a') as file_detail:
        #     file_detail.write("\t" + res)    

        # return res