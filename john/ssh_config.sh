#!/usr/bin/env bash

scp home/john/.ssh/id_rsa.pub root@68.183.59.77:/home/john/.ssh/authorized_keys

scp /home/john/xmen/ssh_controller/john/.credentials root@68.183.59.77:/home/john/

# ssh root@68.183.59.77
