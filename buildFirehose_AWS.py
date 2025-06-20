import boto3

if __name__ == '__main__':
    client = boto3.client('firehose')

    response = client.create_delivery_stream(
        DeliveryStreamName = 'kinesisyuvika',
        DeliveryStreamType = 'DirectPut',
        S3DestinationConfiguration = {
            'RoleARN': 'arn:aws:iam::481329480042:role/firehose_delivery_role',
            'BucketARN': 'arn:aws:s3:::glue-bucket-yuvika',
            'Prefix': 'yuvikatwitter2025',
            'BufferingHints': {
                'SizeInMBs': 10,
                'IntervalInSeconds': 120
            }

        }
    )

    print(response)