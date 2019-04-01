### Samba with udisks-glue

This helps having samba shares on removable drives. You will need `samba` and
`udisks-glue` packages.

First, to have udisks-glue work with linux, you need a polkit rule allowing it -
see in src for a basic rule allowing the plugdev group to mount and unmount
removable drives. This should work under debian derivatives (ie raspbian).

Then you need a samba share on /media. You could use the smb.conf example in src.
It only lets user `samba` access to the shares. You'll also need to add this user
and give it a password :

    # useradd -s /bin/false -d /dev/null -g sambashare samba
    # pdbedit -a samba

At last, you will have to autostart udisks-glue for the user specified in
smb.conf. An option is to make a systemd service file ; see the one included in
src. You would just need to enable it with

    # systemctl enable udisks-glue.service

