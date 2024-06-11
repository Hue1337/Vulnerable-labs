# Dockertfile, Image, Container
FROM python:3.8-slim

WORKDIR /app
COPY ./ /app

RUN pip install -r requirements.txt
EXPOSE 80

ENTRYPOINT ["python"]
CMD ["app.py", "-p", "80"]