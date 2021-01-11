import init
import mailManager
import networkManager
import networkManagerFirebasePlugin
import threading
import nginxManager
secs=600.0
ip=''

def UpdateIP(ip):
    k8s_api_server_port = "8080"
    needUpdate = nginxManager.updateIPOfBackendService(k8s_api_server_port)
    if ~needUpdate:
        print('your ip hasn\'t changed:', ip)
    else:
        config = init.config
        email = config['email']
        ip = current_ip
        mailManager.sendEmail(email, email, "your backend IP has updated.", ip)
        networkManagerFirebasePlugin.updateIP()
        threading.Timer(secs, loop, [secs, ip]).start()
        print("your backend IP has updated.", ip)
        nginxManager.restartNginx()
    return needUpdate

def loop(secs, ip):
    print("Current Time: ", init.logManager.getTimestamp())   
    ip = networkManagerFirebasePlugin.getIPfromFirebase()
    UpdateIP(ip)

networkManagerFirebasePlugin.initApp()
loop(secs, ip)