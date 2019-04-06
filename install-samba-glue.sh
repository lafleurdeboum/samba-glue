#!/bin/sh -v


apt-get install samba &&
(cd src && tar c etc/samba/smb.conf) | (cd / && tar xvf -) &&
systemctl restart nmbd &&
(cd src && tar c etc/polkit-1/localauthority/50-local.d/50-mount.pkla) | (cd / && tar xvf -) &&
apt-get install udisks-glue &&
(cd src/ && tar c etc/udisks-glue.conf) | (cd / && tar xvf -) &&
(cd src/ && tar c etc/systemd/system/udisks-glue.service) | (cd / && tar xvf -) &&
systemctl enable udisks-glue &&
sudo useradd samba -s /bin/nologin
echo Choose a password for user samba :
sudo smbpasswd -a samba
