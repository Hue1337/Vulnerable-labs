# Dockertfile, Image, Container
FROM python:3.8

ADD app.py .

RUN pip3 install requests flask
RUN pip3 install requests sqlite3

CMD ["python3", "./app.py"]