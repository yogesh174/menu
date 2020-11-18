def client():
	import os
	namenode_IP = input("\t\t\t\t\tEnter namenode IP: ")
	namenode_port = input("\t\t\t\t\tEnter port number of namenode: ")
	print(''' \t\t\t\t\t Select Option:
		Option1: Do you want set replica size and block size both
		Option2: Do you want to setup only replica size
		Option3: Do you want to setup only block size
		Option4: Don't want to setup replica size and block size and leave as default
	''')
	
	option = int(input("\t\t\t\t\tSelect any option:"))

	if(option==1):
		replica_size=int(input("Enter replica size:"))
		block_size=int(input("Enter block size in bytes:"))
		file_hdfs = open("/etc/hadoop/hdfs-site.xml","w")
		hdfs_data =  '''<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>
 
<!-- Put site-specific property overrides in this file. -->

<configuration>
<property>
<name>dfs.replication</name>
<value>{}</value>
</property>

<property>
<name>dfs.block.size</name>
<value>{}</value>
</property>
</configuration>\n'''.format(replica_size,block_size)
		file_hdfs.write(hdfs_data)

	if(option==2):
		replica_size=int(input("Enter replica size:"))
		file_hdfs = open("/etc/hadoop/hdfs-site.xml","w")
		hdfs_data =  '''<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>
 
<!-- Put site-specific property overrides in this file. -->

<configuration>
<property>
<name>dfs.replication</name>
<value>{}</value>
</property>
</configuration>\n'''.format(replica_size)
		file_hdfs.write(hdfs_data)

	if(option==3):
		block_size=int(input("Enter block size in bytes:"))
		file_hdfs = open("/etc/hadoop/hdfs-site.xml","w")
		hdfs_data =  '''<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>
 
<!-- Put site-specific property overrides in this file. -->

<configuration>
<property>
<name>dfs.block.size</name>
<value>{}</value>
</property>
</configuration>\n'''.format(block_size)
		file_hdfs.write(hdfs_data)

	if(option==4):
		file_hdfs = open("/etc/hadoop/hdfs-site.xml","w")
		hdfs_data =  '''<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>
 
<!-- Put site-specific property overrides in this file. -->

<configuration>
</configuration>\n'''
		file_hdfs.write(hdfs_data)


	file_core = open("/etc/hadoop/core-site.xml", "w")
	core_data = '''<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>

<!-- Put site-specific property overrides in this file. -->

<configuration>
<property>
<name>fs.default.name</name>
<value>hdfs://{}:{}</value>
</property>
</configuration>\n'''.format(namenode_IP,namenode_port)
	file_core.write(core_data)   

client()