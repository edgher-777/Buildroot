import os

print("Checking partition space")
envVar=os.popen("fw_printenv partitionData").read()

while envVar != "resized":
    envVar=os.popen("fw_printenv partitionData").read()
    try:
        partitionSize=int(os.popen("df -h --out=size /dev/mmcblk0p6").read())
    except:
        partitionSize=0
    if partitionSize <= 7000000:
        print("Resizing Partition")
        resizePartition=os.popen("resize2fs /dev/mmcblk0p6")
        setEnvVar=os.popen("fw_setenv partitionData resized").read()
    elif partitionSize==0:
        print("Partitionunavailable")
        setEnvVar=os.popen("Fw_setenv partitionData unavailable")
    else:
        print("Partition rezised")
        setEnvVar=os.popen("fw_setenv partitionData resized").read()

print("Disabling rezise service")
os.popen("systemctl disable resizeOnce").read()