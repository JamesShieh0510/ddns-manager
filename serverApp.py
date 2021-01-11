import init
import mailManager
import networkManager
import networkManagerFirebasePlugin
import threading
import nginxManager
secs=600.0

def UpdateIP():
    k8s_api_server_port = "8080"
    needUpdate = nginxManager.updateIPOfBackendService(k8s_api_server_port)
    if not needUpdate:
        print('your nginx config hasn\'t changed:')
    else:
        ip = networkManagerFirebasePlugin.getIPfromFirebase()
        config = init.config
        email = config['email']
        mailManager.sendEmail(email, email, "your backend IP has updated.", ip)
        threading.Timer(secs, loop, [secs]).start()
        print("your backend IP has updated.", ip)
        nginxManager.restartNginx()
    return needUpdate

def loop(secs):
    print("Current Time: ", init.logManager.getTimestamp())   
    ip = networkManagerFirebasePlugin.getIPfromFirebase()
    UpdateIP()

networkManagerFirebasePlugin.initApp()
loop(secs)