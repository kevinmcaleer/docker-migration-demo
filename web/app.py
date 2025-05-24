from flask import Flask
import redis
import os

app = Flask(__name__)
redis_host = os.getenv("REDIS_HOST", "localhost")
r = redis.Redis(host=redis_host, port=6379, decode_responses=True)

@app.route("/")
def hello():
    r.incr("hits")
    count = r.get("hits")
    return f"Hello from Podman! This page has been viewed {count} times."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
