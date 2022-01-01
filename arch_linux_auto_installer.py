# from selenium import webdriver
import time 
import os 

# path = "/home/arch/Documents/GitHub/archlinux/chrome-driver/chromedriver"
# driver = webdriver.Chrome(path)


os.system("sudo pacman -Syyuu")
os.system("sudo pacman -S xorg-fonts-misc dmenu rofi firefox vlc code blender virtualbox pcmanfm git alacritty")
os.system("yay -S picom-git github-desktop polybar-git stgithub-degithub-degithub-desktopsktopsktopremio python-pip zsh")
os.system("pip install pandas numpy selenium kivy flask")
os.system("git clone https://github.com/llalex25ll/config_archlinux_i3wm.git")
os.system("cd config_archlinux_i3wm/")
os.system("cp i3 ~/,config/")
os.system("cp alacritty.yml ~/.config/")
os.system("cp picom ~/.config/")
os.system("cp polybar ~/.config/")
os.system("cp alacritty ~/.config/")
time.sleep(4)
print("Things i need to download manually:\n    siji-git\n    ttf-unifont")