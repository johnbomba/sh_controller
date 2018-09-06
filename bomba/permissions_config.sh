#! usr/bin bash

# permissions config

chown -R bomba:bomba /etc/ssh/bomba

chmod 755 /etc/ssh/bomba

chmod 644 /etc/ssh/bomba/authorized_keys

sed -i -e '/^#AuthorizedKeysFile/s/^.*$/AuthorizedKeysFile \/etc\/ssh\/bomba\/authorized_keys/' /etc/ssh/sshd_config

sed -i -e '/^PermitRootLogin/s/^.*$/PermitRootLogin no/' /etc/ssh/sshd_config

sed -i -e '/^PasswordAuthentication/s/^.*$/PasswordAuthentication no/' /etc/ssh/sshd_config

sh -c 'echo "" >> /etc/ssh/sshd_config'

sh -c 'echo "" >> /etc/ssh/sshd_config'

sh -c 'echo "# Added by Katabasis build process" >> /etc/ssh/sshd_config'

sh -c 'echo "AllowUsers bomba" >> /etc/ssh/sshd_config'

systemctl reload sshd