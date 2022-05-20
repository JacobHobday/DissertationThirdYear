
import pandas as pd
import numpy as np
import tensorflow as tf
from tensorflow.keras.layers import Dense, Input
from tensorflow.keras.models import Sequential

flagSet = ['F', 'S', 'R', 'P', 'A', 'U', 'E', 'C']


"""

tshark -r test.pcap -T fields
-e frame.number -e frame.time -e eth.src -e eth.dst -e ip.src -e ip.dst -e ip.proto -e col.info -e data.data -E separator=,


tshark -r benign-dec.pcap -T fields -e frame.number -e frame.time_epoch -e eth.src -e eth.dst -e ip.src -e ip.dst -e ip.proto -e data.data -E separator=, > benign.csv 
#57999
"""

dfList = [r'C:\Users\jacob\Desktop\mk2\out\benign-dec.pcap_Flow.csv',
          r'C:\Users\jacob\Desktop\mk2\out\benign-dec.pcap_Flow.csv',

    ]

df = pd.read_csv(r'C:\Users\jacob\Desktop\mk2\out\benign-dec.pcap_Flow.csv', sep=',')
print(df[0:5])
df_join = pd.read_csv(r'C:\Users\jacob\Desktop\mk2\out\dos-synflooding-1-dec.pcap_Flow.csv', sep=',')



print("df shapes:")
print(df.shape)
print(df_join.shape)


df_all_rows = pd.concat([df, df_join]) #combine dataframes
npArr = np.array(df_all_rows)

print("====================================\n")
print("====================================\n")
print("====================================\n")
print("====================================\n")
#print(npArr[:5])
print(npArr.shape)




#ipSrcObj = df['ipSrc'] #ipSrc column object
#print(ipSrcObj.values)

"""
#NEED TO CHANGE NAME LIST
for name in df.columns:
  if name == 'Label':
    pass
  elif name in ['protocol_type','service','flag','land','logged_in',
                'is_host_login','is_guest_login']:
    encode_text_dummy(df,name)
  else:
    encode_numeric_zscore(df,name) 

"""





model =Sequential()
model.add(Dense(10, input_shape=(150, 10), activation= "relu"))
model.add(Dense(5, activation = "relu"))
model.add(Dense(1, activation = "sigmoid"))
print(model.summary())


tf.keras.layers.Dense(1500, activation="relu")
#tf.keras.layers.output(softmax)
    
