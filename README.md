# Checkov tests with Kubernetes manifests including custom policies

## Installation

```bash
# Create new Python virtual environment
python -m venv venv

# Activate Python virtual environment on Windows
.\venv2\Scripts\activate

# Activate Python virtual environment on Linux/MacOS
source venv/bin/activate

# Patch pip and setuptools
python -m pip install --upgrade pip setuptools

# Install latest version of checkov
pip install checkov

# Check checkov version
checkov --version
```
