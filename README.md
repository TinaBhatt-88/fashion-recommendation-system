# fashion-recommendation-system
# AI Fashion Recommendation System

An AI-powered Fashion Recommendation System that finds visually similar fashion products using OpenCLIP embeddings and FAISS similarity search.

## Features

- Upload a fashion image
- Extract image features using OpenCLIP
- Fast similarity search using FAISS
- Display top similar fashion products
- Modern web interface using FastAPI, HTML, CSS, and JavaScript

## Tech Stack

- Python
- FastAPI
- OpenCLIP
- FAISS
- NumPy
- Pillow
- HTML
- CSS
- JavaScript

## Project Structure

```
Fashion Recommendation System/
│
├── app.py
├── search_engine.py
├── create_embeddings.py
├── build_faiss_index.py
│
├── static/
│   ├── style.css
│   └── script.js
│
├── templates/
│   └── index.html
│
├── images/
├── uploads/
│
└── README.md
```

## How It Works

1. Upload a fashion image.
2. OpenCLIP extracts image embeddings.
3. FAISS searches for similar embeddings.
4. The system returns visually similar fashion products.

## Installation

```bash
pip install -r requirements.txt
```

## Run the Project

```bash
uvicorn app:app --reload
```

Open:

```
http://127.0.0.1:8000
```

## Dataset

The project uses the Myntra Fashion Dataset.

Note: The dataset is not included in this repository because of its large size.

## Future Improvements

- FashionCLIP integration
- Text-based search
- Category filtering
- Brand filtering
- Color filtering
- React frontend
- Cloud deployment

## Author

Tina Bhatt
B.Sc. Data Science
