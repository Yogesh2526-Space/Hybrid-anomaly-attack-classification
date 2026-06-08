# import matplotlib.pyplot as plt
# import pandas as pd
# import os

# def plot_hist():
#     file_path = "file_detail.csv"

#     # ✅ Check file exists
#     if not os.path.exists(file_path):
#         print("No data available for plotting")
#         return

#     try:
#         df = pd.read_csv(file_path)

#         # ✅ Count attack types
#         counts = df["Type"].value_counts()

#         print("\nAttack Summary:\n", counts)

#         # ✅ Plot graph
#         counts.plot(kind='bar')

#         plt.ylabel('Number Of Attacks')
#         plt.xlabel('Type Of Attack')
#         plt.title('Intrusion Detection Statistics')

#         plt.xticks(rotation=0)
#         plt.tight_layout()

#         plt.show()

#     except Exception as e:
#         print("Error in plotting:", e)



import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


def plot_hist():
    PATH = 'file_detail.csv'
    df = pd.read_csv('file_detail.csv')

    df = pd.DataFrame(df, columns=['Type'])
    df = df['Type'].value_counts().to_frame().reset_index().rename(
        columns={'index': 'values', 'values': 'count'})
    df.to_csv('./consol.csv', encoding='utf-8',
              mode='w', header=False, index=False)

    print(df)
    
    data = pd.read_csv('./consol.csv', sep=',', header=None, index_col=0)
    
    data.plot(kind='bar', alpha=0.75, rot=0, legend=None)
    #plt.figure(figsize=(12,8))
    plt.ylabel('Number Of Attack')
    plt.xlabel('Type Of Attack')
    plt.title('STATISTICS')
    
    plt.show()