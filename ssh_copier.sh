#!/usr/bin/env bash

scp home/john/.ssh/id_rsa.pub root@<vps_ip_addr>:/home/<os_username>/.ssh/authorized_keys

scp /home/john/xmen/ssh_controller/<os_username>/.credentials root@<vps_ip_addr>:/home/<os_username>/

# ssh root@<vps_ip_addr>
