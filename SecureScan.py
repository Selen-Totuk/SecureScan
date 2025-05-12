# SecureScan.py

import requests
import ssl
import socket
from datetime import datetime

def check_ssl(url):
    try:
        context = ssl.create_default_context()
        with socket.create_connection((url, 443), timeout=5) as sock:
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

def scan_website(url):
    print(f"\n🌐 {url} tarandı:")
    print("-" * 30)
    print("SSL Sertifikası:", check_ssl(url))
    print("HTTP/HTTPS:", check_https_redirect(url))

if __name__ == "__main__":
    website = input("Tarayacağınız site (örnek: google.com): ")
    scan_website(website)
