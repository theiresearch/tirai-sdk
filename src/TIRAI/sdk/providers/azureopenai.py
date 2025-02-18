"""Azure OpenAI API provider implementation"""

import time
from typing import Tuple
import requests

from ..base import BaseAISDK


class AzureOpenAISDK(BaseAISDK):
    """Azure OpenAI API client"""

    def __init__(self, api_key: str, api_url: str):
        self.api_key = api_key
        self.api_url = api_url

    def get_response(self, text: str, model: str) -> Tuple[str, float]:
        """Get response from Azure OpenAI model

        Args:
            text: Input text to send to the model
            model: Name of the model to use

        Returns:
            Tuple of (response text, time taken in seconds)

        Raises:
            requests.exceptions.RequestException: If the API request fails
        """
        start_time = time.time()

        headers = {
            'api-key': self.api_key,
            'Content-Type': 'application/json'
        }

        response = requests.post(
            self.api_url,
            headers=headers,
            json={
                'messages': [{
                    'role': 'user',
                    'content': text
                }]
            }
        )
        response.raise_for_status()

        return response.json()['choices'][0]['message']['content'], time.time() - start_time
