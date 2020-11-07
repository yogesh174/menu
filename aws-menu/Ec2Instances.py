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

ec2_resource = boto3.resource('ec2')
ec2_client = boto3.client('ec2')

def list_sgs():
    print('All Security Groups:')
    print('----------------')
    sg_all = ec2_client.describe_security_groups()
    for sg in sg_all['SecurityGroups'] :
        print(sg['GroupName'])

def list_subnets():
    print('Subnets:')
    print('-------')
    sn_all = ec2_client.describe_subnets()
    print("  AZs \t", "    Subnet ID")
    for sn in sn_all['Subnets'] :
        print(sn['AvailabilityZone'], sn['SubnetId'])

def create_instance(ami, instance_type, count, subnet, sg_id, keypair, name):
    
    args = {
        "ImageId": ami,
        "InstanceType": instance_type,
        "MaxCount": count,
        "MinCount": count,
        "Monitoring": {
            'Enabled': False
        },
        "TagSpecifications": [
            {
                'ResourceType': 'instance',
                'Tags': [
                    {
                        'Key': 'Name',
                        'Value': name,
                    },
                ],
            },
        ],
    }
    
    if subnet :
        args["SubnetId"] = subnet
        
    if keypair:
        args["KeyName"] = keypair

    if sg_id:
        args["SecurityGroupIds"] = [sg_id,]
    
    response = ec2_client.run_instances(**args)
    
    # while True:
    #     time.sleep(10)
    #     response = ec2_client.describe_instances(InstanceIds=[instance_id,],)
    #     state = response['Reservations'][0]['Instances'][0]['State']['Name']
    #     # print(f"State: {state}")
    #     if state == 'running':
    #         break

    return response

def start_instance(instance_id):
    print("Starting instance {} ...".format(instance_id))
    response = ec2_client.start_instances(InstanceIds=[instance_id])

    while True:
        time.sleep(10)
        response1 = ec2_client.describe_instances(InstanceIds=[instance_id,],)
        state = response1['Reservations'][0]['Instances'][0]['State']['Name']
        # print(f"State: {state}")
        if state == 'running':
            break
    
    print("Instance {} started".format(instance_id))
    
    return response

def stop_instance(instance_id):
    print("Stopping instance {} ...".format(instance_id))
    response = ec2_client.stop_instances(InstanceIds=[instance_id])

    while True:
        time.sleep(10)
        response1 = ec2_client.describe_instances(InstanceIds=[instance_id,],)
        state = response1['Reservations'][0]['Instances'][0]['State']['Name']
        # print(state)
        if state == 'stopped':
            break
    
    return response

def terminate_instance(instance_id):
    print("Terminating instance {} ...".format(instance_id))
    ec2_client.terminate_instances(InstanceIds=[instance_id,],)
    while True:
        time.sleep(10)
        response1 = ec2_client.describe_instances(InstanceIds=[instance_id,],)
        state = response1['Reservations'][0]['Instances'][0]['State']['Name']
        # print(state)
        if state == 'terminated':
            break
    
    print("Instance {} terminated".format(instance_id))


def list_instances():
    response = ec2_client.describe_instances()

    t = PrettyTable(['InstanceId', 'InstanceType', 'State', 'SubnetId', "AZ", 'SecurityGroups', 'Tags', 'KeyPair'])


    for reservation in response["Reservations"]:
        for instance in reservation["Instances"]:
            # print(instance)
            try:
                t.add_row([instance["InstanceId"], instance['InstanceType'], instance['State']['Name'], instance.get('SubnetId', ''), instance.get('Placement', '').get('AvailabilityZone', ''), instance['SecurityGroups'][0]['GroupName'], instance['Tags'], instance.get('KeyName', '')])
            except IndexError:
                pass
    print(t)

def describe_instance(instance_id):
    response = ec2_client.describe_instances(InstanceIds=[instance_id,],)

    t = PrettyTable(['InstanceId', 'InstanceType', 'State', 'SubnetId', 'SecurityGroups', 'Tags', 'KeyPair'])

    for reservation in response["Reservations"]:
        for instance in reservation["Instances"]:
            try:
                t.add_row([instance["InstanceId"], instance['InstanceType'], instance['State']['Name'], instance['SubnetId'], instance['SecurityGroups'][0]['GroupName'], instance['Tags'], instance['KeyName']])
            except KeyError:
                t.add_row([instance["InstanceId"], instance['InstanceType'], instance['State']['Name'], instance['SubnetId'], instance['SecurityGroups'][0]['GroupName'], instance['Tags'], '-'])
    print(t)

def detach_volume(vol_id):
    response = ec2_client.detach_volume(
        Force=True,
        VolumeId=vol_id
    )
    return response