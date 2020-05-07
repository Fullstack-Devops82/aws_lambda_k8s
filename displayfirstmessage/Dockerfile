FROM		ubuntu:18.04

ARG		AWS_ACCESS_KEY
ENV		AWS_ACCESS_KEY=$AWS_ACCESS_KEY

ARG		AWS_SECRET_ACCESS_KEY
ENV		AWS_SECRET_ACCESS_KEY=$AWS_SECRET_ACCESS_KEY

ARG		AWS_REGION=us-east-2
ENV		AWS_REGION=$AWS_REGION

MAINTAINER	nazarmiroshnichenko1994@gmail.com
RUN		apt-get -y update

RUN		apt-get -y install python3-pip
RUN		pip3 install stefuna
#RUN		pip3 install awscli

COPY		*.py ~/
RUN 		mkdir ~/.aws
RUN		touch ~/.aws/credentials
RUN		echo "[default]"'\n'"aws_access_key_id=${AWS_ACCESS_KEY}"'\n'"aws_secret_access_key=${AWS_SECRET_ACCESS_KEY}" > ~/.aws/credentials
RUN		chmod 777 ~/.aws/credentials

WORKDIR		~/
