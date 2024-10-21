
# Fatrace Exporter for Prometheus

[Fatrace](https://github.com/martinpitt/fatrace) data exporter to be used with [Prometheus](https://prometheus.io/).

The exporter exposes two metrics:
- file_access_total - cumulative file access events
- file_access_current - instant file access events

These metrics are exposed in port `8123`




## Standalone

Install prometheus_client 
```sh
pip install prometheus_client
```

Run exporter in target directory for monitoring
```sh
cd /target/directory && sudo python exporter.py
```

## Docker
Build docker image
```sh
docker build -t fatrace-exporter:latest .
```

Replace `${TARGET_DIRECTORY}` in `docker-compose.yml` with the path for the target directory to monitor.

Run docker compose
```sh
docker compose up -d
```





## Acknowledgements

- [MartinPitt](https://github.com/martinpitt) for implementing fatrace
