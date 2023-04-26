FROM python:3.11

WORKDIR /opt

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

ENTRYPOINT ["bash", "entrypoint.sh"]

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "127.0.0.1:8000"]
