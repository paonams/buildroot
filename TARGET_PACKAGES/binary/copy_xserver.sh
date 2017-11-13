SOURCE=/home/sanjit/Documents/workArea/LINUXCNC/DISPLAY/SERVER_X/MIRROR_XSERVER
TARGET=xserver
mkdir -p $TARGET/drivers/

cp $SOURCE/hw/xfree86/fbdevhw/.libs/libfbdevhw.so $TARGET
cp $SOURCE/hw/xfree86/vgahw/.libs/libvgahw.so $TARGET
cp $SOURCE/hw/xfree86/vbe/.libs/libvbe.so $TARGET
cp $SOURCE/hw/xfree86/shadowfb/.libs/libshadowfb.so $TARGET
cp $SOURCE/hw/xfree86/int10/.libs/libint10.so $TARGET
cp $SOURCE/hw/xfree86/drivers/modesetting/.libs/modesetting_drv.so $TARGET/drivers/
cp $SOURCE/hw/xfree86/exa/.libs/libexa.so $TARGET
cp $SOURCE/hw/xfree86/dixmods/.libs/libfb.so $TARGET
cp $SOURCE/hw/xfree86/dixmods/.libs/libwfb.so $TARGET
cp $SOURCE/hw/xfree86/dixmods/.libs/libshadow.so $TARGET




