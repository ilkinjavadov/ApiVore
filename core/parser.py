import yaml
import json
from typing import List, Dict, Any
from pathlib import Path

def load_spec(file_path: str) -> Dict[str, Any]:
    path = Path(file_path)
    content = path.read_text(encoding="utf-8")
    try:
        if path.suffix in [".yaml", ".yml"]:
            spec = yaml.safe_load(content)
        elif path.suffix == ".json":
            spec = json.loads(content)
        else:
            raise ValueError("Unsupported file extension. Use .yaml, .yml or .json")
    except Exception as e:
        print(f"[!] Failed to parse spec file: {e}")
        return {}
    return spec

def extract_endpoints(spec: Dict[str, Any]) -> List[Dict[str, Any]]:
    endpoints = []
    paths = spec.get("paths", {})

    for path, methods in paths.items():
        for method, details in methods.items():
            if method.lower() not in ["get", "post", "put", "patch", "delete", "options", "head"]:
                continue
            endpoint = {
                "path": path,
                "method": method.upper(),
                "summary": details.get("summary", ""),
                "parameters": details.get("parameters", []),
                "requestBody": details.get("requestBody", {}),
                "responses": details.get("responses", {}),
            }
            endpoints.append(endpoint)
    return endpoints

def load_endpoints(file_path: str) -> List[Dict[str, Any]]:
    spec = load_spec(file_path)
    if not spec:
        return []
    return extract_endpoints(spec)
