sudo cp /etc/xrdp/xrdp.ini /etc/xrdp/xrdp.ini.bak;
sudo sed -i 's/3389/3390/g' /etc/xrdp/xrdp.ini;
sudo sed -i 's/max_bpp=32/#max_bpp=32\nmax_bpp=128/g' /etc/xrdp/xrdp.ini;
sudo sed -i 's/xserverbpp=24/#xserverbpp=24\nxserverbpp=128/g' /etc/xrdp/xrdp.ini;
echo xfce4-session > ~/.xsession;
