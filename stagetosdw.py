!pip install boto3

import boto3
import csv
import json
import time


# AWS credentials and region
AWS_ACCESS_KEY = 'AKIA47CRZ7X6RZUF7AWX'
AWS_SECRET_KEY = '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'
AWS_SECRET_BUCKET_NAME = "aws-glue-ade-bucket"
AWS_REGION_NAME = 'eu-north-1'
stage_folder = 'staging/'
archive_folder='Archive/'
destination_folder = 'data-store/annual-reports/csv_reports/'


session = boto3.Session(
    aws_access_key_id = AWS_ACCESS_KEY,
    aws_secret_access_key = AWS_SECRET_KEY
    ) 
    
s3=session.resource('s3')
s3bkt=s3.Bucket(AWS_SECRET_BUCKET_NAME)

for obj in s3bkt.objects.filter(Prefix = stage_folder):
    source_key = obj.key
    
    if source_key == stage_folder:
        continue
    
    destination_key = destination_folder + source_key[len(stage_folder):]
    archive_key = archive_folder + source_key[len(stage_folder):]
        
    # Copy the object to the new destination
    copy_source = {'Bucket': AWS_SECRET_BUCKET_NAME, 'Key': source_key}
    s3.Object(AWS_SECRET_BUCKET_NAME, destination_key).copy(copy_source)
    s3.Object(AWS_SECRET_BUCKET_NAME, archive_key).copy(copy_source)
    
    s3.Object(AWS_SECRET_BUCKET_NAME, source_key).delete()



