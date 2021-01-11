import init
import networkManager
import networkManagerFirebasePlugin
import re
import subprocess
#Create a JSON file called ./config.json and add the following json keys and values
#Tips: you can create a credential file from the URL :https://console.firebase.google.com/project/<your project name>/settings/serviceaccounts/adminsdk
# {
    # "nginx_config_file": "./test-file"
    # "upstream": "edge01_backend"
# }
#
# restart nginx service
def restartNginx():
    config = init.config
    sh_file = '/home/'+config['python_user']+'/restart-nginx-service.sh'
    subprocess.call(['sh', sh_file])


def updateIPOfBackendService(port):
    config = init.config
    ip = networkManagerFirebasePlugin.getIPfromFirebase()
    with open(config['nginx_config_file']) as configFile:
        rawText = configFile.read()
        hasChanged = rawText.find(ip) == -1 # return -1 if they are different.
        if hasChanged:
            print("the IP has changed.")
            target = 'upstream '+config['upstream']+' {[\n_a-zA-Z_0-9-.:;# ]*\n}'
            result = 'upstream '+config['upstream']+' {\n    server '+ip+':'+port+';\n}'
            updatedText = re.sub(target, result, rawText)
            print('relace test:', updatedText)
            configFile.close()
            fp = open(config['nginx_config_file'],'w')
            fp.write(updatedText)
            fp.close
        else:
            print("the IP hasn't changed.")
        return hasChanged

