# INDENG-243 Final Project – Rental Finder

This repository contains the full codebase for a housing recommendation demo site built for **UC Berkeley INDENG 243 – Module 3**.

---

## 📁 Project Structure

### `frontend/`
- **`search_map.html`**  
  The main frontend HTML file.  
  Users can input queries (e.g., `Philly big house 2000`) and receive housing recommendations as result cards.  
  A full-screen map function is included but currently hidden for performance reasons.

- **`berkeley_logo.png`**  
  Berkeley logo displayed in the website header.

---

### `backended/`
- **`api.py`**  
  Flask API backend.  
  Hosts the `/recommend` endpoint and connects the frontend to the recommendation model.

- **`model_code.py`**  
  Contains the `match_houses()` function.  
  This function takes natural language queries and returns matched housing results by calling the trained LLM model.

---

### Root Directory Files
- **`243_LLM.ipynb`**  
  Jupyter Notebook used to build and test the large language model (LLM)–based recommendation system.

- **`Preprocessing.ipynb`**  
  Notebook for cleaning and preprocessing the raw housing dataset before model training.

- **`README.md`**  
  This file. Includes documentation and file descriptions.

---
