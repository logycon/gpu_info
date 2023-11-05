## GPU Info 

Outputs GPU Info in JSON format

```bash
gpu_info | jq
```

```json
[
  {
    "gpu": 1,
    "name": "NVIDIA GeForce RTX 3070 Ti Laptop GPU",
    "memory": {
      "used_mb": 149.0,
      "total_mb": 8192.0
    }
  }
]

```

### Build

```bash
make build
```