# create new VM

import google.cloud.compute_v1 as compute_v1

def print_images_list(project: str) -> str:
    """
    Prints a list of all non-deprecated image names available in given project.

    Args:
        project: project ID or project number of the Cloud project you want to list images from.

    Returns:
        The output as a string.
    """
    images_client = compute_v1.ImagesClient()
    # Listing only non-deprecated images to reduce the size of the reply.
    images_list_request = compute_v1.ListImagesRequest(
        project=project, max_results=100, filter="deprecated.state != DEPRECATED"
    )
    output = []

    # Although the `max_results` parameter is specified in the request, the iterable returned
    # by the `list()` method hides the pagination mechanic. The library makes multiple
    # requests to the API for you, so you can simply iterate over all the images.
    for img in images_client.list(request=images_list_request):
        print(f" -  {img.name}")
        output.append(f" -  {img.name}")
    return "\n".join(output)

# create new bucket
# Using the client library

# Imports the Google Cloud client library
from google.cloud import storage

# Instantiates a client
storage_client = storage.Client()

# The name for the new bucket
bucket_name = "my-new-bucket"

# Creates the new bucket
bucket = storage_client.create_bucket(bucket_name)

print(f"Bucket {bucket.name} created.")

# create new bucket

from google.cloud import storage


def create_bucket_class_location(bucket_name):
    """
    Create a new bucket in the US region with the coldline storage
    class
    """
    # bucket_name = "your-new-bucket-name"

    storage_client = storage.Client()

    bucket = storage_client.bucket(bucket_name)
    bucket.storage_class = "COLDLINE"
    new_bucket = storage_client.create_bucket(bucket, location="us")

    print(
        "Created bucket {} in {} with storage class {}".format(
            new_bucket.name, new_bucket.location, new_bucket.storage_class
        )
    )
    return new_bucket

# Upload an object to a bucket













