sudo apt install python
sudo apt install python-pip
sudo pip install requests
pip install firebase_admin
export python_user=$(whoami)
echo 'service nginx restart' > /home/$python_user/restart-nginx-service.sh
sudo chown root:root /home/$python_user/restart-nginx-service.sh
sudo chmod 700 /home/$python_user/restart-nginx-service.sh
su root
sudo echo "$python_user  ALL=(ALL) NOPASSWD: /restart-nginx-service.sh" >> /etc/sudoers