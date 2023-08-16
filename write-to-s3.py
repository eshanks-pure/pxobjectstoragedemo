#!/usr/bin/env python
import os, time, datetime, boto3
from random import randint

S3_ACCESS_KEY = os.environ['S3_ACCESS_KEY']
S3_SECRET_KEY = os.environ['S3_SECRET_KEY']
S3_BUCKET_NAME = os.environ['S3_BUCKET_NAME']
S3_ENDPOINT = os.environ['S3_ENDPOINT']
S3_REGION = os.environ['S3_REGION']

#Creating Session With Boto3.

session = boto3.Session(
aws_access_key_id=S3_ACCESS_KEY,
aws_secret_access_key=S3_SECRET_KEY
)
#Creating S3 Resource From the Session.
for i in range(1, 50):
    s3 = session.resource('s3')
    object = s3.Object(S3_BUCKET_NAME, str(datetime.datetime.now()))
    txt_data = b'This is the content of the file uploaded from python boto3'
    result = object.put(Body=txt_data)
    res = result.get('ResponseMetadata')
    if res.get('HTTPStatusCode') == 200:
        print('New File Uploaded Successfully', flush=True)
    else:
        print('File Upload Failed', flush=True)
    #Wait a random amount of time before trying again
    delay = randint(1,5)
    time.sleep(delay)
