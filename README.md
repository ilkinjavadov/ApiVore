# apivore 🐊

AI-Powered API Abuse Scanner — IDOR, Rate Limiting & More.

## Features
- 🔍 IDOR (Insecure Direct Object Reference) detection
- 🔁 Rate-limiting bypass testing
- 🧠 (Soon) AI-powered endpoint abuse prediction
- 📄 OpenAPI / Swagger support
- 📤 JSON & HTML output

## Installation

```bash
git clone https://github.com/yourusername/apivore.git
cd apivore
pip install -r requirements.txt
```

## Usage
```bash
python apivore.py --openapi examples/test_api.yaml --bearer "eyJ..." --output output/report.json
```
