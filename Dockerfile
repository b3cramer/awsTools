FROM python:2.7
MAINTAINER Matt Cramer b3cramer@gmail.com
WORKDIR /Users/cramerm/GitHub/awsTools
ADD awsFileMover.py /
RUN pip install boto3
CMD [ "python", "./awsFileMover", "-OPTIONAL_FLAG" ]
