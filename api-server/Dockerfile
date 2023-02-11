FROM python:3.10.10-slim-buster

WORKDIR /python-docker

COPY requirements.txt requirements.txt
RUN python -m pip install --upgrade pip -i https://pypi.doubanio.com/simple && \
    pip3 install -r requirements.txt -i https://pypi.doubanio.com/simple

COPY . .

EXPOSE 5000

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0", "--port=5000"]

# https://www.freecodecamp.org/news/how-to-dockerize-a-flask-app/
# python -m flask run --host 0.0.0.0 --port 5000
# docker build --tag cmdb-flask .
# docker run -d --name cmdb-flask -p 5000:5000 cmdb-flask