import subprocess, os

class arch_auto():
    def packages_installer():
        subprocess.run(['sudo', 'bash', '-c','pacman -Syyyuu --needed base-devel git xorg-fonts-misc dmenu rofi firefox vlc code blender virtualbox pcmanfm git alacritty xorg xorg-xinit bluez bluez-utils lxappearance ranger htop brightnessctl xfce4-power-manager i3'])
        subprocess.run(['bash', '-c','git clone https://aur.archlinux.org/yay.git'])
        subprocess.run(['bash', '-c', 'yay -S siji-git ttf-unifont picom-git polybar-git python-pip zsh'])
        subprocess.run('bash', '-c', 'pip install pandas numpy selenium kivy flask GitPython')
        subprocess.run(['sudo', 'bash', '-c','pacman -Syyyuu'])
        subprocess.run(['bash', '-c', 'sh -c "$(wget -O- https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"'])
        subprocess.run(['bash', '-c', 'chsh -s $(which zsh)'])
        


    def files_setup():
        os.chidr('~/i3wm')
        subprocess.run(['bash', '-c', 'cp -r alacritty i3 picom rofi polybar ~/.config'])
        subprocess.run(['bash', '-c', 'cp -r .vimrc .zshrc .zsh .vim .oh-my-zsh ~/'])
        subprocess.run(['bash', '-c', 'cp -r kU6QGsW.jpeg ~/Pictures']) 
        subprocess.run(['bash', '-c', 'reboot'])

def main():
    arch_auto.packages_installer()
    arch_auto.files_setup()

if __name__ == '__main__':
        main()

