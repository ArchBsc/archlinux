#   from selenium import webdriver
import time, os, shutil, git
# Packages for git clone: GitPython

# path = "/home/arch/Documents/GitHub/archlinux/chrome-driver/chromedriver"
# driver = webdriver.Chrome(path)
class arch_auto():
    def packages_installer():
        os.system("sudo pacman -Syyuu")
        os.system("sudo pacman -S xorg-fonts-misc dmenu rofi firefox vlc code blender virtualbox pcmanfm git alacritty")
        os.system("sudo yay -S picom-git github-desktop google-chrome polybar-git stgithub-degithub-degithub-desktopsktopsktopremio python-pip zsh")
        os.system("pip install pandas numpy selenium kivy flask GitPython")
        git.Git("~/").clone("https://github.com/llalex25ll/config_archlinux_i3wm.git")
        os.system("sudo pacman -Syyuu")
        print("Things i need to download manually:\n    siji-git\n    ttf-unifont")
        time.sleep(5)

    def files_setup():
        os.chdir("~/config_archlinux_i3wm/")
        shutil.copy("i3", "~/.config/")
        shutil.copy("alacritty.yml", "~/.config/")
        shutil.copy("picom", "~/.config/")
        shutil.copy("polybar", "~/.config/")
        shutil.copy("alacritty", "~/.config/")
        os.makedirs("~/Pictures/wallpaper/")
        shutil.copy("kU6QGsW.jpeg", "~/Pictures/wallpaper/")
        time.sleep(4)
        os.system("reboot")

def main():
    arch_auto.packages_installer()
    arch_auto.files_setup()

if __name__ == '__main__':
    main()
