import subprocess
import os
import shlex
import boto3
import json
import datetime
import pandas as pd
import time
from subprocess import check_call

ec2_resource = boto3.resource('ec2')
ec2_client = boto3.client('ec2')

def list_azs():
    response = ec2_client.describe_availability_zones()
    azs = [response['AvailabilityZones'][i]['ZoneName'] for i in range(len(response['AvailabilityZones']))]
    return azs

def create_volume(az, size, vt='gp2', name='auto', ssid=""):
    args = {
        "AvailabilityZone": az,
        "Size": size,
        "VolumeType": vt,
        "TagSpecifications": [
            {
                'ResourceType': 'volume',
                'Tags': [
                    {
                        'Key': 'Name',
                        'Value': name,
                    },
                ],
            },
        ],
    }

    if ssid :
        args["SnapshotId"] = ssid

    response = ec2_client.create_volume(**args)
    return response

def attach_volume(vol_id, instance_id, device_name):
    response = ec2_client.attach_volume(
        Device=device_name,
        InstanceId=instance_id,
        VolumeId=vol_id
    )

    return response 

def list_volumes():
    response = ec2_client.describe_volumes()

    return response

def delete_volume(vol_id):
    response = ec2_client.delete_volume(VolumeId=vol_id,)
    return response

def get_volume_details(vol_id):

    response = ec2_client.describe_volumes(VolumeIds=[vol_id,],)
    return response

def create_and_attach_volume(az, size, instance_id, device_name="/dev/sdf", vt='gp2', name='auto', ssid=""):
    args = {
        "AvailabilityZone": az,
        "Size": size,
        "VolumeType": vt,
        "TagSpecifications": [
            {
                'ResourceType': 'volume',
                'Tags': [
                    {
                        'Key': 'Name',
                        'Value': name,
                    },
                ],
            },
        ],
    }

    if ssid :
        args["SnapshotId"] = ssid

    response = ec2_client.create_volume(**args)
    
    vol_id = response['VolumeId']

    instance = ec2_resource.Instance(instance_id)
    
    while True:
        time.sleep(10)
        response1 = ec2_client.describe_volumes(VolumeIds=[vol_id,],)

        state = response1['Volumes'][0]['State']
        # print(f"State: {state}")
        if state == 'available':
            break

    instance.attach_volume(
        Device=device_name,
        VolumeId=vol_id
    )

    return response