#!/usr/bin bash

#firewalld configs

systemctl start firewalld

firewall-cmd --reload

systemctl enable firewalld

sed -i -e '/^Port/s/^.*$/Port <defined_ssh_port>/' /etc/ssh/sshd_config

firewall-cmd --add-port <defined_ssh_port>/tcp --permanent

firewall-cmd --reload

systemctl reload sshd

timedatectl set-timezone America/New_York