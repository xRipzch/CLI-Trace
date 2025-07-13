import requests

def check_url(url):
    try:
        res = requests.get(url, timeout=5, headers={"User-Agent": "CLITrance"})
        return res.status_code == 200
    except Exception:
        return False
