# 📘 README.md — Apivore: AI Powered API Abuse Scanner

---

## Apivore


<p align="center">
  <img src="/examples/apivore.png" alt="ApiVore Logo" width="250" />
</p>

Apivore is an advanced, modular API abuse scanner enhanced with AI support for API security testing.  
It automatically tests APIs based on OpenAPI/Swagger specifications, detecting IDOR vulnerabilities, rate limiting issues, and provides AI-powered analysis.

---

## Features

- Supports OpenAPI 3.x / Swagger 2.0 parsing  
- Multiple authentication methods (Bearer, Basic, None)  
- Advanced IDOR testing (content comparison with different IDs, sensitive data detection)  
- Rate limit testing (checks for 429 status codes, Retry-After headers)  
- AI-powered analysis (using OpenAI GPT-4 mini model)  
- JSON and HTML report generation  
- Asynchronous HTTP requests (powered by httpx)  
- Colorful CLI output with rich

---

## Installation

1. Clone the repository:
```bash
git clone https://github.com/username/apivore.git
cd apivore
```


## Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```
## Install dependencies:
```bash
pip install -r requirements.txt
```

## Add your OpenAI API key to a .env file:
```bash
OPENAI_API_KEY=sk-XXXXXXXXXXXXXXXXXXXXXXXXXXXX
```

## Usage
```bash
python apivore.py --openapi examples/test_api.yaml --auth-type bearer --auth-token <token> --output output/report.json --enable-ai
```
## Development
- Python 3.11+ recommended

- Use pytest for testing

- New modules can be easily added; architecture is async-based

MIT Licensed 
All rights Reserved - Ilkin Javadov

