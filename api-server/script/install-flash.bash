#!/bin/bash
if [ -d /cmdb-flask ];then rm -rf /cmdb-flask/*;else mkdir /cmdb-flask;fi


# 编译 VUE
cd /cmdb-flask/web/
npm install
npm run build
docker cp node-t1:/data/web/dist/ ./