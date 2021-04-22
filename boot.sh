fdt addr ${fdt_addr} && fdt get value bootargs /chosen bootargs

test -n "${BOOT_ORDER}" || setenv BOOT_ORDER "A B"
test -n "${BOOT_A_LEFT}" || setenv BOOT_A_LEFT 3
test -n "${BOOT_B_LEFT}" || setenv BOOT_B_LEFT 3
test -n "${BOOT_DEV}" || setenv BOOT_DEV "mmc 0:1"

setenv bootpart
setenv raucslot

for BOOT_SLOT in "${BOOT_ORDER}"; do
  if test "x${bootpart}" != "x"; then
    # skip remaining slots
  elif test "x${BOOT_SLOT}" = "xA"; then
    if test ${BOOT_A_LEFT} -gt 0; then
      setexpr BOOT_A_LEFT ${BOOT_A_LEFT} - 1
      echo "Found valid RAUC slot A"
      setenv bootpart "/dev/mmcblk0p3"
      setenv raucslot "A"
    fi
  elif test "x${BOOT_SLOT}" = "xB"; then
    if test ${BOOT_B_LEFT} -gt 0; then
      setexpr BOOT_B_LEFT ${BOOT_B_LEFT} - 1
      echo "Found valid RAUC slot B"
      setenv bootpart "/dev/mmcblk0p5"
      setenv raucslot "B"
    fi
  fi
done

setenv boot_targets "mmc0"
setenv devtype "mmc"
setenv devnum "0"
setenv distro_bootpart "1"
setenv boot_scripts "boot.scr"
setenv script "boot.scr"
setenv prefix "/"
setenv mmc_boot "run scan_dev_for_scripts"

if test -n "${bootpart}"; then
  setenv bootargs "${bootargs} root=${bootpart} rauc.slot=${raucslot}"
  saveenv
else
  echo "No valid RAUC slot found. Resetting tries to 3"
  setenv BOOT_A_LEFT 3
  setenv BOOT_B_LEFT 3
  reset
fi

if test "${raucslot}" = "A"; then
  setenv BOOT_DEV "mmc 0:3"
elif test "${raucslot}" = "B"; then
  setenv BOOT_DEV "mmc 0:5"
fi
fatload mmc 0:1 ${kernel_addr_r} zImage
fatload mmc 0:1 ${fdt_addr} bcm2711-rpi-4-b.dtb
bootz ${kernel_addr_r} - ${fdt_addr}
