#!/usr/bin/env python

import boto3
from boto.s3.connection import S3Connection
import sys


session = boto3.Session(profile_name='default')

s3 = boto3.resource('s3')
s3client = boto3.client('s3')
firstBucketName = sys.argv[1]
bucket = firstBucketName
secondBucketName = sys.argv[2]
threshold = sys.argv[3]
firstFileName = 'abc.txt'

keys = []
def findLarge(bucket):

    resp = s3client.list_objects_v2(Bucket=bucket)
    for key in resp['Contents']:
        if key['Size'] >= int(threshold):
            keys.append(key['Key'])
    return keys


def moveLarge(bucketFromName, bucketToName, fileName):
    copySource = {
        'Bucket': bucketFromName,
        'Key': fileName
    }
    s3.Object(bucketToName, fileName).copy(copySource)

findLarge(bucket)

for key in keys:
    moveLarge(firstBucketName, secondBucketName, key)
