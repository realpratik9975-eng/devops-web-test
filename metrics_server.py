from http.server import BaseHTTPRequestHandler, HTTPServer

PORT = 8000
LOG_FILE = "access.log"


def get_metrics():

    total_requests = 0
    successful_requests = 0
    not_found_requests = 0

    with open(LOG_FILE, "r") as file:

        for line in file:

            if '"GET ' in line:

                total_requests += 1

                if '" 200 ' in line:
                    successful_requests += 1

                elif '" 404 ' in line:
                    not_found_requests += 1

    metrics = f"""# HELP http_requests_total Total HTTP requests
# TYPE http_requests_total counter
http_requests_total{{status="200"}} {successful_requests}
http_requests_total{{status="404"}} {not_found_requests}
"""

    return metrics


class MetricsHandler(BaseHTTPRequestHandler):

    def do_GET(self):

        if self.path == "/metrics":

            metrics = get_metrics()

            self.send_response(200)
            self.send_header(
                "Content-Type",
                "text/plain; version=0.0.4"
            )
            self.send_header(
                "Content-Length",
                str(len(metrics))
            )
            self.end_headers()

            self.wfile.write(metrics.encode())

        else:

            self.send_response(404)
            self.end_headers()


server = HTTPServer(("0.0.0.0", PORT), MetricsHandler)

print(f"Metrics server running on port {PORT}")

server.serve_forever()
