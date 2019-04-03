# Share pluggable disks with udisks-glue on Samba

These scripts help having Samba shares on removable drives. This HOWTO should
fit with any Raspberry Pi, although any modern linux should do the trick. You
will need the `samba` and `udisks-glue` packages. Indeed all commands beginning
with a `#` should be executed as the root user. So, begin with :

    # apt-get install samba udisks-glue
    # systemctl enable nmbd

Now, to have udisks-glue work with user `pi`, you need a polkit rule allowing it
- see in `src` for a basic rule allowing the plugdev group to mount and unmount
removable drives.

Then you will have to autostart udisks-glue for the user specified in smb.conf.
An option is to make a systemd service file ; see the one included in `src`. You
would just need to enable it with

    # systemctl enable udisks-glue.service

Finally you need a samba share on /media. You could use the smb.conf example in
`src`. It only lets user `samba` access to the shares _on behalf_ of user `pi`.
You'll also need to add him in and give it a password :

    # useradd -s /bin/false -d /dev/null -g sambashare samba
    # pdbedit -a samba

Last word, how do you get things unmounted ? Well the simplest option is to turn
the server off. But you could also use `lighttpd` with mod_cgi enabled, and the
admin script in `src/usr/lib/cgi-bin/drives.py`. For this to work, you'll need a
special sudo rule to let user `www-data` use `eject` _on behalf_ of user `pi`.
I haven't found the way to have it separated from my sudoers file, coming soon !

