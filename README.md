#  Website Scraper

> **Cybersecurity Project — Information Assurance and Security**

A simple client-server web application designed for adaptive web data extraction. It enables users to enter a public website URL, select the types of content to extract (such as headings, links, images, paragraphs, or metadata), and export the collected data in CSV, JSON, or Excel formats.


## Table of Contents

- [Overview](#overview)
- [Project Structure](#project-structure)
- [Tech Stack](#tech-stack)
- [Getting Started](#getting-started)
- [How to Use](#how-to-use)

---

## Overview

This tool allows users to:

- Paste any public URL and select which data fields to extract (headings, links, paragraphs, images, etc.)
- Automatically check the site's `robots.txt` before scraping — if blocked, the tool stops
- Apply rate limiting to avoid overloading servers
- Download results as **CSV**, **JSON**, or **Excel**

---

## Project Structure

```
webscraper/
├── app.py                  
├── requirements.txt        
├── scraper/
│   ├── __init__.py         
│   └── scraper.py          
├── templates/
│   └── index.html         
└── output/                 
```

## Getting Started

### Prerequisites

- Python **3.9 or higher**

Check your version:
```bash
python --version
```

If needed, download Python from [https://python.org](https://python.org).

### Installation

**1. Clone or extract the project**
```bash
cd path/to/webscraper
```

**2. Install dependencies**
```bash
pip install -r requirements.txt
```

**3. Start the server**
```bash
python app.py
```

**4. Open the interface**

Go to [http://127.0.0.1:5000](http://127.0.0.1:5000) in your browser.

---

## How to Use

1. **Paste a URL** into the input field (e.g. `https://books.toscrape.com`)
2. **Select data fields** — check the boxes for what you want to extract
3. **Choose an output format** — CSV, JSON, or Excel
4. **Click RUN SCRAPER**

The interface will display:
- Whether `robots.txt` allowed or blocked the scrape
- Number of records extracted
- Any warnings or errors encountered
- A **Download** button for your output file

---



