#Deriving the latest base image
FROM python:3.10

# Any working directory can be chosen as per choice like '/' or '/home' etc
# i have chosen /app
WORKDIR /app

#to COPY the remote file at working directory in container
COPY ~/automation/scraper/crawler_advent_lions/. ./
# Now the structure looks like this '/usr/app/src/test.py'

RUN pip install --trusted-host pypi.python.org -r requirements.txt

RUN apt-get update && apt-get install -y wget unzip && \
    wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb &&\
    apt install -y google-chrome-stable_current_amd64.deb && \
    rm google-chrome-stable_current_amd64.deb && \
    apt-get clean

#CMD instruction should be used to run the software
#contained by your image, along with any arguments.

CMD [ "python", ".send_mail.py"]