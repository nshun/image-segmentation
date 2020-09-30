FROM python:3.7-alpine

LABEL maintainer="Shun Nishimura"

WORKDIR /app
COPY ./requirements.txt ./
RUN pip install -r ./requirements.txt

EXPOSE 80

ENTRYPOINT ["python", "app.py"]
