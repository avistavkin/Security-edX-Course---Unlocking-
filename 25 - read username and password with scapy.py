from scapy.all import *
from scapy.layers.http import *
import sys # ignore
sys.path.insert(0,'.') # ignore
from create_recording import recording_path # the path to the pcap file of this assignment

#### Don't change the code until this line ####

def show_username_password():
    packets = rdpcap(recording_path)
    bind_layers(TCP, HTTP, dport=8000)
    bind_layers(TCP, HTTP, sport=8000)
    
    packets = rdpcap(recording_path)
    
    pattern = 'username=(.*)&password=([^\s]+)'
    
    username = ""
    password = ""
    overWriteValues = True
    for packet in packets:
    
        ascii = raw(packet[HTTP]).decode("ascii")
        match = re.search(pattern, ascii)
    
        invalidCredentials = ascii.find("Invalid credentials.") != -1
    
        if invalidCredentials:
            overWriteValues = True
    
        if overWriteValues and match:
            username = match.group(1)
            password = match.group(2)
            overWriteValues = False
    
    print("username: " + username, "password: " + password, sep='\n')

show_username_password()
