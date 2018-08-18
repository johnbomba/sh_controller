#! usr/bin bash

adduser --disabled-password --gecos "" <os_username>

usermod -aG sudo <os_username>

cp .nanorc /home/<os_username>/

mkdir /etc/ssh/<os_username>

mkdir ../etc/ssh/<server_name>