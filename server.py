from flask_cors import CORS
from flask import Flask, request, jsonify, send_file
import requests
import ssl
import socket
from datetime import datetime

app = Flask(__name__)
CORS(app)

def check_ssl(url):
    try:
        context = ssl.create_default_context()
        with socket.create_connection((url, 443)) as sock:
            with context.wrap_socket(sock, server_hostname=url) as ssock:
                cert = ssock.getpeercert()
                issuer = dict(x[0] for x in cert['issuer'])
                expire_date = datetime.strptime(cert['notAfter'], '%b %d %H:%M:%S %Y %Z')
                days_left = (expire_date - datetime.now()).days
                return f"✅ SSL geçerli (Veren: {issuer['organizationName']}, {days_left} gün kaldı)"
    except:
        return "❌ SSL geçersiz veya yok"

def check_https_redirect(url):
    try:
        response = requests.get(f"http://{url}", timeout=5, allow_redirects=True)
        if response.url.startswith("https://"):
            return "✅ HTTPS'e zorluyor"
        else:
            return "❌ Güvensiz (HTTP)"
    except:
        return "⚠️ Bağlantı hatası"

@app.route('/')
def home():
    return send_file('index.html')

@app.route('/scan')
def scan():
    url = request.args.get('url')
    return jsonify({
        "ssl": check_ssl(url),
        "https": check_https_redirect(url)
    })

if __name__ == '__main__':
    app.run()
