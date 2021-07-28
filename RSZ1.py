import os
import logging

logger = logging.getLogger("DEBUG")
debug_logger.debug("Checking partition space")
envVar=os.popen("fw_printenv partitionData").read()

while envVar != "resized"
envVar=os.popen("fw_printenv partitionData").read()
partitionSize=int(os.popen("df -h --out=size /dev/mmcblk0p6").read())
    if partitionSize < 7000000:
        resizePartition=os.popen("resize2fs /dev/mmcblk0p6")
        setEnvVar=os.popen("fw_setenv partitionData resized").read()
    else:
        setEnvVar=os.popen("fw_setenv partitionData resized").read()

os.popen("systemctl disable resizeOnce")