FROM node:16.18.0

WORKDIR /cmdb-web
RUN git clone https://github.com/swxfll/cmdb.git /cmdb-web && cd web && npm install && npm run build

CMD ["/bin/bash", "top"]

docker rm -f cmdb-web
docker rmi cmdb-web
docker build --tag cmdb-web .
docker run -d --name cmdb-web cmdb-web