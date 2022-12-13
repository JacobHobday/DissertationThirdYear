#Get the timestamps of malicious pcaps from a filtered pcap file containing only malicious packets.

from scapy.all import PcapReader
import pandas as pd

pcap = PcapReader(r"C:\Users\jacob\Desktop\mk2\out\malicousFilteredPcaps\mitm-arpspoofing-1-decMalicious.pcap")

times =[]
for pkt in pcap:
   times.append(pkt.time)
   print(pkt.time)



pd.to_csv(times, index=False)
