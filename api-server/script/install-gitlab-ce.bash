#!/usr/bin/env bash

sed -i "s/cn.archive.ubuntu.com/mirrors.tuna.tsinghua.edu.cn/g" /etc/apt/sources.list
curl https://packages.gitlab.com/gpg.key 2> /dev/null | sudo apt-key add - &>/dev/null
echo "deb https://mirrors.tuna.tsinghua.edu.cn/gitlab-ce/ubuntu jammy main" > /etc/apt/sources.list.d/gitlab-ce.list

apt update
apt upgrade -y

apt install gitlab-ce
gitlab-ctl reconfigure
