import pandas as pd
import os

# Writting CSV File

if not os.path.exists('./file_detail.csv'):

    read_file = pd.read_csv(
        str(os.getcwd()) + "\\file_detail.txt", delimiter='\t')
    df = pd.DataFrame(read_file, columns=[
        "IP_Address", "Port_Number", "File_Name", "TimeStamp", "File_Hash", "Type"])

    df.to_csv('./file_detail.csv', encoding='utf-8',
              mode='a', header=True, index=False)
else:
    read_file = pd.read_csv(
        str(os.getcwd()) + "\\file_detail.txt", delimiter='\t')
    read_file.to_csv('./file_detail.csv', index=None, mode='a')
