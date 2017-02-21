import boto3


def putObject(resource, awsBucketName, fileName, objectData):
    s3 = resource

    s3.Bucket(awsBucketName).put_object(Key=fileName, Body=objectData)
    return 0
