import ConfigParser
import os


def init():
    get_config()

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


def get_config():
    global config
    config = ConfigParser.RawConfigParser()
    package_directory = os.path.dirname(os.path.abspath(__file__))
    config.read(os.path.join(package_directory, 'config.txt'))
