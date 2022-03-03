import sys
import requests
from scapy.all import *

def taro_sent(size):
    response = requests.post('https://a8visualizer.herokuapp.com/taro_sent', data={'passphrase': 'PASS', 'size': size})
    print(response.text)

def hanako_received(size):
    response = requests.post('https://a8visualizer.herokuapp.com/hanako_received', data={'passphrase': 'PASS', 'size': size})
    print(response.text)

def reset_game():
    response = requests.post('https://a8visualizer.herokuapp.com/reset_game', data={'passphrase': 'PASS'})
    print(response.text)

def register_user(name):
    response = requests.post('https://a8visualizer.herokuapp.com/register_player', data={'passphrase': 'PASS', 'name': name })
    print(response.text)

if __name__ == '__main__':
    print("Hello robachan!!")
    args = sys.argv
    if 2 <= len(args) and sys.argv[1] == 'hanako':
        print("I am hanako!")
        while (True):
            pkts = sniff(iface="eth0", count=1)
            for pkt in pkts:
                print(len(pkt.payload))
                hanako_received(len(pkt.payload))
    else:
        print("I am taro")
        while(True):
            pkts = sniff(iface="eth1", count=1)
            for pkt in pkts:
                print(len(pkt.payload))
                taro_sent(len(pkt.payload))
