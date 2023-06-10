# DataEngineering_MySQL-to-Redshift-Project

This project was inspired by an upcoming need to move On-Premises data into a Cloud tool for the company I work for

Here's the project architecture:
![RedshiftProject_Architecture](https://github.com/LoganColyer/DataEngineering_MySQL-to-Redshift-Project/assets/72894342/09c88b88-ec39-41d9-a913-23a30b3fc30e)


Here's what I did

1. Navigated to the [S&P500](https://finance.yahoo.com/quote/%5EGSPC?p=%5EGSPC) on Yahoo Finance to download as much historical data as possible to a csv file
2. Inserted the CSV file into my local MySQL database
3. Created s3 Bucket in AWS
4. Wrote the python script to 
    (1) Pull the data from MySQL 
    (2) Convert to a Pandas DataFrame 
    (3) Save DataFrame to CSV 
    (4) Connects to an s3 Bucket 
    (5) Upload CSV file to s3 Bucket
5. Create Amazon Redshift database and load data from s3 Bucket
6. 

This is only phase one of the project. I plan to add more things like automation with Apache Airflow and leveraging Stock Market API's instead of manually downloading CSV files to upload onto MySQL. But this was a good first step to learning how to transfer data from one relational database to another. Especially going from On-Prem to the Cloud. 
