sudo apt update
sudo apt install python3 python3-pip -y
pip3 install undetected-chromedriver selenium
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo dpkg -i google-chrome-stable_current_amd64.deb
sudo apt --fix-broken install -y
wget https://chromedriver.storage.googleapis.com/chromedriver_linux64.zip
unzip chromedriver_linux64.zip
sudo mv chromedriver /usr/local/bin/

install screen
apt install screen
screen -S ocean

Jalankan Script 
ls
cd ocean
ls
python3 script.py
