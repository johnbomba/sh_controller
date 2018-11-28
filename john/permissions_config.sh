#!/usr/bin/env bash

# permissions config

chown -R john:john /etc/ssh/john

chmod 755 /etc/ssh/john

chmod 644 /etc/ssh/john/authorized_keys

sed -i -e '/^#AuthorizedKeysFile/s/^.*$/AuthorizedKeysFile \/etc\/ssh\/john\/authorized_keys/' /etc/ssh/sshd_config

sed -i -e '/^PermitRootLogin/s/^.*$/PermitRootLogin no/' /etc/ssh/sshd_config

sed -i -e '/^PasswordAuthentication/s/^.*$/PasswordAuthentication no/' /etc/ssh/sshd_config

sh -c 'echo "" >> /etc/ssh/sshd_config'

sh -c 'echo "" >> /etc/ssh/sshd_config'

sh -c 'echo "# Added by Katabasis build process" >> /etc/ssh/sshd_config'

sh -c 'echo "AllowUsers john" >> /etc/ssh/sshd_config'
  
systemctl reload sshd