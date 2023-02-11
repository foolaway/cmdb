#!/bin/bash
if [ -d /cmdb-flask ];then rm -rf /cmdb-flask/*;else mkdir /cmdb-flask;fi
cd /cmdb-flask
git clone https://github.com/swxfll/cmdb.git
cd cd cmdb/api-server/

docker rm -f cmdb-flask
docker rmi cmdb-flask
docker build --tag cmdb-flask .
docker run -d --name cmdb-flask -p 5000:5000 cmdb-flask

