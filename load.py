from azure.identity import DefaultAzureCredential
from azure.storage.blob import BlobServiceClient

ACCOUNT_NAME = "ethans1124etl"
CONTAINER = "output"

credential = DefaultAzureCredential()

service = BlobServiceClient(
    account_url=f"https://{ACCOUNT_NAME}.blob.core.windows.net",
    credential=credential
)

blob = service.get_blob_client(
    container=CONTAINER,
    blob="employee_transformed.csv"
)

with open("/home/azureuser/ethans-1124/output/employee_transformed.csv", "rb") as data:
    blob.upload_blob(
        data,
        overwrite=True
    )

print("Transformed file uploaded successfully.")
