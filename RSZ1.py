import os

envVar=os.popen("fw_printenv partitionData").read()

while not envVar == "partitionData=resized\n":
    try:
        s=os.popen("df /dev/mmcblk0p6 | grep /dev/mmcblk0p6").read()
        l=s.split()
        partitionSize=int(l[1])
    except:
        partitionSize=0
    if partitionSize <= 800000 and partitionSize > 1024 :
        resizePartition=os.popen("resize2fs /dev/mmcblk0p6")
        os.popen("fw_setenv partitionData resized").read()
    elif partitionSize==0:
        os.popen("fw_setenv partitionData unavailable")
    else:
        os.popen("fw_setenv partitionData resized").read()
    envVar=os.popen("fw_printenv partitionData").read()
