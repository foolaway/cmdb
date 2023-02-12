#!/bin/bash
# 使用 Docker 部署,采用外挂数据卷的方式
# HTML资源文件: /data/html/
# NGINX配置文件 /data/conf/cmdb-web.conf
if [ -d /data/html ];then
  rm -rf /data/html/*
  echo "Empty directory /data/html"
else
  mkdir -p /data/html
  echo "create directory /data/html..."
fi
if [ -d /data/conf ];then
  rm -rf /data/conf/*
  echo "Empty directory /data/conf"
else
  mkdir -p /data/conf
  echo "create directory /data/conf..."
fi

cat >/data/conf/cmdb-web.conf<<EOF
upstream v1api {
    server 127.0.0.1:5000;
  }
server {
    server_name gala-cmdb.xlab.io;
    listen 80;
    location / {
        root /data/html;
        index index.html;
    }

    location /v1/api {
        proxy_pass http://v1api;
        rewrite ^/v1/api/(.*)$ /$1 break;
    }
}
EOF

# 部署 Nginx 容器
docker run -d --name nginx-t1 -p 80:80 -v /data/html:/data/html -v /data/conf:/etc/nginx/conf.d/ nginx

# 请将编译好的前端文件上传到宿主机的/data/html目录下





