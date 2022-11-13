"""
exercise 8
Shaked Horovitz
"""

import base64
import os.path

from azure.storage.blob import BlobServiceClient


CONNECTION_STRING_SRC = 'DefaultEndpointsProtocol=https;AccountName=onboardingpractice;AccountKey=7nUB5BsakecXpB7r2ETp02p+DKjv8ZBJ3uWqNUqq4orYq+V8C+vTGKiSPUPNJoa1PJ702mYKQuBq+AStFz+bzQ==;EndpointSuffix=core.windows.net'
CONTAINER_NAME_SRC = 'python'

CONNECTION_STRING_DEST = 'DefaultEndpointsProtocol=https;AccountName=onboardingpractice123;AccountKey=Xb9tXJdV0DeuVl3GU7ptF5wAeokyyCKMZ+Yq4VENnQIw7cLvIm8/JALRIK2brjTSiqTi7O2iIEs/+AStovwC5A==;EndpointSuffix=core.windows.net'
CONTAINER_NAME_DEST = 'destcontainer'
DECODE = 'utf-8'

def read_files_from_container():
    """
    This function decode the content of the blobs on source storage account and copy them to other storage account.
    :return: None
    """
    blob_service_src = BlobServiceClient.from_connection_string(CONNECTION_STRING_SRC)
    container_src = blob_service_src.get_container_client(CONTAINER_NAME_SRC)
    blob_service_dest = BlobServiceClient.from_connection_string(CONNECTION_STRING_DEST)
    container_dest = blob_service_dest.get_container_client(CONTAINER_NAME_DEST)
    blob_list = container_src.list_blobs()
    local_path = "./data"
    os.mkdir(local_path)
    for blob in blob_list:
        blob_client_src = container_src.get_blob_client(blob.name)
        blob_content = blob_client_src.download_blob().readall()
        blob_content = base64.b64decode(blob_content).decode(DECODE)


        local_file_name = blob.name
        upload_file_path = os.path.join(local_path, local_file_name)
        file = open(file=upload_file_path, mode='w')
        file.write(blob_content)
        file.close()

        blob_client_dest = blob_service_dest.get_blob_client(container=CONTAINER_NAME_DEST, blob=local_file_name)

        with open(file=upload_file_path, mode="rb") as data:
            blob_client_dest.upload_blob(data)





