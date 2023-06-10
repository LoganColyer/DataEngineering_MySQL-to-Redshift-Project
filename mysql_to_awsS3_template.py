# Import libraries
import mysql.connector
import pandas as pd
import csv
import boto3

# Connect to MySQL and store in cnxn variable
cnxn = mysql.connector.connect(user='YOUR_USERNAME',
                              password='YOUR_PASSWORD',
                              host='YOUR_HOST',
                              database='YOUR_DATABASE')

# Create SQL Statement with triple brackets to keep SQL formatting
SQL_STATEMENT = """
SELECT * FROM YOUR_TABLENAME
"""

# Read SQL Statement into pandas dataframe
df = pd.read_sql(SQL_STATEMENT,cnxn)

# You don't have to setup your code like this. I just prefer it so my access keys aren't statically saved in my code
# Open the csv file where your access key and secret access key live. You'll need to change your path below.
with open(r'C:\Users\aws-admin-programmatic-access_accessKeys.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        value = row[0:2]
        ACCESS_KEY_ID = value[0]
        SECRET_ACCESS_KEY = value[1]

# Create s3 variable containing AWS credentials
s3 = boto3.resource(
    service_name='s3',
    region_name='YOUR_REGION', # My region is 'us-west-2'
    aws_access_key_id=ACCESS_KEY_ID, 
    aws_secret_access_key=SECRET_ACCESS_KEY
)

# Save to csv format
df.to_csv('YOUR_DATA.csv')

# Upload files to S3 bucket
s3.Bucket('YOUR_S3_BUCKET_NAME').upload_file(Filename='YOUR_DATA.csv', Key='YOUR_DATA.csv')