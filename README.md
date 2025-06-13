# 🧊 TempConvert

A simple Python package to convert temperatures between Celsius and Fahrenheit.

---

## 📦 Installation

```bash
# Install via pip (from PyPI)
pip install tempconvert-atharv22
bash
Copy
Edit
# Or if you're using Poetry for development
poetry install
🚀 Usage
python
Copy
Edit
from tempconvert import celsius_to_fahrenheit, fahrenheit_to_celsius

print(celsius_to_fahrenheit(0))      # Output: 32.0
print(fahrenheit_to_celsius(212))    # Output: 100.0
🧪 Running Tests
bash
Copy
Edit
# Make sure you're in the virtual environment, then run:
pytest
bash
Copy
Edit
# All test cases are inside the tests/ folder
# Example:
tests/test_main.py
🔧 Development Setup
bash
Copy
Edit
# Clone the repository
git clone https://github.com/YOUR_USERNAME/tempconvert
cd tempconvert
bash
Copy
Edit
# Install dependencies using Poetry
poetry install
bash
Copy
Edit
# Activate the virtual environment
poetry env info --path

# Then manually activate it based on your OS path
📤 Publish to PyPI (For Maintainers Only)
bash
Copy
Edit
# Make sure you have the correct PyPI token set in GitHub secrets as PYPI_API_TOKEN
# Bump the version in pyproject.toml
bash
Copy
Edit
# Tag the new version:
git tag v0.1.x
git push origin v0.1.x

# GitHub Actions will auto-publish to PyPI
🤝 Contributing
bash
Copy
Edit
# Feel free to fork and create PRs!
# Make sure to include test coverage for new features.
📄 License
bash
Copy
Edit
MIT License © Atharv Chougale
