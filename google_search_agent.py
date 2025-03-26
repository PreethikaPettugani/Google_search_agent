import requests
class GoogleSearchAgent:
    def __init__(self, api_key, cse_id):
        self.api_key = api_key
        self.cse_id = cse_id
        self.base_url = "https://www.googleapis.com/customsearch/v1"

    def search(self, query, num_results=5):
        """
        Perform a search using the Google Search API.
        Args:
        - query (str): The search query.
        - num_results (int): Number of results to fetch (max 10 per request).
        Returns:
        - List of search results with titles, links, and descriptions.
        """
        params = {
            "q": query,
            "key": self.api_key,
            "cx": self.cse_id,
            "num": num_results
        }
        response = requests.get(self.base_url, params=params)
        if response.status_code == 200:
            results = response.json().get("items", [])
            search_results = [
                {
                    "title": item.get("title", "No Title"),
                    "link": item.get("link", "No Link"),
                    "description": item.get("snippet", "No Description")
                }
                for item in results
            ]
            return search_results
        else:
            raise Exception(f"Error: {response.status_code} - {response.text}")

# Example usage:
if __name__ == "__main__":
    api_key = "Your api key"
    cse_id = "your cse id"
    agent = GoogleSearchAgent(api_key, cse_id)
    query = "Deloitte"
    try:
        results = agent.search(query)
        for idx, result in enumerate(results,1):
            print(f"{idx}. {result['title']} - {result['link']}")
            print(f"Description: {result['description']}\n")
    except Exception as e:
        print(e)