import requests
import logging
from typing import List, Dict

logger = logging.getLogger(__name__)  # Added logger


class WebSearch:
    def _parse_results(self, data: dict) -> List[Dict]:  # Added method
        return [
            {
                "title": result.get("Text", ""),
                "url": result.get("FirstURL", ""),
                "content": result.get("Abstract", ""),
            }
            for result in data.get("Results", [])
        ]

    def search(self, query: str) -> List[Dict]:
        try:
            response = requests.get(
                "https://api.duckduckgo.com/",
                params={"q": query, "format": "json", "no_html": 1, "no_redirect": 1},
            )
            return self._parse_results(response.json())
        except Exception as e:
            logger.error(f"Web search failed: {str(e)}")
            return []
