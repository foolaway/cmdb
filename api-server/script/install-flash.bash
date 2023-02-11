#!/bin/bash
if [ -d /cmdb-flask ];then rm -rf /cmdb-flask/*;else mkdir /cmdb-flask;fi

git clone https://github.com/swxfll/cmdb.git /cmdb-flask
cd /cmdb-flask/api-server/

docker rm -f cmdb-flask
docker rmi cmdb-flask
docker build --tag cmdb-flask .
docker run -d --name cmdb-flask -p 5000:5000 cmdb-flask

