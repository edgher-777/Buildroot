import os
import logging

logger = logging.getLogger("DEBUG")
logger.debug("Checking partition space")
envVar=os.popen("fw_printenv partitionData").strip().read()

while envVar != "resized":
    envVar=os.popen("fw_printenv partitionData").read()
    partitionSize=int(os.popen("df -h --out=size /dev/mmcblk0p6").read())
    if partitionSize < 7000000:
        logger.debug("Resizing Partition")
        resizePartition=os.popen("resize2fs /dev/mmcblk0p6")
        setEnvVar=os.popen("fw_setenv partitionData resized").read()
    else:
        setEnvVar=os.popen("fw_setenv partitionData resized").read()
logger.debug("Disabling rezise service")
os.popen("systemctl disable resizeOnce").read()