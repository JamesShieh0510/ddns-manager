su root
sudo apt install python
sudo apt install python-pip
sudo pip install requests
pip install firebase_admin
export python_user=$(whoami)


mkdir /root/ddns-manager
cp ./* /root/ddns-manager/
echo "@reboot     root    cd /root/ddns-manager/;python clientCronJob.py" >> /etc/crontab
echo "*/5 * * * *     root    cd /root/ddns-manager/;python clientCronJob.py" >> /etc/crontab
