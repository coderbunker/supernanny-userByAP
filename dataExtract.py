apCentral = []
apClassroom = []
apKitchen = []
apEntrance = []
apGallery = []
ap13B9 = []
ap16B9 = []
ap17B9 = []
currentList = ""

def write(line, currentList) :
    if currentList == "apClassroom" :
        apClassroom.append(line[:-1])
    elif currentList == "apKitchen" :
        apKitchen.append(line[:-1])
    elif currentList == "apEntrance" :
        apEntrance.append(line[:-1])
    elif currentList == "apCentral" :
        apCentral.append(line[:-1])
    elif currentList == "apGallery" :
        apGallery.append(line[:-1])
    elif currentList == "ap13B9" :
        ap13B9.append(line[:-1])
    elif currentList == "ap16B9" :
        ap16B9.append(line[:-1])
    elif currentList == "ap17B9" :
        ap17B9.append(line[:-1])
    else :
        print("error")


with open('/home/pi/userByAP/clientData.txt', 'rt') as myfile:
    for line in myfile:
        if len(line) == 10: #it's the ap header
        #    print("inloop "+line)
            if line[:-1] == "10.1.0.10": #meilleure solution??
                currentList = "apClassroom"
            elif line[:-1] == "10.1.0.11":
                currentList = "apCentral"
            elif line[:-1] == "10.1.0.12":
                currentList = "apKitchen"
            elif line[:-1] == "10.1.0.14":
                currentList = "apEntrance"
            elif line[:-1] == "10.1.0.13":
                currentList = "ap13B9"
            elif line[:-1] == "10.1.0.15":
                currentList = "apGallery"
            elif line[:-1] == "10.1.0.16":
                currentList = "ap16B9"
            elif line[:-1] == "10.1.0.17":
                currentList = "ap17B9"
            else :
                print("unable to identify AP")
                print("test"+line)

        else :
            write(line,currentList)

#print ("length "+str(len(apClassroom)))

with open('/home/pi/userByAP/influxData2.txt', 'w+') as influx:
    influx.write("AP,name=apClassroom value="+str(len(apClassroom))+ "\n")
    influx.write("AP,name=apKitchen value="+str(len(apKitchen))+ "\n")
    influx.write("AP,name=apEntrance value="+str(len(apEntrance))+ "\n")
    influx.write("AP,name=apCentral value="+str(len(apCentral))+ "\n")
    influx.write("AP,name=apGallery value="+str(len(apGallery))+ "\n")
    influx.write("AP,name=ap13B9 value="+str(len(ap13B9))+ "\n")
    influx.write("AP,name=ap16B9 value="+str(len(ap16B9))+ "\n")
    influx.write("AP,name=ap17B9 value="+str(len(ap17B9))+ "\n")

