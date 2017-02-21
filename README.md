# OCI Cloud Object Storage Library
Contains the Python library for cloud object storage

*Configuration*

The configuration file "config.txt" must be created in the configuration directory.  Below is the format:

```
[GlobalInformation]
cloudSelect = Can be either aws or chameleon
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

```

Note:  Chameleon and AWS configuration parameters are only needed based on the cloudSelect parameter i.e. if you have "cloudSelect = chameleon", all AWS parameters may be omitted and vice versa.

*Usage*

import cloudStorage

putObject(objectData)

Returns the response if using chameleon cloud e.x. 201 if object was created successfully.

The included test.py file shows a simple use case for the putObject function.
