# AI Web-Scraper

An interactive web application for scraping website content and extracting specific information using AI (Ollama LLM).

## Features

- Scrape any website’s DOM content using Selenium
- Clean and process scraped HTML with BeautifulSoup
- Split large DOM content into manageable chunks
- Use AI (Ollama LLM via LangChain) to extract information based on user prompts
- Easy to use Streamlit UI

## Installation

1. Clone this repository.
2. Install dependencies:
    ```sh
    pip install -r requirements.txt
    ```
3. Download ChromeDriver and place it in the project root as `chromedriver.exe`.
4. Download version of llm you want to use using ollama in parse change LLM model e.g. `model = OllamaLLM(model="llama3.2")`

## Requirements

- Python 3.8+
- Up to date ChromeDriver based on Chrome-version on system
- All Python dependencies in requirements.txt
- Ensure ChromeDriver matches your installed Chrome version.
- Ollama must be running locally for parsing to work.



## Run it locally

Run the Streamlit app:

```sh
streamlit run main.py
```

1. Enter the URL of the site you want to scrape.
2. View and inspect the cleaned DOM content.
3. Describe what information you want parsed.
4. Click "Parse Content" to extract information using AI.

