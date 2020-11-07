#!/usr/bin/python3
import subprocess
import os
import shlex
import boto3
import json
import datetime
import pandas as pd
import time
from prettytable import PrettyTable
from subprocess import check_call
from botocore.exceptions import ClientError
from Ec2Instances import *
from Ec2Volumes import *
from utils import *
from S3 import *
from Ec2KeyPairs import *

main_menu = ["navigate to EC2", "navigate to S3", 
            "navigate to CloudFront", "quit"
            ]


while True:
    # change_color(1)
    print("\t\t\tWelcome to the menu!!!")
    # change_color(7)
    print("\t\t\t-----------------------")
    print()

    for i in range(1, len(main_menu)+1):
        print("Press {} : To {}".format(i, main_menu[i-1]))

    option = ask_choice()
    option = main_menu[option-1]

    if option == "navigate to EC2" :
        
        ec2_menu = ["navigate to Instances", "navigate to EBS",
                    "navigate to KeyPairs", "return to previous menu"
                    ]
        while True:

            for i in range(1, len(ec2_menu)+1):
                print("Press {} : To {}".format(i, ec2_menu[i-1]))

            option = ask_choice()
            option = ec2_menu[option-1]

            if option == "navigate to Instances":
                
                instances_menu = ["launch Instances",
                                "list Instances",
                                "stop Instances",
                                "start Instances",
                                "terminate Instance",
                                "get instance details",
                                "return to previous menu"
                                ]
                while True:
                    for i in range(1, len(instances_menu)+1):
                        print("Press {} : To {}".format(i, instances_menu[i-1]))

                    option = ask_choice()
                    option = instances_menu[option-1]

                    if option == "launch Instances":
                        
                        subnet = input("Enter Subnet ID(default - default subnet): ")
                        
                        name = input("Enter Name(default- auto): ") or "auto"
                        
                        ami = input("Enter AMI ID(default- ami-098f16afa9edf40be): ") or "ami-098f16afa9edf40be"
                        instance_type = input("Enter Instance Type(default- t2.micro): ") or "t2.micro"

                        keypair = input("Enter key pair name(default - None): ")
                        sg_id = input("Enter Security Group ID(default - 'default' SG): ")
                        count = input("Enter count of instances(default- 1):") or '1'
                        count = int(count)
                        # ami and count required
                        subnet = subnet.strip() 
                        keypair = keypair.strip()
                        sg_id = sg_id.strip()
                        
                        response = create_instance(ami, instance_type, count, subnet, sg_id, keypair, name)

                    elif option == "list Instances":
                        list_instances()

                    elif option == "stop Instances":
                        instance_id = input("Enter the instance id: ")
                        
                        response = stop_instance(instance_id)

                        print("{} instance Stopped".format(instance_id))

                    elif option == "start Instances":
                        instance_id = input("Enter the instance id: ")
                        
                        response = start_instance(instance_id)
                        
                        IP = response['Reservations'][0]['Instances'][0]['PublicIpAddress']
                        print("Public IP: {}".format(IP))
                        # txt = f"ssh ec2-user@{IP} -i C:\\Users\\91733\\Desktop\\KeyPairs\\keypair2.pem"
                        # print(txt)
                        # copy2clip(txt)

                    elif option == "terminate Instance":
                        instance_id = input("Enter the instance id: ")
                        terminate_instance(instance_id)

                    elif option == "get instance details":
                        instance_id = input("Enter the instance id: ")
                        describe_instance(instance_id)
                    
                    elif option == "return to previous menu":
                        break
                    else :
                        print("Option not supported")
                                    

            elif option == "navigate to EBS":
                
                ebs_menu = ["create volume",
                            "create and attach volume",
                            "attach volume",
                            "detach volume",
                            "list volumes",
                            "delete volume",
                            "get volume details",
                            "return to previous menu"
                            ]
                
                while True:
                    for i in range(1, len(ebs_menu)+1):
                        print("Press {} : To {}".format(i, ebs_menu[i-1]))

                    option = ask_choice()
                    option = ebs_menu[option-1]

                    if option == "create volume":
                        
                        azs = list_azs()
                        az = input("Enter Subnet ID(default - {}): ".format(azs[0])).strip() or azs[0]
                        size = int(input("Enter size(default- 1): ").strip() or "1")
                        vt = input("Enter Volume type(default- gp2): ").strip() or "gp2"
                        name = input("Enter name of volume(default- auto): ").strip() or "auto"
                        
                        response = create_volume(az, size, vt='gp2', name='auto')
                        print("Volume with volume id {} created".format(response['VolumeId']))

                    elif option == "create and attach volume":
                        azs = list_azs()
                        az = input("Enter Subnet ID(default - {}): ".format(azs[0])).strip() or azs[0]
                        size = int(input("Enter size(default- 1): ").strip() or "1")
                        vt = input("Enter Volume type(default- gp2): ").strip() or "gp2"
                        name = input("Enter name of volume(default- auto): ").strip() or "auto"
                        device_name = input("Enter the device name(default- /dev/sdf) : ").strip() or "/dev/sdf"
                        instance_id = input("Enter Instance ID: ").strip()

                        response = create_and_attach_volume(az, size, instance_id, device_name, vt='gp2', name='auto')
                        print("Volume with volume id {} created".format(response['VolumeId']))

                    elif option == "attach volume":
                        vol_id = input("Enter the Volume ID : ").strip()
                        instance_id = input("Enter the Instance ID : ").strip()
                        device_name = input("Enter the device name(default- /dev/sdf) : ").strip() or "/dev/sdf"
                        try :
                            response = attach_volume(vol_id, instance_id, device_name)
                            print(response)
                        except ClientError as e:
                            print("Check if they are in same region")
                            print(e)

                    elif option == "detach volume":
                        vol_id = input("Enter the Volume ID : ").strip()
                        response = detach_volume(vol_id)

                    elif option == "list volumes":
                        response = list_volumes()
                        t = PrettyTable(['VolumeId', 'InstanceId', 'AvailabilityZone', 'Size', 'State'])
                        
                        for volume in response['Volumes']:
                            try:
                                t.add_row([volume['VolumeId'], volume['Attachments'][0].get('InstanceId', ''),  volume['AvailabilityZone'], volume['Size'], volume['State']])
                            except IndexError:
                                t.add_row([volume['VolumeId'], '-',  volume['AvailabilityZone'], volume['Size'], volume['State']])
                        print(t)


                    elif option == "delete volume":
                        vol_id = input("Enter the Volume ID : ").strip()
                        try:
                            delete_volume(vol_id)
                        except ClientError as e:
                            print("Make sure that volume is detached")
                            print(e)

                    elif option == "get volume details":
                        vol_id = input("Enter the Volume ID : ").strip()
                        response = get_volume_details(vol_id)

                        t = PrettyTable(['VolumeId', 'InstanceId', 'AvailabilityZone', 'Size', 'State'])
                        
                        volume = response['Volumes'][0]

                        try:
                            t.add_row([volume['VolumeId'], volume['Attachments'][0].get('InstanceId', ''),  volume['AvailabilityZone'], volume['Size'], volume['State']])
                        except IndexError:
                            t.add_row([volume['VolumeId'], '-',  volume['AvailabilityZone'], volume['Size'], volume['State']])
                        print(t)
                    
                    elif option == "return to previous menu":
                        break
                    else :
                        print("Option not supported")
                

            elif option == "navigate to KeyPairs":
                keypairs_menu = ["create a keypair", "delete a keypair",
                            "list keypairs", "return to previous menu"
                            ]
                
                while True:

                    for i in range(1, len(keypairs_menu)+1):
                        print("Press {} : To {}".format(i, keypairs_menu[i-1]))

                    option = ask_choice()
                    option = keypairs_menu[option-1]

                    if option == "create a keypair":
                        keypair_name = input("Enter the name of Keypair : ").strip()
                        print("Creating KeyPair ...")
                        response = create_keypair(keypair_name)
                        path = input("Enter the path to save Keypair : ").strip()
                        print("Saving KeyPair ...")
                        with open(os.path.join(path,'{}.pem'.format(response['KeyName'])), 'w') as file:
                            file.write(response['KeyMaterial'])
                        print("Created and saved KeyPair")

                    elif option == "delete a keypair":
                        keypair_name = input("Enter the name of Keypair : ").strip()
                        print("Deleting KeyPair ...")
                        response = delete_keypair(keypair_name)                        
                        # print(response)
                        print("Deleted KeyPair")

                    elif option == "list keypairs":
                        response = list_keypairs()
                        t = PrettyTable(['KeyPairId', 'KeyName'])
                        for keypair in response['KeyPairs']:
                            t.add_row([keypair['KeyPairId'], keypair['KeyName']])
                        print(t)

                    elif option == "return to previous menu":
                        break
                    else :
                        print("Option not supported")
            
            elif option == "return to previous menu":
                break

            else :
                print("Option not supported")

    elif option == "navigate to S3" :
        s3_menu = ["create a bucket", "delete bucket",
                    "list buckets","upload files to bucket",
                    "download files from bucket", "list files in bucket",
                    "delete file in bucket", "return to previous menu"
                    ]

        while True:

            for i in range(1, len(s3_menu)+1):
                print("Press {} : To {}".format(i, s3_menu[i-1]))

            option = ask_choice()
            option = s3_menu[option-1]

            if option == "create a bucket":
                bucket_name = input("Enter the name of bucket : ").strip()
                region = input("Enter the region of bucket(default- us-west-1) : ").strip() or "us-west-1"
                response = create_bucket(bucket_name, region)
                if not response[0]:
                    print("Bucket not created")
                    print(response[1])
                else :
                    print("Bucket created ...")

            elif option == "delete bucket":
                bucket_name = input("Enter the name of bucket : ").strip()
                print("Deleting bucket {}".format(bucket_name))
                delete_bucket(bucket_name)
                print("Deleted bucket")
            
            
            elif option == "list buckets":
                response = list_buckets()
                            
                print('Existing buckets:')
                for bucket in response['Buckets']:
                    print(f'  {bucket["Name"]}')
            
            elif option == "upload files to bucket":
                path = input("Enter the path to file : ").strip()
                bucket_name = input("Enter the name of bucket : ").strip()
                obj_name = input("Enter the name of object(default- path to file) : ").strip() or path
                public = input("Make object public[y/n](default- n) : ").strip() or "n"
                if public.lower() == "y":
                    public = True
                elif public.lower() == "n":
                    public = False
                print("File uploading ...")
                response = upload_file(path, bucket_name, obj_name, public)
                print(response)
                
                if not response[0]:
                    print("File not uploaded")
                    print(response[1])
                else :
                    print("File uploaded")

                
            elif option == "download files from bucket":
                bucket_name = input("Enter the name of bucket : ").strip()
                obj_name = input("Enter the name of object: ").strip()
                path = input("Enter the path to file(default - path to menu): ").strip() or obj_name
                
                download_file(bucket_name, obj_name, path)
                
            elif option == "list files in bucket":
                bucket_name = input("Enter the name of bucket : ").strip()
                response = list_files(bucket_name)
                for key in response['Contents']:
                    print(key['Key'])

            elif option == "delete file in bucket":
                bucket_name = input("Enter the name of bucket : ").strip()
                obj_name = input("Enter the name of object: ").strip()
                print("Deleting object ...")
                response = delete_file(bucket_name, obj_name)
                print("Object deleted")

            elif option == "return to previous menu":
                break

            else :
                print("Option not supported")
                
        

    elif option == "navigate to CloudFront":
        cloudfront_menu = ["create a distribution with S3 as the origin domain", 
                            "return to previous menu"
                            ]
        while True:
            for i in range(1, len(cloudfront_menu)+1):
                print("Press {} : To {}".format(i, cloudfront_menu[i-1]))

            option = ask_choice()
            option = cloudfront_menu[option-1]

            if option == "create a distribution with S3 as the origin domain":
                pass
            elif option == "return to previous menu":
                break
            else :
                print("Option not supported")
        

    elif option == "quit" :
        break
    else :
        print("Option not supported")