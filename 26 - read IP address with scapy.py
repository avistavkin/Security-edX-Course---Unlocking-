from scapy.all import *
from scapy.layers.http import *
import sys # ignore
sys.path.insert(0,'.') # ignore
from create_recording import recording_path # the path to the pcap file of this assignment

#### Don't change the code until this line ####

def show_source_destination_ip_address():
    packets = rdpcap(recording_path)
    for packet in packets:
        print ("packet.src", packet.getlayer(IP).src)
        print ("packet.dst", packet.getlayer(IP).dst)
    
show_source_destination_ip_address()