FROM registry.cn-shenzhen.aliyuncs.com/runcobo/nginx:stable-alpine
RUN yum install wget \
    && wget -O redis.tar.gz "http://download.redis.io/releases/redis-5.0.3.tar.gz" \
    && tar -xvf redis.tar.gz
