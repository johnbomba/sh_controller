#! /usr/bin bash

scp /home/john/.ssh/id_rsa.pub root@<vps_ip_addr>:/etc/ssh/<os_username>/authorized_keys

scp <os_username>/.credentials root@<vps_ip_addr>:/home/<os_username>/

# ssh root@<vps_ip_addr>