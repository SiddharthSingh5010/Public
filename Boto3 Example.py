import boto3
import botocore
from botocore.retries import bucket

BUCKET_NAME = 'siddharthbucket501' # replace with your bucket name
s3 = boto3.resource('s3')

def downloadfile(bucketname,filename,destfilename):
    try:
        s3.Bucket(bucketname).download_file(filename, destfilename)
    except botocore.exceptions.ClientError as e:
        if e.response['Error']['Code'] == "404":
            print("The File {} does not exist.".format(filename))
        else:
            raise
def uploadfile(bucketname,filename):
    try:
        data = open(filename, 'rb')
        s3.Bucket(bucketname).put_object(Key=filename, Body=data)
    except botocore.exceptions.ClientError as e:
            raise

def listbucket():
    li=[]
    for bucket in s3.buckets.all():
        li.append(bucket.name)
    return li

def getfilenames(bucketname):
    li=[]
    bucket = s3.Bucket(bucketname)
    for obj in bucket.objects.all():
        li.append(obj.key)
    return li

uploadfile(BUCKET_NAME,'Python Data Engineer.pdf')
print(getfilenames(BUCKET_NAME))
