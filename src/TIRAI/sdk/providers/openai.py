"""OpenAI API provider implementation"""

import time
from typing import Tuple
import requests

from ..base import BaseAISDK


class OpenAISDK(BaseAISDK):
    """OpenAI API client"""

    def __init__(self, api_key: str, base_url: str = 'https://api.openai.com/v1'):
        self.api_key = api_key
        self.base_url = base_url

    def get_response(self, text: str, model: str) -> Tuple[str, float]:
        """Get response from OpenAI model

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
            'Authorization': f'Bearer {self.api_key}',
            'Content-Type': 'application/json'
        }

        response = requests.post(
            f'{self.base_url}/chat/completions',
            headers=headers,
            json={
                'model': model,
                'messages': [{
                    'role': 'user',
                    'content': text
                }]
            }
        )
        response.raise_for_status()

        return response.json()['choices'][0]['message']['content'], time.time() - start_time
