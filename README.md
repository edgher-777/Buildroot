These changes are to create a RO system and set a RW folder creating a disk partition

File directory to be replaced:
board/raspberrypi4/genimage-raspberrypi4.cfg

File directory to be created:
board/raspberrypi4/overlay/etc/fstab

File directories need to be created:
board/raspberrypi4/overlay/CFA002WIFI/wifi
board/raspberrypi4/overlay/CFA002WIFI/update
board/raspberrypi4/overlay/CFA002WIFI/traceability
board/raspberrypi4/overlay/CFA002WIFI/SerialNumber
board/raspberrypi4/overlay/var/lock
board/raspberrypi4/overlay/data
board/raspberrypi4/overlay/boot
board/raspberrypi4/overlay/fstab*
board/raspberrypi4/overlay/fw_env.config*
board/raspberrypi4/overlay/rauc/demo.cert.pem*
board/raspberrypi4/overlay/rauc/demo.key.pem*
board/raspberrypi4/overlay/rauc/system.config*
board/raspberrypi4/overlay/etc/cpuinfo*
board/cmdline.txt*
board/config.txt*

System configuration:
Rootfilesystem overlay directories: board/raspberrypi4/overlay
