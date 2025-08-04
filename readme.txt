Reminder:
Please review the functions "f5()" and "changeTab()" because different OSs or browsers may have different shortcuts
Please input the information of your smtp server or discord

This bot is to regularly detect "attack" in Travian and notify yourself via email or discord.

After install all depended libraries, you can run the script below to start:
python3 scan_attack_bot.py

You can also run it on a cloud VM (Linux) so that it doesn't bother your PC.
Roughly, the following command may remind you what to install.

<Remote Desktop>
sudo apt-get update
sudo apt-get install --no-install-recommends ubuntu-desktop
sudo apt-get install gnome-core
sudo reboot now -h
sudo apt install xrdp -y
sudo passwd root

<Enable root login>
https://askubuntu.com/questions/1192471/login-as-root-on-ubuntu-desktop

<Python>
sudo apt install vim
sudo apt install python3-venv
python3 -m venv vvv
source vvv/bin/activate     !!! need this step after reboot
pip install pyautogui xxx yyy zzz
python3 scan_attack_bot.py

Use RDP client to connect your cloud VM e.g. Windows App, Remote desktop

Future: this kind of notification bot could be applied to different games or areas.
Hope this app inspired you something~
Thank you~
