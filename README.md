# TIRAI

The I Research AI - A unified SDK for various AI model providers.

[![PyPI version](https://badge.fury.io/py/TIRAI.svg)](https://badge.fury.io/py/TIRAI)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Features

- Unified interface for multiple AI providers:
  - OpenAI gpt-4o
  - xAI's grok-2-latest
  - DeepSeek's deepseek-reasoner
  - Azure o3-mini
- Simple API key management via environment variables
- Automatic model selection and configuration
- Response time tracking
- Comprehensive test coverage
- Type hints and documentation

## Installation

```bash
pip install TIRAI
```

## Quick Start

1. Set up environment variables for your chosen provider:

```bash
# OpenAI
export OPENAI_API_KEY="your-key"                             # Required
export OPENAI_BASE_URL="https://api.openai.com/v1"          # Optional

# xAI (Grok)
export XAI_API_KEY="your-key"                               # Required
export XAI_BASE_URL="https://api.x.ai/v1"                   # Optional

# DeepSeek
export DEEPSEEK_API_KEY="your-key"                          # Required
export DEEPSEEK_BASE_URL="https://api.deepseek.com/v1"      # Optional

# Azure OpenAI o3-mini
export AZURE_OPENAI_API_KEY="your-key"                      # Required
export AZURE_OPENAI_URL="your-deployment-url"               # Required
```

2. Create an SDK instance and get responses:

```python
from TIRAI import AISDKConfig

# Create an SDK instance for your chosen model
sdk = AISDKConfig.create_sdk('gpt-4o')         # For OpenAI
# sdk = AISDKConfig.create_sdk('grok-2-latest')  # For Grok
# sdk = AISDKConfig.create_sdk('deepseek-reasoner')  # For DeepSeek
# sdk = AISDKConfig.create_sdk('azure-o3-mini')  # For Azure OpenAI

# Get a response
try:
    response, time_taken = sdk.get_response("What is artificial intelligence?")
    print(f"Response: {response}")
    print(f"Time taken: {time_taken:.2f}s")
except Exception as e:
    print(f"Error: {e}")
```

## Supported Models

- OpenAI: `gpt-4o`
- X.AI: `grok-2-latest`
- DeepSeek: `deepseek-reasoner`
- Azure OpenAI: `azure-o3-mini`

## Error Handling

The SDK provides clear error messages for common issues:

```python
try:
    response, time = sdk.get_response("Your prompt here")
except ValueError as e:
    print(f"Configuration error: {e}")  # Missing API keys, invalid models
except requests.exceptions.RequestException as e:
    print(f"API call failed: {e}")  # Network errors, API timeouts
```

## Development

For development and contribution guidelines, please see [MAINTAINING.md](MAINTAINING.md).

## License

This project is licensed under the MIT License - see the LICENSE file for details.
