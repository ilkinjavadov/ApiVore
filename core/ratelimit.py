import asyncio

RATE_LIMIT_STATUS_CODES = [429]

async def scan(endpoints, client, request_count=10, delay=0.1):
    results = []

    for ep in endpoints:
        path = ep["path"]
        method = ep["method"]

        # ID parametre varsa ilk id ile test ederiz
        url = path.replace("{id}", "1") if "{id}" in path else path

        status_codes = []
        rate_limited = False

        for _ in range(request_count):
            try:
                resp = await client.request(method, url)
                status_codes.append(resp.status_code)
                if resp.status_code in RATE_LIMIT_STATUS_CODES:
                    rate_limited = True
                    break
                await asyncio.sleep(delay)  # isteklere biraz delay ekleyerek spam önle
            except Exception:
                # Hata olursa atla
                continue

        if rate_limited:
            results.append({
                "endpoint": url,
                "method": method,
                "rate_limited": True,
                "status_codes": status_codes
            })

    return results

