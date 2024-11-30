import requests

# Prometheus URL
PROMETHEUS_URL = "http://localhost:9090/api/v1/query"

QUERIES = {
    "cpu_utilization": "100 - (avg(irate(node_cpu_seconds_total{mode='idle'}[5m])) * 100)",
    "memory_utilization": "(1 - (node_memory_MemAvailable_bytes / node_memory_MemTotal_bytes)) * 100",
    "latency": "sum(rate(prometheus_http_request_duration_seconds_sum{instance='localhost:9090'}[5m])) * 1000",
#    "latency": "sum(rate(prometheus_http_request_duration_seconds_sum{instance='localhost:9090'}[$__rate_interval])) * 1000", 
    "request_count": "sum(prometheus_http_requests_total{instance='localhost:9090'})",
    "http_2xx_errors": 'sum(prometheus_http_requests_total{code=~"2..", instance="localhost:9090"})',
    "http_3xx_errors": 'sum(prometheus_http_requests_total{code=~"3..", instance="localhost:9090"})',
    "http_4xx_errors": 'sum(prometheus_http_requests_total{code=~"4..", instance="localhost:9090"})',
    "http_5xx_errors": 'sum(prometheus_http_requests_total{code=~"5..", instance="localhost:9090"})'
}

def fetch_metric(query):
    """
    Fetches a metric value from Prometheus.
    Args:
        query (str): PromQL query to fetch a specific metric.
    Returns:
        float: Metric value if found, else None.
    """
    try:
        response = requests.get(PROMETHEUS_URL, params={'query': query})
        response.raise_for_status()  # Raise HTTPError for bad responses
        data = response.json()

        # Extracting the metric value
        result = data['data']['result']
        if result:
            return float(result[0]['value'][1])  # Return the metric value
        else:
            return None  # No data found for the query
    except Exception as e:
        print(f"Error fetching metric for query '{query}': {e}")
        return None

def main():
    print("Fetching metrics from Prometheus...")

    # Dictionary to store the fetched metric values
    metrics = {}

    # Fetch and store each metric in the dictionary
    for metric_name, query in QUERIES.items():
        value = fetch_metric(query)
        if value is None:
            metrics[metric_name] = 0
        else:
            metrics[metric_name] = value
    
    # Return the metrics dictionary or individual variables
    return metrics

if __name__ == "__main__":
    metrics = main()
    
    # Print the fetched metrics (optional)
    for metric_name, value in metrics.items():
        print(f"{metric_name.replace('_', ' ').capitalize()}: {value}")
    
    # Now, `metrics` dictionary contains all the metrics values and can be imported into another file.