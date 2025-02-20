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

## Test01

Folder `manifests01` contains a simple Kubernetes Pod manifest to test the built-in Checkov policies.

 ```bash
# Run Kubernetes checks with built-in policies
checkov -d manifests01 --framework kubernetes --summary-position bottom

# Run Kubernetes checks with built-in policies and skip some checks
checkov -d manifests01 --framework kubernetes --summary-position bottom --skip-check CKV2_K8S_6,CKV_K8S_11,CKV_K8S_43
 ```
