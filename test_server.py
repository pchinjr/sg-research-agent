import requests

print(
    requests.post(
        "https://sg-research-agent.onrender.com",
        json={
            "query": "What is meta's new product Thread?"
        }
    ).json()
)