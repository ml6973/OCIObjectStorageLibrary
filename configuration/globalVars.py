import ConfigParser
import os


def init():
    get_config()

    global uploadSize
    uploadSize = int(config.get('GlobalInformation', 'uploadSize'))
    uploadSize = uploadSize * 1024 * 1024

    global bufferSize
    bufferSize = int(config.get('GlobalInformation', 'bufferSize'))
    bufferSize = bufferSize * 1024 * 1024
    bufferSize = min(bufferSize, uploadSize)

    global chameleon_tenant_id
    chameleon_tenant_id = ""

    global cloudSelect
    cloudSelect = config.get('GlobalInformation', 'cloudSelect')

    global chameleonAuthURL
    try:
        chameleonAuthURL = config.get('GlobalInformation', 'chameleonAuthURL')
    except ConfigParser.NoOptionError:
        if (cloudSelect != "chameleon"):
	    pass
    
    global chameleonObjectStorageURL
    try:
        chameleonObjectStorageURL = config.get('GlobalInformation', 'chameleonObjectStorageURL')
    except ConfigParser.NoOptionError:
        if (cloudSelect != "chameleon"):
	    pass

    global chameleonTenantName
    try:
        chameleonTenantName = config.get('GlobalInformation', 'chameleonTenantName')
    except ConfigParser.NoOptionError:
        if (cloudSelect != "chameleon"):
	    pass

    global chameleonContainerName
    try:
        chameleonContainerName = config.get('GlobalInformation', 'chameleonContainerName')
    except ConfigParser.NoOptionError:
        if (cloudSelect != "chameleon"):
	    pass

    global chameleonCloudUsername
    try:
        chameleonCloudUsername = config.get('GlobalInformation', 'chameleonCloudUsername')
    except ConfigParser.NoOptionError:
        if (cloudSelect != "chameleon"):
	    pass

    global chameleonCloudPassword
    try:
        chameleonCloudPassword = config.get('GlobalInformation', 'chameleonCloudPassword')
    except ConfigParser.NoOptionError:
        if (cloudSelect != "chameleon"):
	    pass

    global awsAccess
    try:
         awsAccess = config.get('GlobalInformation', 'awsAccess')
    except ConfigParser.NoOptionError:
         if (cloudSelect != "aws"):
	     pass

    global awsSecret
    try:
         awsSecret = config.get('GlobalInformation', 'awsSecret')
    except ConfigParser.NoOptionError:
        if (cloudSelect != "aws"):
	    pass
    global awsRegion
    try:
        awsRegion = config.get('GlobalInformation', 'awsRegion')
    except ConfigParser.NoOptionError:
        if (cloudSelect != "aws"):
	    pass

    global awsBucketName
    try:
        awsBucketName = config.get('GlobalInformation', 'awsBucketName')
    except ConfigParser.NoOptionError:
	if (cloudSelect != "aws"):
	    pass

    global jetstreamAuthURL
    try:
        jetstreamAuthURL = config.get('GlobalInformation', 'jetstreamAuthURL')
    except ConfigParser.NoOptionError:
        if (cloudSelect != "jetstream"):
	    pass
    
    global jetstreamObjectStorageURL
    try:
        jetstreamObjectStorageURL = config.get('GlobalInformation', 'jetstreamObjectStorageURL')
    except ConfigParser.NoOptionError:
        if (cloudSelect != "jetstream"):
	    pass

    global jetstreamTenantID
    try:
        jetstreamTenantID = config.get('GlobalInformation', 'jetstreamTenantID')
    except ConfigParser.NoOptionError:
        if (cloudSelect != "jetstream"):
	    pass

    global jetstreamContainerName
    try:
        jetstreamContainerName = config.get('GlobalInformation', 'jetstreamContainerName')
    except ConfigParser.NoOptionError:
        if (cloudSelect != "jetstream"):
	    pass

    global jetstreamCloudUsername
    try:
        jetstreamCloudUsername = config.get('GlobalInformation', 'jetstreamCloudUsername')
    except ConfigParser.NoOptionError:
        if (cloudSelect != "jetstream"):
	    pass

    global jetstreamCloudPassword
    try:
        jetstreamCloudPassword = config.get('GlobalInformation', 'jetstreamCloudPassword')
    except ConfigParser.NoOptionError:
        if (cloudSelect != "jetstream"):
	    pass



def get_config():
    global config
    config = ConfigParser.RawConfigParser()
    package_directory = os.path.dirname(os.path.abspath(__file__))
    config.read(os.path.join(package_directory, 'config.txt'))
