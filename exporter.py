from prometheus_client import start_http_server, Counter, Gauge
import subprocess
import threading
import re
import time

# Define Prometheus metrics
file_access_counter = Counter('file_access_total', 'Total number of file access events', ['process', 'operation', 'path'])
file_access_gauge = Gauge('file_access_current', 'Current number of file access events', ['process', 'operation', 'path'])

# Regex pattern to parse fatrace output
fatrace_pattern = re.compile(r"(\w+)\((\d+)\): (\w+) (.+)")

def parse_fatrace_line(line):
    match = fatrace_pattern.match(line)
    if match:
       return match.groups()
    return None

def reset_gauge():
    while True:
        # Reset the gauge to 0 every 15 seconds
        time.sleep(15)
        file_access_gauge.clear()

def run_fatrace():
    # Run fatrace command
    proc = subprocess.Popen(['fatrace', '--current-mount'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    for line in proc.stdout:

        res = parse_fatrace_line(line)
        if res:
            process, pid, operation, path = res
            # Update Prometheus metrics
            file_access_counter.labels(process=process, operation=operation, path=path).inc()
            file_access_gauge.labels(process=process, operation=operation, path=path).inc()

if __name__ == '__main__':
    # Start the Prometheus metrics server
    start_http_server(8123)

    # Run fatrace in a separate thread
    fatrace_thread = threading.Thread(target=run_fatrace)
    fatrace_thread.daemon = True
    fatrace_thread.start()

    # Reset gauge periodically in a separate thread
    reset_thread = threading.Thread(target=reset_gauge)
    reset_thread.daemon = True
    reset_thread.start()

    # Keep the main thread running
    fatrace_thread.join()
    reset_thread.join()