# Website Scraper — Launch Guide
**Cybersecurity Project · Information Assurance and Security · TBS 2025/2026**

---

## What's in this project?

```
webscraper/
├── app.py                  ← Flask server (launches the interface)
├── requirements.txt        ← Python libraries to install
├── scraper/
│   └── scraper.py          ← Core scraping engine (all the logic)
├── templates/
│   └── index.html          ← Web interface (runs in your browser)
└── output/                 ← Your scraped files appear here
```

---

## Step 1 — Make sure Python is installed

Open a terminal (Command Prompt on Windows, Terminal on Mac/Linux) and type:

```
python --version
```

You need **Python 3.9 or higher**. If you don't have it, download it from https://python.org.

---

## Step 2 — Install the required libraries

In the terminal, go to the project folder:

```
cd path/to/webscraper
```

Then install dependencies:

```
pip install -r requirements.txt
```

This installs: Flask (web server), requests (HTTP fetcher), BeautifulSoup (HTML parser), openpyxl (Excel export).

---

## Step 3 — Launch the application

```
python app.py
```

You should see:

```
==================================================
  Website Scraper – Starting...
  Open your browser at: http://127.0.0.1:5000
==================================================
```

---

## Step 4 — Use the interface

Open your browser and go to: **http://127.0.0.1:5000**

**How to scrape a website:**

1. **Paste a URL** — e.g. `https://books.toscrape.com`
2. **Select data fields** — pick what you want: headings, links, paragraphs, etc.
3. **Choose output format** — CSV, JSON, or Excel
4. **Click RUN SCRAPER**

The interface will show you:
- Whether the site's robots.txt allows scraping
- How many records were found
- A download button for your file

---

## What the security checks do

| Check | What happens |
|---|---|
| **robots.txt** | Before scraping, the tool checks if the site allows it |
| **Rate Limiting** | A delay (1–3 seconds) is added between requests |
| **TLS Verification** | HTTPS connections are always verified (no fake certificates) |
| **User-Agent Rotation** | Mimics a real browser to avoid simple bot detection |

If robots.txt blocks access, the scraper **stops** and does not proceed.

---

## Good sites to test on

These sites are designed for scraping practice:

- `https://books.toscrape.com` — book titles and info
- `https://quotes.toscrape.com` — quotes and authors
- `https://example.com` — simple test page

---

## Troubleshooting

**"ModuleNotFoundError"** → Run `pip install -r requirements.txt` again

**"Address already in use"** → Change the port in app.py: `app.run(port=5001)`

**"0 records extracted"** → The page may use JavaScript to load content (dynamic page). Try a simpler static site.

**robots.txt blocks the URL** → The site does not allow scraping. Choose a different URL.

---

## How the pipeline works (simplified)

```
Your input (URL + fields)
        ↓
  Check robots.txt  ← STOP if blocked
        ↓
   Wait (rate limit)
        ↓
   Fetch HTML page
        ↓
   Parse HTML (DOM)
        ↓
   Extract fields
        ↓
   Clean the data
        ↓
 Save to CSV/JSON/Excel
        ↓
     Download ✓
```

---

*Team: Farah Haddad · Mariem Maddouri · Zeineb Jaghmoun · Mayssa Ben Youssef · Mariem Soltani*
