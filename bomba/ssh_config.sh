#! /usr/bin bash

scp /home/john/.ssh/id_rsa.pub root@167.99.224.47:/etc/ssh/bomba/authorized_keys

scp bomba/.credentials root@167.99.224.47:/home/bomba/

# ssh root@167.99.224.47