import json
import boto3, prjsettings as prj
import csv
import time
import io


def lambda_handler(event, context):
    bucketname = event['Records'][0]['s3']['bucket']['name']
    filename=event['Records'][0]['s3']['object']['key']
    print(bucketname)
    print(filename)
    
    
    glue = boto3.client('glue')
    crawler_state(glue)
    response= glue.start_crawler(Name = "annual_reports_crawl")    
    
    print('The Crawler Annual Report is Finshed')     
    glueJobExecution(glue)
    s3_archive_move(prj.AWS_ACCESS_KEY,prj.AWS_SECRET_KEY,bucketname)
    
    return{
        'statusCode': 200,
        'body': json.dumps("Lambda Invoke")
    }

def crawler_state(instance):
    while True:
        state=instance.get_crawler(
            Name = "annual_reports_crawl")['Crawler']['State']
        
        if state=='READY':
            break
        
        print(f'The Crawler Annual Report is {state}')
        time.sleep(5)
    

def glueJobExecution(instance):
    crawler_state(instance)
    response= instance.start_job_run(JobName = "annual_report_etl")
    
    
def s3_archive_move(access_key,access_secret_key,bucket):
    
    archive_folder='data-store-Archive/'
    stage_folder='data-store/annual-reports/csv_reports/'
    
    session = boto3.Session(
        aws_access_key_id = access_key,
        aws_secret_access_key = access_secret_key
        ) 
        
    s3=session.resource('s3')
    s3bkt=s3.Bucket(bucket)
    
    for obj in s3bkt.objects.filter(Prefix = stage_folder):
        source_key = obj.key
        
        if source_key == stage_folder:
            continue
        
        archive_key = archive_folder + source_key[len(stage_folder):]
            
        # Copy the object to the new destination
        copy_source = {'Bucket': bucket, 'Key': source_key}
        s3.Object(bucket, archive_key).copy(copy_source)
        s3.Object(bucket, source_key).delete()
    print(f'File Moved to archive {archive_folder}')    



