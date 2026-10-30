import json
import os
from pathlib import Path
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer


os.environ.setdefault(
    "ONNX_MODEL_PATH",
    str(Path(__file__).resolve().parent / "models" / "pretrained_model.onnx"),
)

from app_lambda import lambda_handler


class LocalBackendHandler(BaseHTTPRequestHandler):
    def _send_json(self, status_code, payload):
        body = json.dumps(payload).encode("utf-8")
        self.send_response(status_code)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.end_headers()
        self.wfile.write(body)

    def do_OPTIONS(self):
        self.send_response(204)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.end_headers()

    def do_POST(self):
        content_length = int(self.headers.get("Content-Length", "0"))
        body = self.rfile.read(content_length).decode("utf-8")

        event = {
            "body": body,
            "isBase64Encoded": False,
        }

        response = lambda_handler(event, None)
        status_code = response.get("statusCode", 500)
        response_body = response.get("body", "{}")

        try:
            payload = json.loads(response_body)
        except json.JSONDecodeError:
            payload = {"error": response_body}

        self._send_json(status_code, payload)

    def log_message(self, format, *args):
        return


def main():
    server = ThreadingHTTPServer(("127.0.0.1", 8000), LocalBackendHandler)
    print("Local backend running at http://127.0.0.1:8000")
    server.serve_forever()


if __name__ == "__main__":
    main()