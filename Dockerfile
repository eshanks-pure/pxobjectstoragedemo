FROM python:3.10.7-alpine3.16
WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
CMD [ "python", "./write-to-s3.py" ]
