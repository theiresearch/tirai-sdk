# TIRAI

The I Research AI - including a unified SDK for various AI model providers.

[![PyPI version](https://badge.fury.io/py/TIRAI.svg)](https://badge.fury.io/py/TIRAI)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Features

- Unified SDK interface for multiple AI providers:
  - xAI's Grok models
  - DeepSeek models
  - Azure OpenAI models
  - OpenAI GPT models
- Simple configuration management
- Automatic model selection based on input
- Response time tracking
- Type hints and comprehensive documentation

## Installation

```bash
pip install TIRAI
```

## Quick Start

```python
from TIRAI import AISDKConfig

# Create an SDK instance for the model you want to use
sdk = AISDKConfig.create_sdk('gpt-4o')  # For OpenAI gpt-4o
# sdk = AISDKConfig.create_sdk('grok-2-latest')  # For Grok
# sdk = AISDKConfig.create_sdk('deepseek-reasoner')  # For DeepSeek R1
# sdk = AISDKConfig.create_sdk('azure-o3-mini')  # For Azure OpenAI o3-mini

# Get a response
response, time_taken = sdk.get_response(
    "What is the capital of France?",
    model="gpt-4o"
)

print(f"Response: {response}")
print(f"Time taken: {time_taken:.2f}s")
```

## Configuration

The SDK requires API keys to be set as environment variables:

```bash
# For OpenAI
export OPENAI_API_KEY="your-api-key"
export OPENAI_BASE_URL="https://api.openai.com/v1"  # Optional

# For X.AI (Grok)
export XAI_API_KEY="your-api-key"
export XAI_BASE_URL="https://api.x.ai/v1"  # Optional

# For DeepSeek
export DEEPSEEK_API_KEY="your-api-key"
export DEEPSEEK_BASE_URL="https://api.deepseek.com/v1"  # Optional

# For Azure OpenAI
export AZURE_OPENAI_API_KEY="your-api-key"
export AZURE_OPENAI_URL="your-azure-endpoint"
```

## Supported Models

- OpenAI: `gpt-4o`, `gpt-3.5-turbo`, etc.
- X.AI: `grok-2-latest`
- DeepSeek: `deepseek-reasoner`
- Azure OpenAI: `azure-o3-mini`

## Error Handling

The SDK raises appropriate exceptions when API calls fail:

```python
try:
    response, time = sdk.get_response("Hello", "gpt-4o")
except requests.exceptions.RequestException as e:
    print(f"API call failed: {e}")
except ValueError as e:
    print(f"Invalid configuration: {e}")
```

## Development

To contribute to the SDK:

1. Clone the repository
```bash
git clone https://github.com/TheIResearch/tir-ai-sdk.git
cd tir-ai-sdk
```

2. Create a virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install development dependencies
```bash
pip install -e ".[dev]"
```

4. Run tests
```bash
python -m pytest tests/
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Support

For support, please create an issue on our [GitHub repository](https://github.com/TheIResearch/tir-ai-sdk/issues) or contact us at jl@theiresearch.com.

## Citation

If you use this SDK in your research, please cite:

```bibtex
@software{tir_ai_sdk,
  author = {The I Research},
  title = {TIR AI SDK},
  year = {2025},
  publisher = {GitHub},
  url = {https://github.com/theiresearch/tir-ai-sdk}
}
