# BrandMind AI

**On-Device Marketing & Creative Intelligence**

BrandMind AI is a prototype AI marketing assistant designed for Snapdragon-powered HP PCs. It is intended to analyze brand assets and marketing creatives, then provide actionable content and campaign recommendations.

## Challenge
Snapdragon® AI Lab Build & Present Challenge — Qualcomm

## Core Modules
- Brand Profile
- Creative Doctor
- Marketing Copilot
- Campaign Builder
- On-device AI model integration (planned/experimental)

## Proposed AI Stack
- Python / Flask
- React or HTML/CSS/JavaScript UI
- ONNX Runtime
- Qualcomm AI Hub models
- Open-source vision/NLP models
- SQLite for local prototype data

## Repository Structure
```text
brandmind-ai/
├── app/
│   ├── __init__.py
│   └── routes.py
├── static/
│   ├── css/style.css
│   └── js/app.js
├── templates/
│   └── index.html
├── requirements.txt
├── .gitignore
└── README.md
```

## Run Locally
```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
pip install -r requirements.txt
python -m app
```

Open `http://127.0.0.1:5000`.

## Important
The current repository is a functional UI/API prototype. Qualcomm AI Hub and Snapdragon-specific model deployment should be added after selecting and benchmarking compatible models on the target Snapdragon hardware.
