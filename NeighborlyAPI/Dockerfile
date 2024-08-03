FROM mcr.microsoft.com/azure-functions/python:3.0-python3.8-appservice

COPY . /home/site/wwwroot

RUN pip install -r /home/site/wwwroot/requirements.txt
