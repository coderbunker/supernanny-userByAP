#!/bin/bash
for ip in `cat /home/pi/userByAP/ap_list.txt`; do
  for interface in `ssh admin@$ip /sbin/ifconfig | grep eth| tail -n2| cut -d " " -f 1`; do
  	echo $ip
    #grep "$ip $interface" cache/ap_mac.txt
    ssh admin@$ip /usr/sbin/wl -i $interface assoclist | cut -d " " -f 2;
  done;
done;

#(for ip in `cat ap_list.txt`;  do ssh admin@$ip /sbin/arp -a; done;) | cut -d " " -f2,4 | sed s/[\(\)]//g | tee arp.txt


