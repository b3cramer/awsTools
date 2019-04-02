Project guide:
Given the names of two S3 buckets in a single region (e.g. us-east-1) and a threshold size in MB, create a Python application that can copy all files greater than the threshold size from one bucket to another. (hint: use boto3)
Containerize this script with Docker. The container should take the two bucket names and the threshold as arguments that will be passed on to the Python application. For testing, consider using environment variables to pass in creds. This could be done with an IAM Role too. (hint: use the python base image)
Version control all of these files into a public GitHub repository. Meaningful and concise commit messages that show how you worked through this problem are a big plus.
