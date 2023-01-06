from aws_cdk import (
    # Duration,
    Stack,
    aws_s3 as s3,
    aws_cloudtrail as cloudtrail,
    aws_logs as logs,
    # aws_sqs as sqs,
)
from constructs import Construct

class DataeventsloggingStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # loggingbucket = s3.Bucket(self, 'loggingbucket',
        #     encryption=s3.BucketEncryption.S3_MANAGED,
        #     versioned=True,
        #     )
        
        dataeventstrail = cloudtrail.Trail(self, 'dataeventstrail',
            enable_file_validation=True,
            send_to_cloud_watch_logs=True,
            )

        dataeventstrail.log_all_s3_data_events()
        

        # The code that defines your stack goes here

        # example resource
        # queue = sqs.Queue(
        #     self, "DataeventsloggingQueue",
        #     visibility_timeout=Duration.seconds(300),
        # )
