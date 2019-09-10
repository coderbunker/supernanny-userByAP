#!/bin/bash
while true
do
/home/pi/userByAP/ap_list.sh > /home/pi/userByAP/ap_list.txt
/home/pi/userByAP/client_data.sh > /home/pi/userByAP/clientData.txt
python3  /home/pi/userByAP/dataExtract.py
curl -i -XPOST 'https://influxdb01.monitor.agora-space.com:8066/write?db=telegraf' -u telegraf:cookiesPancakes@work --data-binary @/home/pi/userByAP/influxData2.txt
sleep 20
done


