# example-gcp-batch

GCP Batch サービスについてのサンプルコードです。

## sample

```
rye sync
rye run python -c "from src.example_gcp_batch import list_filtered_jobs; l = list_filtered_jobs('your parent'); print([i.name for i in l])"
```
