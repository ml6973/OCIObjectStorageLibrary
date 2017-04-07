# OCI Cloud Object Storage Library
Contains the Python library for cloud object storage

## Configuration

The configuration file "config.txt" must be created in the configuration directory.  Below is the format:

```
[GlobalInformation]
cloudSelect = Can be either aws or chameleon
uploadSize = The max size in Megabytes of each chunk of the file being uploaded
bufferSize = The max size in Megabytes of memory to allocate to the streaming buffer
chameleonAuthURL = Use the appropriate authentication (identity) endpoint
chameleonObjectStorageURL = Use the appropriate object storage endpoint
chameleonTenantName = Use the appropriate tenant name
chameleonContainerName = Use the appropriate container name
chameleonCloudUsername = Username to authenticate with chameleon cloud
chameleonCloudPassword = Password to authenticate with chameleon cloud
awsAccess = aws Access Key for authentication
awsSecret = aws Secret Key for authentication
awsRegion = Use the appropriate region for authentication and storage
awsBucketName = Use the appropriate bucket name for storage
jetstreamAuthURL = Use the appropriate authentication (identity) endpoint
jetstreamObjectStorageURL = Use the appropriate object storage endpoint
jetstreamTenantID = Use the appropriate Tenant ID (not name)
jetstreamContainerName = Use the appropriate container name
jetstreamCloudUsername = Username to authenticate with chameleon cloud
jetstreamCloudPassword = Password to authenticate with chameleon cloud

```

Note:  Cloud specific configuration parameters are only needed based on the cloudSelect parameter i.e. if you have "cloudSelect = chameleon", all other cloud parameters such as AWS will be omitted and vice versa.

## Usage
Ensure the object you are passing is a "file-like" class.
The path parameter is optional, use it to specific the pseudo directory within the container the file will be uploaded to

```
import cloudStorage

putObject(objectData, path)
```

The included test.py file shows a simple use case for the putObject function.
