# userByAP
Script that lists the number of user connected by AP and send the data to the bunker InfluxDB database.

Run data2Influx.sh to excecute the script.

First version is the same as the one deployed on pi-bunker and does not take account of dynamic IPs for AP as they are hard coded on 10.1.0.0/24

ap_list.sh and client_data.sh come from https://github.com/lenzai/monitor_asus 
