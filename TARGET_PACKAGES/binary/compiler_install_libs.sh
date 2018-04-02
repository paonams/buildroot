TARGET=/opt/ARM/buildroot/output/host/usr/arm-buildroot-linux-gnueabihf/sysroot

cd $TARGET/usr/lib
rm libEGL* libGLE* libOpenC* libmali.so
cd -
pwd
cp -aRP x11/* $TARGET/usr/lib

cp armsoc_drv.so $TARGET/usr/lib/xorg/modules/drivers
#cp -r boot $TARGET
#cp setip.sh $TARGET/etc

cd 5422_platform
cp xorg.conf $TARGET/etc/X11/xorg.conf
cp 10-odroid.rules $TARGET/etc/udev/rules.d
cp blacklist-odroid.conf $TARGET/etc/modules-load.d
cp asound.conf $TARGET/etc
cd -

#cd $TARGET/usr/lib/xorg/modules/drivers/
#rm cirrus_* vesa_drv.so
#cd -

#mkdir -p $TARGET/etc/mlabs
#cp mount.sh $TARGET/etc
cp -r xserver/* $TARGET/usr/lib/xorg/modules

cp bin_xserver/* $TARGET/bin/
cp bin_xserver/* $TARGET/usr/bin/

