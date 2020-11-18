import subprocess
import os
import shlex
import boto3
import json
import datetime
import pandas as pd
import time
from subprocess import check_call
from prettytable import PrettyTable
import boto3
from botocore.exceptions import ClientError


def create_bucket(bucket_name, region=None):

    try:
        if region is None:
            s3_client = boto3.client('s3')
            s3_client.create_bucket(Bucket=bucket_name)
        else:
            s3_client = boto3.client('s3', region_name=region)
            location = {'LocationConstraint': region}
            s3_client.create_bucket(Bucket=bucket_name,
                                    CreateBucketConfiguration=location)
    except ClientError as e:
        return False, e
    return True, ''

def delete_bucket(bucket_name):
    s3_client = boto3.client('s3')
    s3_client.delete_bucket(Bucket=bucket_name,)

def list_buckets():
    s3 = boto3.client('s3')
    response = s3.list_buckets()
    return response

def upload_file(file_name, bucket, object_name, public):
    s3_client = boto3.client('s3')
    args = {}
    if public:
        args["ExtraArgs"] = {'ACL': 'public-read'}
        
    try:
        response = s3_client.upload_file(file_name, bucket, object_name, **args)
        return True, response
    except ClientError as e:
        return False, e

def download_file(bucket, obj, path):
    s3 = boto3.client('s3')
    s3.download_file(bucket, obj, path)

def list_files(bucket):
    s3 = boto3.client('s3')
    response = s3.list_objects_v2(
        Bucket=bucket,
    )
    return response

def delete_file(bucket, obj):
    s3 = boto3.client('s3')
    response = s3.delete_objects(
        Bucket=bucket,
        Delete={
            'Objects': [
                {
                    'Key': obj
                },
            ],
        }
    )
    return response

