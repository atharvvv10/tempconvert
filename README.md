🧊 TempConvert
A simple Python package to convert temperatures between Celsius and Fahrenheit.

📦 Installation
Install via pip (from PyPI):

bash
Copy
Edit
pip install tempconvert-atharv22
Or if you're using Poetry for development:

bash
Copy
Edit
poetry install
🚀 Usage
python
Copy
Edit
from tempconvert import celsius_to_fahrenheit, fahrenheit_to_celsius

print(celsius_to_fahrenheit(0))      # Output: 32.0
print(fahrenheit_to_celsius(212))    # Output: 100.0
🧪 Running Tests
Make sure you're in the virtual environment. Then run:

bash
Copy
Edit
pytest
All test cases are inside the tests/ folder (e.g., test_main.py).

🔧 Development Setup
Clone the repository:

bash
Copy
Edit
git clone https://github.com/YOUR_USERNAME/tempconvert
cd tempconvert
Install dependencies using Poetry:

bash
Copy
Edit
poetry install
Activate the virtual environment:

bash
Copy
Edit
poetry env info --path
Then manually activate it based on your OS path.

📤 Publish to PyPI (For Maintainers Only)
Make sure you have the correct PyPI token set in GitHub secrets as PYPI_API_TOKEN.

Bump the version in pyproject.toml

Tag the new version:

bash
Copy
Edit
git tag v0.1.x
git push origin v0.1.x
GitHub Actions will auto-publish to PyPI.

🤝 Contributing
Feel free to fork and create PRs! Make sure to include test coverage for new features.

📄 License
MIT License © Atharv Chougale

