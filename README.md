# AI Python App

A small Python project that loads a text file, cleans it, calls the GitHub API, and saves the combined result as JSON.

## What it covers
- Functions and modules
- OOP (a `Document` class)
- Error handling with try/except
- Saving and loading JSON
- Calling a web API with `requests`
- Git and GitHub

## How to run
```bash
git clone https://github.com/Murugan2004-ds/ai-python-app.git
cd ai-python-app
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python -m src.main
```

## Project structure
- `src/utils.py`: text cleaning
- `src/document.py`: Document class
- `src/loader.py`: file loading with error handling
- `src/storage.py`: JSON save and load
- `src/api_client.py`: GitHub API client
- `src/main.py`: runs everything together