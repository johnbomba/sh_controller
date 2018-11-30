#!/usr/bin/env bash

adduser --disabled-password --gecos "" john

usermod -aG sudo john

cp .nanorc /home/john/

mkdir /home/john/.ssh

# mkdir /etc/ssh/john