
# Fatrace Exporter for Prometheus

[Fatrace](https://github.com/martinpitt/fatrace) data exporter to be used with [Prometheus](https://prometheus.io/).

The exporter exposes two metrics:
- file_access_total - cumulative file access events
- file_access_current - instant file access events

These metrics are exposed in port `8123`

## Docker

Replace `${TARGET_DIRECTORY}` in `docker-compose.yml` with the path for the target directory to monitor.

Run docker compose
```sh
docker compose up -d
```

Build docker image (for custom implementation)
```sh
docker build .
```

## Standalone

Install `prometheus_client` python package
```sh
pip install prometheus_client
```

Run exporter in target directory for monitoring
```sh
cd /target/directory && sudo python exporter.py
```


## Acknowledgements

- [MartinPitt](https://github.com/martinpitt) for implementing fatrace
