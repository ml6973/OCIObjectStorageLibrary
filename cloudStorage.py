import configuration.globalVars as globalVars
import chameleon.chameleonObjectStorage as chameleonObjectStorage
import aws.awsAuth as awsAuth
import aws.awsObjectStorage as awsObjectStorage
import jetstream.jetObjectStorage as jetObjectStorage
import datetime
import time

# These functions allow for multi-cloud support by allowing single function calls for shared cloud commands


# Boots a VM, cloud used is dependent on the request
def putObject(objectData, path=""):
   globalVars.init()
   if not path == "":
      path = path.lstrip("/")
      path = path.rstrip("/")
      path = "/" + path + "/"
   else:
      path = "/"
   ts = time.time()
   fileName = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')

   # Chameleon Cloud Object Storage
   if (globalVars.cloudSelect == "chameleon"):
       status = chameleonObjectStorage.putObject(fileName, path, objectData)
       return status


   # AWS Object Storage
   if (globalVars.cloudSelect == "aws"):
       resource = awsAuth.authResource(globalVars.awsAccess,
                                       globalVars.awsSecret, 
			               globalVars.awsRegion)
       status = awsObjectStorage.putObject(resource, globalVars.awsBucketName, fileName, objectData)
       return status

   # Jetstream Cloud Object Storage
   if (globalVars.cloudSelect == "jetstream"):
       status = jetObjectStorage.putObject(fileName, path, objectData)
       return status
