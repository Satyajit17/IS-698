import boto3

s3 = boto3.client('s3')
bucket_name = 'my-boto3-s3-bucket-satyajit'  # Change this to a globally unique name
region = 'us-east-1'

response = s3.create_bucket(Bucket=bucket_name, Region=region)
print(f'Bucket {bucket_name} created successfully!')
