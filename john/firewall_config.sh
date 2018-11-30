#!/usr/bin/env bash

#firewalld configs

systemctl start firewalld

firewall-cmd --reload

systemctl enable firewalld

sed -i -e '/^#Port/s/^.*$/Port 9876/' /etc/ssh/sshd_config

firewall-cmd --add-port 9876/tcp --permanent

firewall-cmd --reload

systemctl reload sshd

timedatectl set-timezone America/New_York