sudo apt install python
sudo apt install python-pip
sudo pip install requests
pip install firebase_admin
export python_user=$(whoami)
echo 'sudo service nginx restart' > /home/$python_user/restart-nginx-service.sh
sudo chown root:root /home/$python_user/restart-nginx-service.sh
sudo chmod 705 /home/$python_user/restart-nginx-service.sh

nginx_config=$(cat config.json | grep nginx_config_file | awk '{print $2}' | sed -e "s/[,\"]//g")
export nginx_config_path=$nginx_config
sudo chown root:root $nginx_config
sudo chmod 707 $nginx_config
su root
sudo pip install requests
pip install firebase_admin
sudo echo "$python_user  ALL=(ALL) NOPASSWD: /home/$python_user/restart-nginx-service.sh" >> /etc/sudoers
sudo echo "$python_user  ALL=(ALL) NOPASSWD: $nginx_config_path" >> /etc/sudoers

mkdir /root/ddns-manager
cp ./* /root/ddns-manager/
echo "@reboot     root    cd /root/ddns-manager/;python serverCronJob.py" >> /etc/crontab
echo "*/5 * * * *     root    cd /root/ddns-manager/;python serverCronJob.py" >> /etc/crontab
