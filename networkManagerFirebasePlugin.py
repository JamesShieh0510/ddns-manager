import init
import networkManager
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
#Create a JSON file called ./config.json and add the following json keys and values
#Tips: you can create a credential file from the URL :https://console.firebase.google.com/project/<your project name>/settings/serviceaccounts/adminsdk
# {
    # "service_account_key_file": "the credential file path and name"
# }
#
# Initialize the app with a service account, granting admin privileges
def initApp():
    global db
    cred = createCred()
    firebase_admin.initialize_app(cred)
    db = firestore.client()
    getDocument(u'ip-proxy', u'ip-record')
# Use a service account
def createCred():
    config = init.config
    cred = credentials.Certificate(config['service_account_key_file'])
    return cred
def getDocument(collection, document):
    global doc_ref
    doc_ref = db.collection(collection).document(document)

def updateIP():
    ip = networkManager.getMyIP()
    doc_ref.set({                   
        u'ip': ip,
    })
def getIPfromFirebase():
    doc = doc_ref.get({'ip'})
    ip = doc.to_dict()['ip']
    print('get IP from firebase:', ip)
    return ip
