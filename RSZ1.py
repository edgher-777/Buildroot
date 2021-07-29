import os

print("Checking partition space")
envVar=os.popen("fw_printenv partitionData").read()
print(envVar)

while not envVar == "partitionData=resized\n":
    try:
        s=os.popen("df /dev/mmcblk0p6 | grep /dev/mmcblk0p6").read()
        l=s.split()
        partitionSize=int(l[1])
        print(partitionSize)
    except:
        partitionSize=0
    if partitionSize <= 800000 and partitionSize > 1024 :
        print("Resizing Partition")
        resizePartition=os.popen("resize2fs /dev/mmcblk0p6")
        setEnvVar=os.popen("fw_setenv partitionData resized").read()
        print("Disabling resize service")
        os.popen("systemctl disable resizeOnce").read()
    elif partitionSize==0:
        print("Partition unavailable")
        setEnvVar=os.popen("fw_setenv partitionData unavailable")
    else:
        print("Partition rezised")
        os.popen("systemctl disable resizeOnce").read()
