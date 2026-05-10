import requests
from bs4 import BeautifulSoup
import csv
import json


def save_to_csv(data: dict, filename: str = "books.csv"):
    with open(filename, "w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["category", "title", "price", "availability"])

        for category, books in data.items():
            for book in books:
                writer.writerow([
                    category,
                    book["title"],
                    book["price"],
                    book["availability"]
                ])

    print(f"\nCSV export complete → {filename}")


def save_to_json(data: dict, filename: str = "books.json"):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
    print(f"\nJSON export complete → {filename}")


BASE_URL = "https://books.toscrape.com/"


def fuzzy_match(user_input, categories):
    user_input = user_input.lower().strip()
    # Exact match
    if user_input in (c.lower() for c in categories):
        return user_input

    # Partial match
    for category in categories:
        if user_input in category.lower():
            return category

    return None


def choose_category(categories):
    print("\nAvailable categories:\n")

    category_list = list(categories.keys())
    counts = {}

    # Count books for each category (first page only)
    for name in category_list:
        counts[name] = count_books_in_category(categories[name])

    # Display categories with book counts
    for idx, name in enumerate(category_list, start=1):
        print(f"{idx}. {name} ({counts[name]} books)")

    user_input = input("\nEnter a category number or name: ").strip()

    # If user typed a number
    if user_input.isdigit():
        index = int(user_input) - 1
        if 0 <= index < len(category_list):
            selected = category_list[index]
        else:
            print("Invalid number.")
            return None
    else:
        # Fuzzy match for names
        selected = fuzzy_match(user_input, category_list)
        if not selected:
            print("Category not recognized.")
            return None

    # Prevent selecting empty categories
    if counts[selected] == 0:
        print("\nThis category has 0 books. Please choose another.\n")
        return None

    return selected


def choose_output_format():
    print("\nChoose output format:")
    print("1. JSON")
    print("2. CSV")
    print("3. Preview 5 Results Only (No Export)")

    choice = input("Enter 1, 2, or 3: ").strip()

    if choice == "1":
        return "json"
    if choice == "2":
        return "csv"
    return "none"


def fetch_page(url: str) -> BeautifulSoup:
    response = requests.get(url, timeout=10)
    response.encoding = "utf-8"
    response.raise_for_status()
    return BeautifulSoup(response.text, "html.parser")


def extract_books(soup: BeautifulSoup) -> list:
    books = []
    items = soup.select(".product_pod")

    for item in items:
        title = item.h3.a["title"]
        price = item.select_one(".price_color").text
        availability = item.select_one(".availability").text.strip()

        books.append({
            "title": title,
            "price": price,
            "availability": availability
        })

    return books


def get_categories() -> dict:
    soup = fetch_page(BASE_URL)
    categories = {}

    for cat in soup.select(".side_categories ul li ul li a"):
        name = cat.text.strip()
        link = BASE_URL + cat["href"]
        categories[name] = link

    return categories


def scrape_category(name: str, url: str) -> list:
    print(f"\nScraping category: {name}")
    books = []
    page_number = 1

    while True:
        # Correct handling of page 1 vs page 2+
        if page_number == 1:
            page_url = url  # index.html
        else:
            page_url = url.replace("index.html", f"page-{page_number}.html")

        print(f"  Page {page_number}: {page_url}")

        try:
            soup = fetch_page(page_url)
            page_books = extract_books(soup)

            if not page_books:
                break

            books.extend(page_books)
            page_number += 1

        except requests.exceptions.RequestException:
            break

    print(f"  Total books in '{name}': {len(books)}")
    return books


def scrape_all_categories():
    categories = get_categories()
    all_books = {}

    for name, url in categories.items():
        all_books[name] = scrape_category(name, url)

    return all_books


def count_books_in_category(url):
    """Return the number of books in a category by scraping page 1 only."""
    soup = fetch_page(url)
    books = soup.select("article.product_pod")
    return len(books)


def handle_category_selection(categories):
    selected = None
    while selected is None:
        selected = choose_category(categories)
    return selected


def handle_scrape(selected, categories):
    print(f"\nScraping category: {selected}")
    return {selected: scrape_category(selected, categories[selected])}


def handle_export(fmt, data, selected):
    if fmt == "json":
        filename = f"{selected}.json"
        save_to_json(data, filename)
        print(f"\nExported to {filename}")
    elif fmt == "csv":
        filename = f"{selected}.csv"
        save_to_csv(data, filename)
        print(f"\nExported to {filename}")


def handle_preview_export(fmt, data, selected):
    books = data[selected]
    print(f"\nScraped {len(books)} books from {selected}\n")

    for book in books[:5]:
        print(book)

    if fmt == "none":
        print("\nWould you like to export the full results?")
        print("1. Yes (JSON)")
        print("2. Yes (CSV)")
        print("3. No (Continue)")

        export_choice = input("Enter 1, 2, or 3: ").strip()

        if export_choice == "1":
            handle_export("json", data, selected)
        elif export_choice == "2":
            handle_export("csv", data, selected)


def ask_to_continue():
    print("\nWould you like to scrape another category?")
    print("1. Yes")
    print("2. No (Exit)")
    return input("Enter 1 or 2: ").strip() == "1"


def main():
    print("Scraping available categories...")
    categories = get_categories()

    while True:
        selected = handle_category_selection(categories)
        data = handle_scrape(selected, categories)

        fmt = choose_output_format()
        handle_export(fmt, data, selected)
        handle_preview_export(fmt, data, selected)

        if not ask_to_continue():
            print("\nGoodbye!")
            break


if __name__ == "__main__":
    main()
