#!/bin/bash

nmap -p 8443 10.1.0.0/23| grep -B4 open | grep Nmap| cut -d " " -f 5


