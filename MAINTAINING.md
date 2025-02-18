# Maintaining TIRAI

This document provides guidelines for developers maintaining and contributing to the TIRAI SDK.

## Development Setup

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

3. Install dependencies
```bash
pip install -r requirements.txt
pip install -e .
```

## Project Structure

```
tirai-sdk/
├── src/
│   └── TIRAI/
│       ├── sdk/
│       │   ├── providers/
│       │   │   ├── openai.py
│       │   │   ├── xai.py
│       │   │   ├── deepseek.py
│       │   │   └── azureopenai.py
│       │   ├── base.py
│       │   └── config.py
│       └── __init__.py
├── tests/
│   └── test_sdk.py
├── examples/
│   └── basic_usage.py
└── requirements.txt
```

## Testing

The project includes a comprehensive test suite with 83% code coverage. Current coverage by module:

- `config.py`: 100%
- `openai.py`: 100%
- `base.py`: 78%
- `azureopenai.py`: 64%
- `deepseek.py`: 64%
- `xai.py`: 64%

### Running Tests

Run the full test suite with coverage:
```bash
pytest tests/ -v --cov=TIRAI
```

Run a specific test:
```bash
pytest tests/test_sdk.py -k "test_config_creation"
```

### Test Structure

The test suite (`test_sdk.py`) includes:
- Configuration tests
- SDK creation tests
- API error handling tests
- Response handling tests
- Missing API key tests

## Code Style

- Use Black for code formatting
- Use isort for import sorting
- Follow PEP 8 guidelines
- Maintain type hints throughout the codebase

Format code before committing:
```bash
black src/ tests/
isort src/ tests/
flake8 src/ tests/
mypy src/ tests/
```

## Adding New Providers

1. Create a new provider file in `src/TIRAI/sdk/providers/`
2. Implement the provider class extending `BaseSDK`
3. Add configuration handling in `config.py`
4. Add tests in `test_sdk.py`
5. Update supported models in README.md

## Release Process

1. Update version in `pyproject.toml`
2. Update CHANGELOG.md
3. Run tests and ensure all pass
4. Build distribution:
   ```bash
   python -m build
   ```
5. Upload to PyPI:
   ```bash
   twine upload dist/*
   ```

## Continuous Integration

The project uses GitHub Actions for CI/CD:
- Runs tests on each pull request
- Checks code formatting
- Builds and publishes releases

## Documentation

- Keep README.md user-focused
- Update MAINTAINING.md for developer changes
- Document all public APIs with docstrings
- Include type hints for all functions

## Support

For bugs and feature requests:
1. Check existing GitHub issues
2. Create a new issue with:
   - Clear description
   - Steps to reproduce
   - Expected vs actual behavior
   - Environment details
