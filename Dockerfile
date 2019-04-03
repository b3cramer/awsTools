FROM python:2.7
MAINTAINER Matt Cramer b3cramer@gmail.com
ADD ${pwd}/awsFileMover.py /
RUN pip install boto3
ENTRYPOINT [ "python","./awsFileMover.py" ]
