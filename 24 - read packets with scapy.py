#вот этот код даёт ответ
from scapy.all import *
from scapy.layers.http import *
import sys # ignore
sys.path.insert(0,'.') # ignore
from create_recording import recording_path # the path to the pcap file of this assignment

#### Don't change the code until this line ####

def show_mac_address():
    packets = rdpcap(recording_path)
    for packet in packets:
        print ("packet.src", packet.src)
        print ("packet.dst", packet.dst)
    

show_mac_address()



#вот этот код в принципе выполняется


from scapy.all import *
from scapy.layers.http import *
import sys # ignore
sys.path.insert(0,'.') # ignore
from create_recording import recording_path # the path to the pcap file of this assignment

#### Don't change the code until this line ####

def show_mac_address():
    packets = rdpcap(recording_path)
    for packet in packets:
    # We're only interested packets with a DNS Round Robin layer
        if packet.haslayer(DNSRR):
            # If the an(swer) is a DNSRR, print the name it replied with.
            if isinstance(packet.an, DNSRR):
                print(packet.an.rrname)
        # We're only interested packets with a DNS Round Robin layer
 

show_mac_address()