import asyncio
import json
from deepdiff import DeepDiff

SENSITIVE_KEYS = ['email', 'username', 'phone', 'ssn', 'role', 'is_admin', 'password']

async def fetch_response(client, method, url):
    try:
        resp = await client.request(method, url)
        text = await resp.aread()
        try:
            return resp.status_code, json.loads(text)
        except:
            return resp.status_code, text.decode(errors='ignore')
    except Exception as e:
        return None, None

def contains_sensitive_fields(data):
    if not isinstance(data, dict):
        return False
    for key in data.keys():
        if any(s in key.lower() for s in SENSITIVE_KEYS):
            return True
    return False

async def scan(endpoints, client):
    results = []

    for ep in endpoints:
        path = ep["path"]
        method = ep["method"]

        if "{id}" not in path:
            continue

        baseline_id = 1
        baseline_url = path.replace("{id}", str(baseline_id))
        status, baseline_data = await fetch_response(client, method, baseline_url)
        if status != 200 or baseline_data is None:
            continue

        for test_id in range(2, 6):
            test_url = path.replace("{id}", str(test_id))
            status, test_data = await fetch_response(client, method, test_url)
            if status != 200 or test_data is None:
                continue

            diff = DeepDiff(baseline_data, test_data, ignore_order=True)
            if diff:
                sensitive = contains_sensitive_fields(test_data)
                results.append({
                    "endpoint": test_url,
                    "method": method,
                    "diff": diff.to_dict(),
                    "sensitive_fields_detected": sensitive
                })

    return results

