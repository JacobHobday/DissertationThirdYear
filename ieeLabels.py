import pandas as pd


attackers =[]
#df = pd.read_csv('')


#for row in df:
#    if row.contains(attackers): #decide which label
#        df.insert() #add label


        

from scapy.all import PcapReader


#pcap = PcapReader("new/benign-dec.pcap")


pkts = PcapReader(r'C:\Users\jacob\Desktop\mk2\dataset\IEEEIOT\mal\mitm-arpspoofing-1-dec.pcap')


def mitmArpSpoof(pkts):
for pkt in pkts:
    if str(pkt['IP'].src) == "192.168.0.16" && str(pkt['IP'].dst) == "192.168.0.13":
        #insert 'benign' or 'mal' label into final column
        





def rdMethod():
    pkts = rdpcap(r'C:\Users\jacob\Desktop\mk2\dataset\IEEEIOT\mal\mitm-arpspoofing-1-dec.pcap')
    ports = [80, 25]
    filtered = (pkt for pkt in pkts if
        TCP in pkt and
        (pkt[TCP].sport in ports or pkt[TCP].dport in ports))
    wrpcap('filtered.pcap', filtered)




print(pkts)










eth.addr == f0:18:98:5e:ff:9f and ((((ip.src == 192.168.0.16 and ip.dst == 192.168.0.13) or (ip.src == 192.168.0.13 and ip.dst == 192.168.0.16)) and !icmp and tcp) or (arp.src.hw_mac == f0:18:98:5e:ff:9f and (arp.dst.hw_mac == bc:1c:81:4b:ae:ba or arp.dst.hw_mac == 48:4b:aa:2c:d8:f9)))
