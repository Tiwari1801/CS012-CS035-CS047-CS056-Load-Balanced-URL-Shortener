from flask import Flask, request, redirect
import redis
import hashlib

app = Flask(__name__)
redis_client = redis.Redis(host='redis', port=6379, decode_responses=True)

def shorten_url(long_url):
    hash_obj = hashlib.md5(long_url.encode())
    short_key = hash_obj.hexdigest()[:6]
    redis_client.set(short_key, long_url)
    return short_key

@app.route('/shorten', methods=['POST'])
def shorten():
    long_url = request.json.get('url')
    if not long_url:
        return {"error": "URL is required"}, 400
    short_key = shorten_url(long_url)
    return {"short_url": f"http://localhost:5000/{short_key}"}, 201

@app.route('/<short_key>')
def redirect_url(short_key):
    long_url = redis_client.get(short_key)
    if long_url:
        return redirect(long_url)
    return {"error": "URL not found"}, 404

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
