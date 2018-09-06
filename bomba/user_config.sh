#! usr/bin bash

adduser --disabled-password --gecos "" bomba

usermod -aG sudo bomba

cp .nanorc /home/bomba/

mkdir /etc/ssh/bomba

mkdir ../etc/ssh/<server_name>