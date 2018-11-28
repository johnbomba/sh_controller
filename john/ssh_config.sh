#!/usr/bin/env bash

scp /home/john/.ssh/id_rsa.pub root@178.128.148.102:/etc/ssh/john/authorized_keys

scp john/.credentials root@178.128.148.102:/home/john/

# ssh root@178.128.148.102