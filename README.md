# Currency Converter CLI 🌍💰

A simple Python command-line application that fetches live exchange rates from the National Bank of Uzbekistan (NBU) API. It allows users to check currency rates, convert currencies to UZS, and view all available currencies.

## Features
- Fetches live exchange rates using the NBU API.
- Allows currency conversion from a specified amount to UZS.
- Displays a list of all available currencies with their codes and names.
- Caches exchange rate data locally for offline usage.

## Technologies Used
- **Python**: Core programming language.
- **Requests**: For HTTP requests to fetch live exchange rates.
- **JSON**: For caching data locally.
- **Colorama**: For enhancing terminal UI with colors.

## Why This Project?
As a **Golang developer**, I primarily work on larger projects, but I created this small Python project to revisit the language and remember its fundamentals. It was also a fun way to experiment with Python's libraries like `colorama`.

## How to Run the Project
1. Clone the repository:
   ```bash
   git clone https://github.com/<your-username>/currency-converter-cli.git
   cd currency-converter-cli
   ```
2. Install dependencies:
    ```bash
    pip install requests colorama
    ```
3. Run the project
    ```bash
    python exchange.py
    ```

## Requirements
- **Python 3.7+**
- **Internet connection (for fetching live rates)**
- **Colorama (for colored terminal output)**

## To-Do

- Add support for multi-currency conversion.
- Improve error handling for API connectivity.
- Include tests for core functionality.

## Acknowledgements

- National Bank of Uzbekistan API for providing exchange rate data.
- Python community for amazing libraries like colorama and requests.

## Author

Hi! I'm Javohir, a passionate Golang developer working on big projects. This small Python project was a fun exercise to revisit Python basics. You can find my larger projects on my GitHub and GitLab profile.