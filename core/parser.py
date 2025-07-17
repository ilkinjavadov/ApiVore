import yaml

def load_endpoints(openapi_path):
    with open(openapi_path, 'r') as f:
        try:
            spec = yaml.safe_load(f)
        except yaml.YAMLError as e:
            print(f"[!] YAML parse error: {e}")
            return []

    endpoints = []

    # Swagger/OpenAPI 'paths' alanını tarar
    paths = spec.get("paths", {})
    for path, methods in paths.items():
        for method, details in methods.items():
            endpoints.append({
                "method": method.upper(),
                "path": path,
                "parameters": details.get("parameters", [])
            })

    return endpoints
