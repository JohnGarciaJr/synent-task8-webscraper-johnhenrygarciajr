# 📘 Task 8 — Web Scraper (Books to Scrape)
### Synent Technologies Python Development Internship  
### Developer: John Henry Garcia Jr

This project is my submission for **Task 8: Web Scraper**, where the objective was to extract structured data from a website using **requests** and **BeautifulSoup**.

I built a fully interactive **Book Category Web Scraper** for the website *Books to Scrape*, featuring category selection, pagination handling, data preview, and export to JSON/CSV.

Link to Video Submission:
[Task 8 — Web Scraper Video](https://www.linkedin.com/posts/johngarciajr83_internship-python-programming-ugcPost-7461168747844849664-nDRh?utm_source=social_share_send&utm_medium=member_desktop_web&rcm=ACoAADaOpwwB33Y0_oTjzePpZVr26EEozGnel7I)
---

## 🚀 Features

### 🔍 Category Scraping
- Automatically loads all book categories from the homepage  
- Displays category names **with book counts**  
- Allows selection by **number or name**  
- Skips empty categories  

### 📄 Pagination Handling
- Detects and loads all pages in a category  
- Scrapes:
  - Title  
  - Price  
  - Availability  

### 💾 Export Options
After scraping, users can choose:

1. **Export to JSON**  
2. **Export to CSV**  
3. **Preview first 5 results only**  

If preview is selected, the user is asked:

> “Would you like to export the full results?”

### 🔁 Looping Workflow
After each scrape, the user can:

- Scrape another category  
- Exit the program cleanly  

### 🧩 Modular Code Structure
The scraper uses helper functions for:

- Category loading  
- Category selection  
- Page scraping  
- Data extraction  
- Exporting  
- Previewing  
- Loop control  

This keeps the code clean, readable, and maintainable.

---

## 🧠 How It Works

### 1. Load Categories
The scraper fetches all categories and displays them like:

```
37. Contemporary (3 books)

38. Spirituality (6 books)
    ...
```


### 2. User Selects a Category
You can enter:

- Category number  
- Category name (case‑insensitive)

### 3. Scraping Begins
The scraper:

- Loads page 1 (`index.html`)
- Loads additional pages (`page-2.html`, `page-3.html`, etc.)
- Extracts:
  - Title  
  - Price  
  - Availability  

### 4. Choose Output Format
```
1. JSON
2. CVS
3. Preview 5 Results Only (No Export)
```


### 5. Optional Export After Preview
If preview is chosen, the user can still export afterward.

### 6. Loop or Exit
The user can scrape another category or exit.

---

## 📄 Example Output (Preview Mode)

```
Scraped 11 books from Philosophy

{'title': "Sophie's World", 'price': '£15.94', 'availability': 'In stock'}
{'title': 'The Death of Humanity...', 'price': '£58.11', 'availability': 'In stock'}
{'title': 'The Stranger', 'price': '£17.44', 'availability': 'In stock'}
{'title': 'Proofs of God...', 'price': '£54.21', 'availability': 'In stock'}
{'title': 'Kierkegaard...', 'price': '£47.13', 'availability': 'In stock'}
```


---

## 🧪 Error Handling
The scraper gracefully handles:

- Network errors  
- Missing pages  
- Invalid category input  
- Empty categories  
- Unexpected HTML changes  

---

## 🧼 Code Quality
This project follows:

- PEP‑8 formatting  
- Modular function design  
- Clear separation of concerns  
- Readable CLI output  

---

## 📚 Dependencies
- `requests`  
- `beautifulsoup4`

---

## 🧩 Project Structure

```
task-8/
│
├── scraper.py          # Main scraper logic
├── README.md           # Documentation (this file)
├── requirements.txt    # Dependencies (requests, beautifulsoup4)
└── exports/            # (Optional) Folder for saved JSON/CSV files
```


---

## 🛠️ Installation

### 1. Install dependencies
```bash
pip install -r requirements.txt
```

### 2. Run the scraper
```
python scraper.py
```

If using a src folder:
```
python src/scraper.py
```

## 🏁 Conclusion
This task demonstrates:

- Web scraping fundamentals

- Pagination handling

- CLI design

- Data export workflows

## 📬 Contact / Updates
This repository will be updated daily as tasks are completed.
Each task folder includes its own documentation and execution notes.

**Developer:** John Henry Garcia Jr  
**Location:** Pearland, Texas  
**Reach me here: jhgarci4@asu.edu
