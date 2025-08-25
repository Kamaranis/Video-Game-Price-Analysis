# Web Scraping & Analysis of Video Game Revaluation Potential

## 📄 Project Goal

This project is a comprehensive data engineering initiative designed to create a unique dataset for analyzing the economic value and appreciation potential of video games. The primary objective was to build a robust, ethical, and efficient web scraping pipeline to extract pricing data from `PriceCharting.com` for the Xbox One and Xbox Series X platforms.

The final output is not just a script, but a structured, clean, and publicly available dataset published on Zenodo, ready for economic analysis, trend prediction, and data visualization.

## ✨ A Methodical & Ethical Engineering Workflow

This project was executed following a rigorous, multi-stage process that mirrors professional data engineering practices, emphasizing strategy and ethics over brute-force extraction.

### Stage 1: Feasibility Study and Source Vetting

Before writing a single line of code, a thorough evaluation of potential data sources was conducted.
*   **Source Analysis:** Multiple sites (e.g., VGChartz, SteamDB, PriceCharting) were initially considered.
*   **Technical & Ethical Vetting:** Each site was evaluated for technical scraping feasibility (static vs. dynamic content, use of AJAX/PHP) and ethical/legal constraints through a careful analysis of their `robots.txt` files.
*   **Source Selection:** `PriceCharting.com` was chosen for its relevant data and clear (though challenging) structure. This initial research phase ensured the project was viable and respectful of the source's infrastructure.

### Stage 2: Solving the Dynamic Content Challenge

The main technical challenge was that `PriceCharting.com` uses "lazy loading" (or infinite scroll) to load product data dynamically via JavaScript. A simple HTML request would not capture the full dataset.
*   **Network Analysis:** Using browser Dev Tools, the XHR (XMLHttpRequest) requests sent by the frontend were identified and analyzed.
*   **Request Simulation:** The final scraper does not brute-force the website. Instead, it simulates these JSON requests by iteratively calling the backend endpoint with the correct parameters (`cursor`, `format`, etc.).
*   **Robust Implementation:** The solution was implemented using the `requests-html` library in Python to efficiently manage sessions and parse the JSON responses, making the extraction process clean and highly efficient.

### Stage 3: Ethical Scraping & Final Dataset Creation

The project was designed with a strong emphasis on ethical best practices.
*   **Rate Limiting:** The script incorporates delays between requests to avoid overloading the server.
*   **Compliance:** The scraper operates within the rules defined in the site's `robots.txt` and terms of use.
*   **Data Publication:** The final, cleaned dataset of **2,369 video games** was structured and published on **Zenodo** under a CC0 (Public Domain) license, promoting open access for academic and research purposes.

## 📊 The Dataset

The resulting dataset (`videojuegos_xbox.csv`) contains the following features:
*   `ID`: Unique product identifier from PriceCharting.
*   `Título`: The name of the video game.
*   `Loose_Price`, `CIB_Price`, `New_Price`: Prices for the game in different conditions (loose, complete in box, new).
*   `Plataforma`: The console platform (Xbox One or Xbox Series X).

**DOI:** The dataset is formally published and citable via Zenodo: **[https://doi.org/10.5281/zenodo.14043146](https://doi.org/10.5281/zenodo.14043146)**

## 💻 Technologies Used

*   **Language:** Python 3
*   **Core Libraries:**
    *   **`requests-html`**: For handling dynamic content and JavaScript-heavy sites.
    *   **`BeautifulSoup4`**: For initial HTML parsing and link discovery.
    *   **Pandas**: For data structuring, cleaning, and final CSV generation.

## 🚀 Getting Started

The repository contains the full Python script and a detailed memo outlining the entire process.
1.  **Clone the repository.**
2.  Install the necessary libraries: `pandas`, `requests-html`, `beautifulsoup4`.
3.  Examine the `link_crawler` and `download_pc` functions to understand the two-stage process of link discovery and data extraction.

## 👤 Author

**Antonio Barrera Mora**

*   **LinkedIn:** https://www.linkedin.com/in/anbamo/
*   **GitHub:** @Kamaranis