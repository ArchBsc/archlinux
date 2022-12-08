# Archlinux (command)

## wifi
```
iwctl
station wlan0 get-networks
station wlan0 connect
```
## Partition 
To partition the disk:
boot: ```/dev/sda1``` 512M
home: ```/dev/sda2``` (the rest of the disk)

```
cfdisk /dev/sda
mkfs.fat -F32 /dev/sda1
mkfs.ext4 /dev/sda2
```
## Mount
```
mount /dev/sda2 /mnt
mount --mkdir /dev/sda1 /boot/efi
```

## Install the system
```
pacstrap -i /mnt base linux linux-firmware sudo vim
genfstab -U -p /mnt >> /mnt/etc/fstab
```
Switch to root
```
arch-chroot /mnt /bin/bash
```
## Set locale
```
vim /etc/locale.gen (en_US.UTF-8)
locale-gen
echo "LANG=en_US.UTF-8" > /etc/locale.conf
```

## Set the time zone
```
ln -sf /usr/share/zoneinfo/Europe/Athens /etc/localtime
hwclock --systohc --utc
```

## Set hostname
```
echo arch > /etc/hostname
vim /etc/hosts
```
And add this:
(127.0.0.1        localhost
::1              localhost
127.0.1.1        arch)

## Enable network
```
pacman -S networkmanager
systemctl enable NetworkManager
passwd
```

## Install GRUB
```
pacman -S grub efibootmgr
grub-install --target=x86_64-efi --bootloader-id=GRUB --efi-directory=/boot/efi --removable
grub-mkconfig -o /boot/grub/grub.cfg
pacman -S grub
grub-install /dev/sda
grub-mkconfig -o /boot/grub/grub.cfg
```

## Finish 
```
exit
umount -R /mnt
reboot
```

(boot again)

## Swap File
```
dd if=/dev/zero of=/swapfile bs=1M count=3072 status=progress
chmod 0600 /swapfile
mkswap -U clear /swapfile
swapon /swapfile
echo '/swapfile none swap defaults 0 0' >> /etc/fstab
free -m (to check if swapfile work)
```

## Add user

```
useradd -m -g users -G wheel -s /bin/bash username
passwd username
EDITOR=nano visudo (Uncomment this: %wheel ALL=(ALL) ALL)
```

## Install window system and audio

```
sudo pacman -S pulseaudio pulseaudio-alsa xorg xorg-xinit xorg-serverpacman -S pulseaudio pulseaudio-alsa xorg xorg-xinit xorg-server
sudo pacman -S i3 rxvt-unicode dmenu lightdm lightdm-gtk-greeter
systemctl enable lightdm
echo "exec i3"  > ~/.xinitrc
```
Move to gui ```startx```
