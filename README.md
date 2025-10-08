# Python Project Template

A minimal Python project skeleton with best practices for packaging and development.

## Prerequisites

- Python 3.9 or higher
- pip (usually comes with Python)

## Setup

### 1. Clone or Use This Template

```bash
git clone <url>
cd <project_name>
```

### 2. Configure Your Project

Edit `pyproject.toml` and update the following fields:

```toml
[project]
name = "your-project-name"           # Change this to your project name
version = "0.1.0"
description = "Your project description"  # Change this
authors = [{name = "Your Name", email = "your.email@example.com"}]  # Change this
```

**Important:** Make sure to set a real project name (not `[project-name]`).

### 3. Initialize Project Structure

Run the setup script to automatically create your package structure:

```bash
mkdir src
python setup.py
```

This will:
- Read your project name from `pyproject.toml`
- Create `src/<package_name>/` directory
- Create `src/<package_name>/__init__.py` with version info
- Update `pyproject.toml` package discovery settings

### 4. Create a Virtual Environment

**Windows:**
```powershell
python -m venv venv
venv\Scripts\activate
```

**macOS/Linux:**
```bash
python -m venv venv
source venv/bin/activate
```

### 5. Install the Package

**For development (editable install with dev dependencies):**
```bash
pip install -e ".[dev]"
```

**For production (runtime dependencies only):**
```bash
pip install .
```

## Adding Dependencies

Edit `pyproject.toml` and add your dependencies:

```toml
dependencies = [
    "requests>=2.31.0",
    "numpy>=1.24.0",
]
```

Then reinstall:
```bash
pip install -e ".[dev]"
```
