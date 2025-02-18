# Maintaining TIRAI Package

This guide explains how to maintain and update the TIRAI package, including making changes, versioning, and publishing new releases.

## One-Time Setup

1. **PyPI Account Setup**
   - Create an account on [PyPI](https://pypi.org/account/register/)
   - Go to Account Settings → API tokens
   - Create a new API token for TIRAI package
   - Save the token securely (you'll only see it once!)

2. **GitHub Repository Setup**
   - Go to your repository: https://github.com/theiresearch/tirai-sdk
   - Click Settings → Secrets and variables → Actions
   - Click "New repository secret"
   - Name: `PYPI_API_TOKEN`
   - Value: Your PyPI API token from step 1
   - Click "Add secret"

## Making Updates

### 1. Update Your Code
- Make your changes to the code in `src/TIRAI/`
- Test your changes locally
- Update documentation if needed

### 2. Update Version Number
Edit `setup.py` and increment the version number according to [Semantic Versioning](https://semver.org/):
```python
setup(
    name="TIRAI",
    version="0.1.1",  # Update this line
    ...
)
```

Version numbering follows MAJOR.MINOR.PATCH:
- MAJOR: Incompatible API changes (e.g., 1.0.0)
- MINOR: New features, backwards-compatible (e.g., 0.2.0)
- PATCH: Bug fixes, backwards-compatible (e.g., 0.1.1)

### 3. Commit and Push Changes
```bash
# Add all changed files
git add .

# Commit with a descriptive message
git commit -m "Update version to 0.1.1: Added feature X"

# Push to GitHub
git push
```

### 4. Create a GitHub Release
1. Go to https://github.com/theiresearch/tirai-sdk/releases
2. Click "Create a new release"
3. Fill in the details:
   - Tag version: `v0.1.1` (must match setup.py version with 'v' prefix)
   - Release title: "Version 0.1.1"
   - Description: List what changed in this version
4. Click "Publish release"

### 5. Automatic Publication
The GitHub Action will automatically:
1. Build the package
2. Upload to PyPI
3. Make it available for installation via `pip install TIRAI`

You can monitor the progress:
1. Go to your repository
2. Click Actions tab
3. Watch the "Publish to PyPI" workflow

## Verifying the Release

1. **Check PyPI**
   - Visit https://pypi.org/project/TIRAI/
   - Verify the new version is listed

2. **Test Installation**
```bash
# Create a new virtual environment
python -m venv test_env
source test_env/bin/activate

# Install the new version
pip install TIRAI

# Test the package
python -c "from TIRAI import AISDKConfig; print(AISDKConfig.list_models())"
```

## Troubleshooting

### Release Failed
1. Check the Actions tab for error messages
2. Common issues:
   - Version number in setup.py doesn't match GitHub release tag
   - PyPI token expired or incorrect
   - Build errors in the code

### Need to Delete a Release
- Only delete releases if absolutely necessary
- Cannot delete/modify versions already on PyPI
- Must increment version number for new releases

## Getting Help
- PyPI Issues: https://pypi.org/help/
- GitHub Actions: https://docs.github.com/en/actions
- Package Questions: Create an issue in the GitHub repository

Remember: You cannot modify a version once it's published to PyPI. Always test thoroughly before releasing!
