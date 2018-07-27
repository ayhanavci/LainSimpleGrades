FROM python:3.7
ENV PYTHONUNBUFFERED 1
RUN mkdir /lainsimplegrades
WORKDIR /lainsimplegrades
ADD requirements.txt /lainsimplegrades/
RUN pip install -r requirements.txt
ADD . /lainsimplegrades/
EXPOSE 8000