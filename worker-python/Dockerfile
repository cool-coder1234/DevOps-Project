FROM python:3.11-slim
WORKDIR /app
COPY requirements/common.txt requirements/common.txt
COPY requirements/docker.txt requirements/docker.txt
RUN pip install --upgrade pip && \
    pip install flask flask-sqlalchemy flask-migrate flask-login \
    flask-mail flask-bootstrap flask-wtf flask-moment \
    flask-httpauth flask-pagedown redis gunicorn pymysql python-dotenv
COPY . .
CMD ["python", "flasky.py"]