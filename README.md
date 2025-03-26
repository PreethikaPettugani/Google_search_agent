# Google Search Agent

## Description
Google Search Agent is a Python-based script that interacts with the Google Custom Search API to fetch search results programmatically. It allows users to perform web searches and retrieve relevant results, including titles, links, and descriptions.

## Features
- Perform Google searches using the Custom Search API.
- Retrieve search results with titles, links, and descriptions.
- Fetch up to 10 results per request.
- Handle API responses and errors gracefully.

## Prerequisites
To use this script, you need:
- A Google Cloud account.
- A Google Custom Search Engine (CSE) ID.
- An API key from Google Cloud.

## Installation
1. Clone this repository:
   ```sh
   git clone https://github.com/yourusername/google-search-agent.git
   cd google-search-agent
   ```
2. Install dependencies:
   ```sh
   pip install requests
   ```

## Usage
1. Replace the placeholders in the script with your API key and CSE ID:
   ```python
   api_key = "Your API Key"
   cse_id = "Your CSE ID"
   ```
2. Run the script:
   ```sh
   python google_search_agent.py
   ```
3. Modify the `query` variable in the script to search for specific terms:
   ```python
   query = "Deloitte"
   ```

## Example Output
```
1. Deloitte - https://www2.deloitte.com/
   Description: Deloitte provides industry-leading audit, consulting, tax, and advisory services.

2. Deloitte Careers - https://www2.deloitte.com/global/en/careers.html
   Description: Explore Deloitte career opportunities worldwide.
```


