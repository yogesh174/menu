import os
print("\n\n")
print("\t\t\t\t\t\tWelcome to hadoop cluster setup menu")
print("\t\t\t\t\t\t------------------------------------")
print(''' \t\t\t\t\t\tFor setting hadoop cluster you have to follow certain steps:
          \t\t\t\t\tStep:1 Give details about namenode.
          \t\t\t\t\tStep:2 Give details about datanode.
          \t\t\t\t\tStep:3 give details about client.
''')
Namenode_IP = input("\t\t\t\t\t\tGive IP at which you want to configure namenode: ")
print("Downloading and Configuring Hadoop and JAVA")

# copy down.py file that contains code for downloading and installing hadoop and java rpm for linux

os.system("scp down.sh root@{}:/root/".format(Namenode_IP))

os.system("ssh root@{} sudo chmod +x down.sh ".format(Namenode_IP))

os.system("ssh root@{} sudo sh down.sh".format(Namenode_IP))

#copy namenode.py into instance
os.system("scp nameNode.py root@{}:/root/".format(Namenode_IP))

#install python3 on the instance
os.system("sleep 2")
os.system("ssh root@{} sudo yum install python3 -y".format(Namenode_IP))

#setup namenode core-site.xml and hdfs-site.xml
os.system("sleep 2")
os.system("ssh root@{} sudo python3 nameNode.py".format(Namenode_IP))

#format the namenode
os.system("sleep 2")
os.system("ssh root@{} sudo hadoop namenode -format".format(Namenode_IP))

#start namenode
os.system("sleep 2")
os.system("ssh root@{} sudo hadoop-daemon.sh start namenode".format(Namenode_IP))


Datanode_IP = []
count_datanode = int(input("\t\t\t\t\t\tHow many datanode you want to configure: "))
for i in range(0,count_datanode):
	d_ip = input("\t\t\t\t\t\tGive IP at which you want to configure datanode{}:".format(i+1))
	Datanode_IP.append(d_ip)
	print("Downloading and Configuring Hadoop and JAVA")
	os.system("scp down.sh root@{}:/root/".format(Datanode_IP[i]))
	os.system("ssh root@{} sudo chmod +x down.sh ".format(Datanode_IP[i]))
	
	os.system("ssh root@{} sudo sh down.sh".format(Datanode_IP[i]))
	
	os.system("scp dataNode.py root@{}:/root/".format(Datanode_IP[i]))
	os.system("sleep 2")

	os.system("ssh root@{} sudo yum install python3 -y".format(Datanode_IP[i]))
	os.system("sleep 2")

	#setup datanode core-site.xml and hdfs-site.xml
	os.system("ssh root@{} sudo python3 dataNode.py".format(Datanode_IP[i]))
	os.system("sleep 2")

	#start datanode
	os.system("ssh root@{} sudo hadoop-daemon.sh start datanode".format(Datanode_IP[i]))


Client_IP = []
count_client = int(input("\t\t\t\t\t\tHow many client you want to configure: "))
for i in range(0,count_client):
	c_ip = input("\t\t\t\t\t\tGive IP at which you want to configure client: ")
	Client_IP.append(c_ip)
	print("Downloading and Configuring Hadoop and JAVA")
	os.system("scp down.sh root@{}:/root/".format(Client_IP[i]))
	
	os.system("ssh root@{} sudo chmod +x down.sh ".format(Client_IP[i]))
	
	os.system("ssh root@{} sudo sh down.sh".format(Client_IP[i]))
	
	os.system("sleep 2")
	
	os.system("scp client.py root@{}:/root/".format(Client_IP[i]))
	os.system("sleep 2")

	os.system("ssh root@{} sudo yum install python3 -y".format(Client_IP[i]))
	os.system("sleep 2")

	#setup datanode core-site.xml and hdfs-site.xml
	os.system("sleep 2")
	os.system("ssh root@{} sudo python3 client.py".format(Client_IP[i]))