sudo apt-get update
sudo apt-get -y upgrade

sudo apt-get -y install pip

sudo apt -y install python3-flask

sudo apt -y install python3-full


pip install w1thermsensor --break-system-packages


echo "dtoverlay=w1-gpio" >> /boot/firmware/config.txt # Rankiniu budu reikia padaryti

# Viskas susirase, turbut GPIO reikia dar surasyti

# Sukurti servisu scriptus,, kurie sukuria servisus ir peleidzia juos