# clitrance/modules/user.py
from utils.http import check_url

def run(username):
    targets = {
        "GitHub": f"https://github.com/{username}",
        "Reddit": f"https://www.reddit.com/user/{username}",
        "Twitter": f"https://twitter.com/{username}",
        "Instagram": f"https://www.instagram.com/{username}",
        "Facebook": f"https://www.facebook.com/{username}",
        "LinkedIn": f"https://www.linkedin.com/in/{username}",
    }

    print(f"\n[+] Searching for: {username}\n")
    for platform, url in targets.items():
        found = check_url(url)
        status = "✅ FOUND" if found else "❌ Not found"
        print(f"{platform:10s} : {status}")

