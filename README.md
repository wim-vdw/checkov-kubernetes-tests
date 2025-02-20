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

## Test02

Folder `manifests02` contains a simple Kubernetes database manifest based on a fake CRD.  
Running checkov on this manifest will show that the built-in policies are not enough to cover all the checks.  
Folder `custom_policies` contains some custom policies written in `YAML` and `Python` to check the database manifest.

 ```bash
# Run Kubernetes checks with built-in policies
checkov -d manifests02 --framework kubernetes --summary-position bottom

# Run Kubernetes checks with built-in policies and custom policies
checkov -d manifests02 --framework kubernetes --summary-position bottom --external-checks-dir custom_policies
 ```
