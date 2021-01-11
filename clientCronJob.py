import init
import mailManager
import networkManager
import networkManagerFirebasePlugin
import threading
ip=''

def UpdateIP(ip):
    current_ip=networkManager.getMyIP()
    needUpdate = ~(ip == current_ip)
    if ~needUpdate:
        print('your ip hasn\'t changed:', ip)
    else:
        config = init.config
        email = config['email']
        ip = current_ip
        mailManager.sendEmail(email, email, "your IP has updated.", ip)
        networkManagerFirebasePlugin.updateIP()
        print("your IP has updated.", ip)
    return needUpdate

networkManagerFirebasePlugin.initApp()
print("Current Time: ", init.logManager.getTimestamp())   
UpdateIP(ip)
