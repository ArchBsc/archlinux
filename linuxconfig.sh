#!/bin/bash

## packages_installer

sudo pacman -Syyyuu --needed base-devel git xorg-fonts-misc dmenu rofi firefox vlccode blender virtualbox pcmanfm git alacritty xorg xorg-xinit bluez bluez-utils lxappearance ranger htop brightnessctl xfce4-power-manager i3

git clone https://aur.archlinux.org/yay.git
cd yay
makepkg -si

git clone https://github.com/ArchBsc/i3wm.git

yay -S siji-git ttf-unifont picom-git polybar-git python-pip zsh
pip install pandas numpy selenium kivy flask GitPython

sudo pacman -Syyyuu
sh -c "$(wget -O- https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
chsh -s $(which zsh)


## files setup 

cd /home/arch/i3wm

git checkout main2
cp -r alacritty i3 picom rofi polybar /home/arch/.config
cp -r .vimrc .zshrc .zsh .vim .oh-my-zsh /home/arch
cp -r kU6QGsW.jpeg /home/arch/Pictures
echo "Finished!!"
systemctl reboot







