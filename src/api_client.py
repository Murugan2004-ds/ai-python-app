import requests

def get_github_user(username):
    url =f"https://api.github.com/users/{username}"
    try:
        response = requests.get(url,timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.RequestsException as e:
        print(f"Request failed: {e}")
        return None