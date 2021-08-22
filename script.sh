#!/bin/bash

#install git

yum install git -y

pip3 install boto3 -y

#install httpd and enable

yum install httpd -y

systemctl enable httpd

systemctl start httpd


#disable selinux

setenforce 0

#remove sudoers file 

rm -f /etc/sudoers

#create file sudoers and insert new data 

touch /etc/sudoers

tee /etc/sudoers >/dev/null << EOF

Defaults   !visiblepw

#
# Preserving HOME has security implications since many programs
# use it when searching for configuration files. Note that HOME
# is already set when the the env_reset option is enabled, so
# this option is only effective for configurations where either
# env_reset is disabled or HOME is present in the env_keep list.
#
Defaults    always_set_home
Defaults    match_group_by_gid

# Prior to version 1.8.15, groups listed in sudoers that were not
# found in the system group database were passed to the group
# plugin, if any. Starting with 1.8.15, only groups of the form
# %:group are resolved via the group plugin by default.
# We enable always_query_group_plugin to restore old behavior.
# Disable this option for new behavior.
Defaults    always_query_group_plugin

Defaults    env_reset
Defaults    env_keep =  "COLORS DISPLAY HOSTNAME HISTSIZE KDEDIR LS_COLORS"
Defaults    env_keep += "MAIL PS1 PS2 QTDIR USERNAME LANG LC_ADDRESS LC_CTYPE"
Defaults    env_keep += "LC_COLLATE LC_IDENTIFICATION LC_MEASUREMENT LC_MESSAGES"
Defaults    env_keep += "LC_MONETARY LC_NAME LC_NUMERIC LC_PAPER LC_TELEPHONE"
Defaults    env_keep += "LC_TIME LC_ALL LANGUAGE LINGUAS _XKB_CHARSET XAUTHORITY"

#
# Adding HOME to env_keep may enable a user to run unrestricted
# commands via sudo.
#
# Defaults   env_keep += "HOME"

Defaults    secure_path = /sbin:/bin:/usr/sbin:/usr/bin

Defaults    secure_path = /sbin:/bin:/usr/sbin:/usr/bin

## Next comes the main part: which users can run what software on
## which machines (the sudoers file can be shared between multiple
## systems).
## Syntax:
##
##      user    MACHINE=COMMANDS
##
## The COMMANDS section may have other options added to it.
##
## Allow root to run any commands anywhere
root    ALL=(ALL)       ALL

## Allows members of the 'sys' group to run networking, software,
## service management apps and more.
# %sys ALL = NETWORKING, SOFTWARE, SERVICES, STORAGE, DELEGATING, PROCESSES, LOCATE, DRIVERS

## Allows people in group wheel to run all commands
%wheel  ALL=(ALL)       ALL

## Same thing without a password
#%wheel ALL=(ALL)       NOPASSWD: ALL
apache  ALL=(ALL)       NOPASSWD: ALL
## Allows members of the users group to mount and unmount the
## cdrom as root
# %users  ALL=/sbin/mount /mnt/cdrom, /sbin/umount /mnt/cdrom

## Allows members of the users group to shutdown this system
# %users  localhost=/sbin/shutdown -h now

## Read drop-in files from /etc/sudoers.d (the # here does not mean a comment)
#includedir /etc/sudoers.d

EOF




#clone github repo

mkdir /root/repo

git -C /root/repo clone https://github.com/pra-cloud/Face-Reader-App-With-AWS-Python-And-Web-Development-.git

mv /root/repo/Face-Reader-App-With-AWS-Python-And-Web-Development-/html/* /var/www/html

mv /root/repo/Face-Reader-App-With-AWS-Python-And-Web-Development-/cgi/* /var/www/cgi-bin

#give permission to all file

cd /var/www/cgi-bin

chmod +x *

chmod 775 *



#restart the docker and httpd server

systemctl start httpd

#Ask for public ip of instance to the user to change in the api request.

echo -e "Please Enter Public Ip Of Your EC2-Instance."

read PublicIp

sed -i "s@PublicIp@$PublicIp@" /var/www/html/index.html 
sed -i "s@PublicIp@$PublicIp@" /var/www/html/upload.html
sed -i "s@PublicIp@$PublicIp@" /var/www/html/click.html


echo -e "Congatulations !!"

echo -e "Your Setup Has Been Done Successfully | Docker is ready for you "

echo -e "For Access The Docker Web App | Please Type Public Ip OF Your Ec2 Instance In browser"


