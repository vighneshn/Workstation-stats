FROM ubuntu:14.04

RUN apt-get update &&apt-get install -y /
	python
	python-pip
RUN pip install flask

COPY flask2.py /tmp/flask2.py
COPY templates /tmp/templates

EXPOSE 5000
CMD ["python","/tmp/flask2.py"]
