#!/usr/bin/env bash

# permissions config

chown -R <os_username>:<os_username> /etc/ssh/<os_username>

chmod 755 /etc/ssh/<os_username>

chmod 644 /etc/ssh/<os_username>/authorized_keys

sed -i -e '/^#AuthorizedKeysFile/s/^.*$/AuthorizedKeysFile \/etc\/ssh\/<os_username>\/authorized_keys/' /etc/ssh/sshd_config

sed -i -e '/^PermitRootLogin/s/^.*$/PermitRootLogin no/' /etc/ssh/sshd_config

sed -i -e '/^PasswordAuthentication/s/^.*$/PasswordAuthentication no/' /etc/ssh/sshd_config

sh -c 'echo "" >> /etc/ssh/sshd_config'

sh -c 'echo "" >> /etc/ssh/sshd_config'

sh -c 'echo "# Added by Katabasis build process" >> /etc/ssh/sshd_config'

sh -c 'echo "AllowUsers <os_username>" >> /etc/ssh/sshd_config'
  
systemctl reload sshd