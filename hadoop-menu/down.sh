echo "Downloading Hadoop RPM package Please Wait ....."
echo " "

fileid="17UWQNVdBdGlyualwWX4Cc96KyZhD-lxz"
sleep 2
filename="jdk.rpm"
sleep 3
curl -c ./cookie -s -L "https://drive.google.com/uc?export=download&id=${fileid}" > /dev/null
sleep 3
curl -Lb ./cookie "https://drive.google.com/uc?export=download&confirm=`awk '/download/ {print $NF}' ./cookie`&id=${fileid}" -o ${filename}

echo " "
echo "Downloading Hadoop RPM package Please Wait ....."
echo " "

fileid="1541gbFeGZZJ5k9Qx65D04lpeNBw87rM5"
sleep 2
filename="hadoop.rpm"
sleep 2
curl -c ./cookie -s -L "https://drive.google.com/uc?export=download&id=${fileid}" > /dev/null
sleep 5
curl -Lb ./cookie "https://drive.google.com/uc?export=download&confirm=`awk '/download/ {print $NF}' ./cookie`&id=${fileid}" -o ${filename}

sleep 2
sudo rpm -i hadoop.rpm --force
sleep 2
sudo rpm -i jdk.rpm