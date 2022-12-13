#Get a list & the count of every IP found in pcap.

from scapy.all import PcapReader

import pandas as pd

pcap = PcapReader("new/benign-dec.pcap") 


ipList = []
for pkt in pcap:
    try:
        src = pkt['IP'].src
        dst = pkt['IP'].dst
        
        ipList.append(src)
        ipList.append(dst)
    except:
        print(float(pkt.time))
       
ipList = list(dict.fromkeys(ipList)
print(pd.Series(ipList).is_unique)
print("ADDRS: \n")
print(len(ipList))
