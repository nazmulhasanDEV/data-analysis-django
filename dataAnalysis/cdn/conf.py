# this part for digital ocean static and media files
import os

AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY")
AWS_STORAGE_BUCKET_NAME = "dj-data-analysis"
AWS_S3_ENDPOINT_URL = "https://nyc3.digitaloceanspaces.com"

AWS_S3_OBJECT_PARAMETERS = {
    "CacheControl": "max-age=86400",
     "ACL": "public-read"
}
AWS_LOCATION = "https://dj-data-analysis.nyc3.digitaloceanspaces.com"

DEFAULT_FILE_STORAGE = "dataAnalysis.cdn.backends.MediaRootS3BotoStorage"
