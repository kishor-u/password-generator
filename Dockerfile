FROM python:3.9

LABEL maintainer="kishoru8@gmail.com"

WORKDIR /app

COPY requirements.txt /app

RUN pip --version && python --version && pip install -r requirements.txt

COPY . /app

EXPOSE 8080

ENTRYPOINT ["python"]

CMD ["app.py"]