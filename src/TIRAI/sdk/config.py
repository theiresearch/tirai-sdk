"""Configuration management for TIRAI SDK"""

import os
from typing import Dict, Any

from .providers import OpenAISDK, XAI_SDK, DeepSeekSDK, AzureOpenAISDK


class AISDKConfig:
    """Configuration manager for AI SDKs"""

    @staticmethod
    def get_config(model_type: str) -> Dict[str, str]:
        """Get configuration for a specific model type

        Args:
            model_type: Type of model ('gpt', 'grok', 'deepseek', 'azure')

        Returns:
            Dictionary containing configuration for the specified model

        Raises:
            ValueError: If API key is not found in environment variables
        """
        configs = {
            'gpt': {
                'api_key': os.environ.get('OPENAI_API_KEY'),
                'base_url': os.environ.get('OPENAI_BASE_URL', 'https://api.openai.com/v1')
            },
            'grok': {
                'api_key': os.environ.get('XAI_API_KEY'),
                'base_url': os.environ.get('XAI_BASE_URL', 'https://api.x.ai/v1')
            },
            'deepseek': {
                'api_key': os.environ.get('DEEPSEEK_API_KEY'),
                'base_url': os.environ.get('DEEPSEEK_BASE_URL', 'https://api.deepseek.com/v1')
            },
            'azure': {
                'api_key': os.environ.get('AZURE_OPENAI_API_KEY'),
                'api_url': os.environ.get(
                    'AZURE_OPENAI_URL',
                    'https://jl-m6x5fmxq-swedencentral.openai.azure.com/openai/deployments/o3-mini/chat/completions?api-version=2024-12-01-preview'
                )
            }
        }

        config = configs.get(model_type)
        if not config:
            raise ValueError(f"Unknown model type: {model_type}")

        if not config.get('api_key'):
            raise ValueError(f"{model_type.upper()} API key not found in environment variables")

        return config

    @staticmethod
    def create_sdk(model: str) -> Any:
        """Create an SDK instance based on the model name

        Args:
            model: Name of the model (e.g., 'gpt-4o', 'grok-2-latest')

        Returns:
            An instance of the appropriate SDK class

        Raises:
            ValueError: If model type is unknown or API key is missing
        """
        if model.startswith('gpt'):
            config = AISDKConfig.get_config('gpt')
            return OpenAISDK(api_key=config['api_key'], base_url=config['base_url'])
        elif model.startswith('deepseek'):
            config = AISDKConfig.get_config('deepseek')
            return DeepSeekSDK(api_key=config['api_key'], base_url=config['base_url'])
        elif model.startswith('azure'):
            config = AISDKConfig.get_config('azure')
            return AzureOpenAISDK(api_key=config['api_key'], api_url=config['api_url'])
        else:  # default to grok
            config = AISDKConfig.get_config('grok')
            return XAI_SDK(api_key=config['api_key'], base_url=config['base_url'])
