import boto3

def authResource(ACCESS_KEY,SECRET_KEY,REGION):
    resource = boto3.resource('s3',
                              aws_access_key_id=ACCESS_KEY,
			      aws_secret_access_key=SECRET_KEY,
			      region_name=REGION)
    return resource
