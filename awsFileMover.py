import boto3

session = boto3.Session(profile_name='default')
s3Resource = boto3.resource('s3')
firstBucketName = 'cramerbucket1'
secondBucketName = 'cramerbucket2'
firstFileName = 'abc.txt'



def moveLarge(bucketFromName, bucketToName, fileName):
    copySource = {
        'Bucket': bucketFromName,
        'Key': fileName
    }
    s3Resource.Object(bucketToName, fileName).copy(copySource)

moveLarge(firstBucketName, secondBucketName, firstFileName)
