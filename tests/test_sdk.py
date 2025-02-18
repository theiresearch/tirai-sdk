"""Tests for TIRAI SDK"""

import os
import unittest
from unittest.mock import patch, MagicMock

from TIRAI import AISDKConfig
from TIRAI.sdk.providers import OpenAISDK, XAI_SDK, DeepSeekSDK, AzureOpenAISDK


class TestTIRAISDK(unittest.TestCase):
    """Test cases for TIRAI SDK"""

    def setUp(self):
        """Set up test environment"""
        # Set up test API keys
        os.environ['OPENAI_API_KEY'] = 'test_openai_key'
        os.environ['XAI_API_KEY'] = 'test_xai_key'
        os.environ['DEEPSEEK_API_KEY'] = 'test_deepseek_key'
        os.environ['AZURE_OPENAI_API_KEY'] = 'test_azure_key'
        os.environ['AZURE_OPENAI_URL'] = 'https://test.azure.com/openai'

    def tearDown(self):
        """Clean up test environment"""
        # Remove test API keys
        for key in ['OPENAI_API_KEY', 'XAI_API_KEY', 'DEEPSEEK_API_KEY', 
                   'AZURE_OPENAI_API_KEY', 'AZURE_OPENAI_URL']:
            os.environ.pop(key, None)

    def test_config_creation(self):
        """Test SDK configuration creation for all providers"""
        # Test OpenAI config
        config = AISDKConfig.get_config('gpt')
        self.assertEqual(config['api_key'], 'test_openai_key')
        self.assertEqual(config['base_url'], 'https://api.openai.com/v1')

        # Test XAI config
        config = AISDKConfig.get_config('grok')
        self.assertEqual(config['api_key'], 'test_xai_key')
        self.assertEqual(config['base_url'], 'https://api.x.ai/v1')

        # Test DeepSeek config
        config = AISDKConfig.get_config('deepseek')
        self.assertEqual(config['api_key'], 'test_deepseek_key')
        self.assertEqual(config['base_url'], 'https://api.deepseek.com/v1')

        # Test Azure config
        config = AISDKConfig.get_config('azure')
        self.assertEqual(config['api_key'], 'test_azure_key')
        self.assertEqual(config['api_url'], 'https://test.azure.com/openai')

    def test_sdk_creation(self):
        """Test SDK instance creation for all providers"""
        # Test OpenAI SDK
        sdk = AISDKConfig.create_sdk('gpt-4o')
        self.assertIsInstance(sdk, OpenAISDK)

        # Test XAI SDK
        sdk = AISDKConfig.create_sdk('grok-2-latest')
        self.assertIsInstance(sdk, XAI_SDK)

        # Test DeepSeek SDK
        sdk = AISDKConfig.create_sdk('deepseek-reasoner')
        self.assertIsInstance(sdk, DeepSeekSDK)

        # Test Azure SDK
        sdk = AISDKConfig.create_sdk('azure-o3-mini')
        self.assertIsInstance(sdk, AzureOpenAISDK)

    def test_invalid_model_type(self):
        """Test error handling for invalid model type"""
        with self.assertRaises(ValueError):
            AISDKConfig.get_config('invalid_model')

    def test_missing_api_key(self):
        """Test error handling for missing API key"""
        os.environ.pop('OPENAI_API_KEY')
        with self.assertRaises(ValueError):
            AISDKConfig.get_config('gpt')

    @patch('requests.post')
    def test_openai_response(self, mock_post):
        """Test OpenAI SDK response handling"""
        mock_response = MagicMock()
        mock_response.json.return_value = {
            'choices': [{
                'message': {
                    'content': 'Test response'
                }
            }]
        }
        mock_post.return_value = mock_response

        sdk = OpenAISDK(api_key='test_key')
        response, time_taken = sdk.get_response('Test input', 'gpt-4o')

        self.assertEqual(response, 'Test response')
        self.assertIsInstance(time_taken, float)
        mock_post.assert_called_once()

    @patch('requests.post')
    def test_api_error_handling(self, mock_post):
        """Test API error handling"""
        mock_post.side_effect = Exception('API Error')

        sdk = OpenAISDK(api_key='test_key')
        with self.assertRaises(Exception):
            sdk.get_response('Test input', 'gpt-4o')


if __name__ == '__main__':
    unittest.main()
