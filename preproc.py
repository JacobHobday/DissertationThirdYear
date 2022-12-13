
import pandas as pd
import sys

dfList = [r'C:\Users\jacob\Desktop\mk2\out\benign-dec.pcap_Flow.csv',
          r'C:\Users\jacob\Desktop\mk2\out\benign-dec.pcap_Flow.csv',
         ]

#df = sys.argv[0]
#dfJoin = sys.argv[1]
#df_all = sys.argv[2]
#pr = pd.read_csv(df)
#pr2 = pd.read_csv(dfJoin)

def main():
    df = pd.read_csv(r'C:\Users\jacob\Desktop\mk2\out\final.csv', sep=',')
    df_join = pd.read_csv(r'C:\Users\jacob\Desktop\mk2\out\dos-synflooding-1-dec.pcap_Flow.csv', sep=',')
    #combine dataframes
    df_all_rows = pd.concat([df, df_join]) 

    dfWrite = df_all_rows.to_csv(r'C:\Users\jacob\Desktop\mk2\out\final.csv', mode="a", index = False)
    print(df.shape)
    print(df_join.shape)
    print(df_all_rows.shape)

    testShape(dfWrite)

def testShape(dfWrite):
    print(pd.read_csv(r'C:\Users\jacob\Desktop\mk2\out\test.csv', sep=',').shape) 
   
main()
