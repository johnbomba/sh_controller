#!/usr/bin/env bash

adduser --disabled-password --gecos "" <os_username>

usermod -aG sudo <os_username>

cp .nanorc /home/<os_username>/

mkdir /home/<os_username>/.ssh

mkdir /etc/ssh/<server_name>