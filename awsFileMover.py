import boto3
import os
import sys


session = boto3.Session(profile_name='default')
#client = session.client('s3',
#                        aws_access_key_id=os.environ.get('KEY'),
#                        aws_secret_access_key=os.environ.get('SECRET'))
s3Resource = boto3.resource('s3')
firstBucketName = sys.argv[1]
secondBucketName = sys.argv[2]
threshold = sys.argv[3]
firstFileName = 'abc.txt'



#Get keys of objects in firstBucketName that are larger than 50MBself.
#def findLarge():
#    largeFiles = []
#    for key in value:
#        if value: u'Size' >= 50000000
#            add to largeFiles



def moveLarge(bucketFromName, bucketToName, fileName):
    copySource = {
        'Bucket': bucketFromName,
        'Key': fileName
    }
    s3Resource.Object(bucketToName, fileName).copy(copySource)

moveLarge(firstBucketName, secondBucketName, firstFileName)
