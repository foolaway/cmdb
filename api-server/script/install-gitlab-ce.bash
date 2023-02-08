apt update
apt upgrade -y

apt install gitlab-ce
gitlab-ctl reconfigure
