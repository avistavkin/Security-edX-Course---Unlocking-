from scapy.all import *
from scapy.layers.http import *
import sys # ignore
sys.path.insert(0,'.') # ignore
from create_recording import recording_path # the path to the pcap file of this assignment

#### Don't change the code until this line ####

def show_source_destination_ports():
    packets = rdpcap(recording_path)
#    pass # print destination port of third packet and source port of fourth packet
    packets = rdpcap(recording_path)
    for packet in packets:
        print ("port.src", packet.getlayer(TCP).sport)
        print ("port.dst", packet.getlayer(TCP).dport)

show_source_destination_ports()

"""
from scapy.all import *
from scapy.layers.http import *
import sys # ignore
sys.path.insert(0,'.') # ignore
from create_recording import recording_path # the path to the pcap file of this assignment

#### Don't change the code until this line ####

def show_source_destination_ports():
    packets = rdpcap(recording_path)
#    pass # print destination port of third packet and source port of fourth packet
    packets = rdpcap(recording_path)
    #for packet in packets:
"""
    print ("port.src", packets[1][0].show()) # вот с этой строкой надо будет поразбираться
"""
     #   packet.getlayer(TCP).sport)
     #   print ("port.dst", packet.getlayer(TCP).dport)

show_source_destination_ports()
"""

#Bingo - вот такой вариант сработал!!!!!!

from scapy.all import *
from scapy.layers.http import *
import sys # ignore
sys.path.insert(0,'.') # ignore
from create_recording import recording_path # the path to the pcap file of this assignment

#### Don't change the code until this line ####

def show_source_destination_ports():
    packets = rdpcap(recording_path)
#    pass # print destination port of third packet and source port of fourth packet
    packets = rdpcap(recording_path)
"""
#    for i in range(len(packets)):
#        print ("###packet ",i, "###", packets[i].summary())
"""
    print (packets[2].getlayer(TCP).dport) # печатает порт получателя 3-го пакета
    print (packets[3].getlayer(TCP).sport) # печатает порт отправителя 4-го пакета


show_source_destination_ports()