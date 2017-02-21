import configuration.globalVars as globalVars
import chameleon.chameleonAuth as chameleonAuth
import chameleon.chameleonObjectStorage as chameleonObjectStorage
import aws.awsAuth as awsAuth
import aws.awsObjectStorage as awsObjectStorage
import datetime
import time

# These functions allow for multi-cloud support by allowing single function calls for shared cloud commands


# Boots a VM, cloud used is dependent on the request
def putObject(objectData):
   globalVars.init()
   ts = time.time()
   fileName = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')

   # Chameleon Cloud Object Storage
   if (globalVars.cloudSelect == "chameleon"):
       my_token_id = chameleonAuth.auth()
       status = chameleonObjectStorage.putObject(my_token_id, fileName, objectData)
       return status


   # AWS Object Storage
   if (globalVars.cloudSelect == "aws"):
       resource = awsAuth.authResource(globalVars.awsAccess,
                                       globalVars.awsSecret, 
			               globalVars.awsRegion)
       status = awsObjectStorage.putObject(resource, globalVars.awsBucketName, fileName, objectData)
       return status
