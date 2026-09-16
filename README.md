# fashion-recommendation-system
 

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

 ## Dataset

This project uses the **Fashion Product Images Dataset** by Param Aggarwal, available on Kaggle.

**Dataset Source:**
https://www.kaggle.com/datasets/paramaggarwal/fashion-product-images-dataset

### Dataset Information

* 44,000+ fashion product images
* Product metadata including category, sub-category, gender, color, season, and usage
* Images sourced from the Myntra fashion catalog
* Suitable for image classification, visual similarity search, recommendation systems, and fashion analytics projects.

### Dataset Setup

1. Download the dataset from Kaggle.
2. Extract the downloaded files.
3. Place the dataset inside the project directory:

```text
images/
└── myntradataset/
    ├── images/
    └── styles.csv
```

**Note:** The dataset is not included in this repository because of its large size.


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
