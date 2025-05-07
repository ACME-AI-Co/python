import os
import time
from acme_ai_sdk import AcmeAISDK

client = AcmeAISDK(
    bearer_token=os.environ.get("ACME_AI_SDK_BEARER_TOKEN")  # This is the default and can be omitted
)

with open("birds.csv", "x") as f:
    file = client.files.file_create(file=f)

while True:
    # loop through files to see which one matches our file
    files = client.files.fileslist()
    found = next((f for f in files.files if f.file_id = file.file_id), None)
    if found and found.status == "completed":
        break
    time.sleep(500)

    search_results = client.files.file_search(
        file_id=file.file_id,
        query="chickadee"
    )

    print(search_results)
