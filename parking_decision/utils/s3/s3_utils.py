from typing import Iterator, List

# Internal packages
from apalib.configurations.get_config import get_config

# External packages
import boto3
from botocore.exceptions import ClientError


class S3Utils:

    def __init__(self):
        self._session = boto3.session.Session(region_name=get_config()["AWS_REGION"])
        self._client = self._session.client('s3', endpoint_url=get_config()["AWS_ENDPOINT_URL"])
        self._resource = self._session.resource(service_name='s3', endpoint_url=get_config()["AWS_ENDPOINT_URL"])

    def create_bucket(self, bucket_name: str) -> None:
        try:
            self._client.create_bucket(Bucket=bucket_name,
                                       CreateBucketConfiguration={'LocationConstraint': get_config()["AWS_REGION"]})
        except ClientError as e:
            if e.response.get("Error").get("Code") == 'BucketAlreadyOwnedByYou':
                pass
            else:
                raise

    def clear_bucket(self, bucket_name: str) -> None:
        try:
            for obj in self._client.list_objects(Bucket=bucket_name).get("Contents", []):
                self._client.delete_object(Bucket=bucket_name, Key=obj["Key"])
        except ClientError as e:
            pass

    def get_objects(self, bucket_name: str, prefix: str) -> Iterator:
        return self._resource.Bucket(bucket_name).objects.filter(Prefix=prefix)

    def get_file_data(self, bucket_name: str, file_key: str) -> str:
        response_data: bytes = self._resource.Object(bucket_name, file_key).get()
        data = response_data['Body'].read()
        return data.decode()

    def get_file_lines(self, bucket_name: str, file_key: str) -> List[str]:
        return self.get_file_data(bucket_name=bucket_name, file_key=file_key).splitlines()

    def put_text(self, bucket_name: str, file_key: str, text: str) -> None:
        try:
            self._client.put_object(Bucket=bucket_name,
                                    Key=file_key,
                                    Body=text.encode('ascii'))
        except ClientError as e:
            raise

    def put_file(self, bucket_name: str, key: str, file_path: str) -> None:
        try:
            self._client.put_object(Bucket=bucket_name,
                                    Key=key,
                                    Body=open(file_path, 'rb'))
        except ClientError as e:
            raise
