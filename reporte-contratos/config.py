import os
import json

from azure.keyvault.secrets import SecretClient
from azure.identity import DefaultAzureCredential

try:
    production_env = False #False para local, True para cloud
    test = os.environ['KEY_VAULT']
except:
    production_env = False
    f = open('devkeys.json')
    keys = json.load(f)
    f.close()

def getConfigValue(Key: str, isSecret: bool = False):
    """Returns a config Value, designed for secrets and notSecrets
    sample: getConfigValue('RequiredKey', True)"""

    if production_env:
        if isSecret:
            response = client.get_secret(Key).value
        else:
            response = os.environ[Key]
    else:
        if isSecret:
            response = keys["secrets"][Key]
        else:
            response = keys["environment"][Key]
    return response

##############################################
# KeyVault Config ############################
##############################################
keyVaultName = getConfigValue('KEY_VAULT')
KVUri = f"https://{keyVaultName}.vault.azure.net"
credential = DefaultAzureCredential()
client = SecretClient(vault_url=KVUri, credential=credential)
##############################################
##############################################


class BaseConfig(object):
    """Contains the information related to PowerBI Embedded"""
    #Variables
    SESSION_TYPE = getConfigValue('SESSION_TYPE') #Session type of flask https://flask-session.readthedocs.io/en/latest/

    #Secrets
    SECRET_KEY = getConfigValue('secretkeyflask', True) # Flask APP Secret
