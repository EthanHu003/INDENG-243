# INDENG-243 Final Project – Rental Finder

This repository contains the full codebase for a housing recommendation demo site built for UC Berkeley INDENG 243 - Module 3.

The project is structured into three main components:

📁 Project Structure
frontend/
search_map.html
The main frontend HTML file.
Users input queries here (e.g., "Philly big house 2000") and receive housing recommendations as result cards.
A toggleable full-screen map function is included but currently hidden for performance reasons.

berkeley_logo.png
Berkeley logo used in the website header.

backended/
api.py
Flask API backend.
Hosts the /recommend endpoint and connects the frontend to the recommendation model.

model_code.py
Contains the match_houses() function, which calls the trained language model and returns relevant housing results based on natural language input.

Other Files
243_LLM.ipynb
Notebook used to develop and test the large language model (LLM)–based recommendation system.

Preprocessing.ipynb
Notebook for preprocessing the raw housing dataset before model training and filtering.

README.md
This file. Contains documentation and file descriptions.
