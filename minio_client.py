import json
from minio import Minio
from minio.error import ResponseError

with open('config.json') as config:
    config_file = json.load(config)


class Storage:
    def __init__(self):
        self._storageClient = Minio(config_file['minio_host'],
                              access_key=config_file['access_key'],
                              secret_key=config_file['secret_key'],
                              secure=True)

    def create_bucket(self, bucketName):
        try:
            self._storageClient.make_bucket(bucketName)
        except BucketAlreadyOwnedByYou as err:
            print(err)
        except BucketAlreadyExists as err:
            print(err)
        except ResponseError as err:
            raise

    def upload_to_bucket(self, bucketName, objectName, objectPath):
        try:
            print(f'uploading object {objectName} to bucket {bucketName}')
            self._storageClient.fput_object(bucketName, objectName, objectPath)
        except ResponseError as err:
            print(err)

