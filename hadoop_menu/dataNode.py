def datanode():
	import os
	datanode_folder = input("\t\t\tFolder name for datanode:")
	os.system("sudo rm -rf {}".format(datanode_folder))
	os.system("sudo mkdir {}".format(datanode_folder))
	namenode_IP = input("\t\t\tEnter namenode IP: ")
	namenode_port = input("\t\t\tEnter port number of namenode: ")
	file_hdfs = open("/etc/hadoop/hdfs-site.xml","w")
	hdfs_data =  '''<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>
 
<!-- Put site-specific property overrides in this file. -->

<configuration>
<property>
<name>dfs.data.dir</name>
<value>{}</value>
</property>
</configuration>\n'''.format(datanode_folder)
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
	  


datanode()
