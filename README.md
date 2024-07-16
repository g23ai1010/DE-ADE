High-Level Architecture 
 
This project aims to build a scalable and efficient data engineering platform on AWS. The 
platform consists of several components including data ingestion, storage, processing, 
aggregation, and visualization. 
 
Our options: 
1. Data Ingestion 
• Sources: APIs, Databases, Streaming data, Flat files (CSV, JSON, etc.) 
• Tools: AWS Kinesis, AWS S3, AWS Glue, Apache Kafka 
• We are using EC2 for Data Ingestion using Python Script and Crontab for scheduling 
2. Data Storage 
• Raw Data Storage: AWS S3 
• Processed Data Storage: AWS Redshift, AWS RDS, AWS DynamoDB 
• S3 for Data Storage 
3. Data Processing 
• Batch Processing: AWS Glue, Apache Spark on EMR 
• Stream Processing: AWS Kinesis Data Analytics, Apache Flink 
• Spark, AWS Glue and AWS Crawler using Lambda Function to Trigger Jobs 
4. Data Aggregation 
• Tools: AWS Glue, AWS Redshift, Apache Spark 
• Techniques: ETL (Extract, Transform, Load), ELT (Extract, Load, Transform) 
• AWS Glue for ETL 
5. Data Visualization 
• Tools: AWS QuickSight, Tableau, Power BI 
• We using QuickSight for Visualize the extracts reports

![image](https://github.com/user-attachments/assets/deea0173-bcaf-4533-abbb-a8a1c6ca8ec1)
