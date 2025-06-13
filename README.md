# 🧊 TempConvert

```bash
📌 Internship Context

This project was completed as part of an internship assignment (Days 1–15).
The main goal was not to build a complex application, but to understand and practice:

✅ Python packaging and project structuring

✅ Dependency management with Poetry

✅ Writing and running unit tests with pytest

✅ Automating workflows using GitHub Actions (CI/CD)

✅ Publishing packages to PyPI

You can refer to this project if you're working on similar internship or learning tasks.
```

A simple Python package to convert temperatures between Celsius and Fahrenheit.

---

## 📦 Installation

```bash
# Install via pip (from PyPI)
pip install tempconvert-atharv22
```

```bash
# Or if you're using Poetry for development
poetry install
```

---

## 🚀 Usage

```bash
# Example Python usage
from tempconvert import celsius_to_fahrenheit, fahrenheit_to_celsius

print(celsius_to_fahrenheit(0))      # Output: 32.0
print(fahrenheit_to_celsius(212))    # Output: 100.0
```

---

## 🧪 Running Tests

```bash
# Make sure you're in the virtual environment. Then run:
pytest
```

```bash
# All test cases are inside the tests/ folder
# For example:
tests/test_main.py
```

---

## 🔧 Development Setup

```bash
# Clone the repository
git clone https://github.com/YOUR_USERNAME/tempconvert
cd tempconvert
```

```bash
# Install dependencies using Poetry
poetry install
```

```bash
# Activate the virtual environment
poetry env info --path

# Then manually activate it based on your OS path
```

---

## 📤 Publish to PyPI (For Maintainers Only)

```bash
# Make sure you have the correct PyPI token set in GitHub secrets as PYPI_API_TOKEN
# Bump the version in pyproject.toml
```

```bash
# Tag the new version:
git tag v0.1.x
git push origin v0.1.x

# GitHub Actions will auto-publish to PyPI
```

---

## 🤝 Contributing

```bash
# Feel free to fork and create PRs!
# Make sure to include test coverage for new features.
```

---

## 📄 License

```bash
MIT License © Atharv Chougale
```

