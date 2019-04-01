import boto3

session = boto3.Session(profile_name='default')
s3Resource = boto3.resource('s3')
firstBucketName = 'cramerbucket1'
secondBucketName = 'cramerbucket2'
#firstFileName = 'abc.txt'

#Get keys of objects in firstBucketName that are larger than 50MBself.
def findLarge():
    largeFiles = []
    for key in value:
        if value: u'Size' >= 50000000
            add to largeFiles



def moveLarge(bucketFromName, bucketToName, fileName):
    copySource = {
        'Bucket': bucketFromName,
        'Key': fileName
    }
    s3Resource.Object(bucketToName, fileName).copy(copySource)

moveLarge(firstBucketName, secondBucketName, largeFiles)
