FROM python:3.9

RUN apt update && apt upgrade -y

COPY . .

RUN pip install requests
RUN pip install treading

CMD python test of prfile.py
