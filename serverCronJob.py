import init
import mailManager
import networkManager
import networkManagerFirebasePlugin
import threading
import nginxManager

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
        print("your backend IP has updated.", ip)
        nginxManager.restartNginx()
    return needUpdate

networkManagerFirebasePlugin.initApp()
UpdateIP()

