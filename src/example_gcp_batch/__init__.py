from google.cloud import batch_v1

def list_jobs(parent: str):
    client = batch_v1.BatchServiceClient()
    request = batch_v1.ListJobsRequest(parent=parent)
    page_result = client.list_jobs(request=request)
    return page_result

def list_filtered_jobs(parent: str):
    client = batch_v1.BatchServiceClient()
    request = batch_v1.ListJobsRequest(parent=parent, filter=f'status.state:FAILED')
    page_result = client.list_jobs(request=request)
    return page_result
