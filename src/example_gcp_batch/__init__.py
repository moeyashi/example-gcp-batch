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

def list_finished_jobs(parent: str):
    client = batch_v1.BatchServiceClient()
    # NG filter examples
    # status.state:SUCCEEDED|FAILED # invalid list filter: Invalid literal \'SUCCEEDED|FAILED\' for \'resource.status.state\'.
    # status.state ~ SUCCEEDED|FAILED # invalid list filter: Invalid filter syntax: syntax error at line 1, column 13, token \'~\'
    # status.state = "(SUCCEEDED,FAILED)" # invalid list filter: Invalid literal \'(SUCCEEDED,FAILED)\' for \'resource.status.state\'
    # status.state = ("SUCCEEDED","FAILED") # invalid list filter: Invalid filter syntax: syntax error at line 1, column 27, token \',\'
    # status.state = ("SUCCEEDED"\,"FAILED") # invalid list filter: Invalid filter syntax: syntax error at line 1, column 16, token \'\"SUCCEEDED\"\'
    request = batch_v1.ListJobsRequest(parent=parent, filter='status.state = "SUCCEEDED" OR status.state = "FAILED"')
    page_result = client.list_jobs(request=request)
    return page_result
