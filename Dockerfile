FROM python:latest
COPY . /app
#RUN apt-get install -y python3
RUN apt-get update && apt-get install -y python3-pip net-tools
RUN pip install selenium
RUN pip install flask
RUN pip install webdriver-manager
RUN pip install currencyconverter
