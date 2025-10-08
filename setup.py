"""
Setup script for the project.

When run directly (python setup.py), it initializes the project structure.
When run by pip/setuptools, it performs standard package setup.
"""

import re
import sys
from pathlib import Path


def slugify(name: str) -> str:
    """Convert project name to a valid Python package name."""
    # Convert to lowercase and replace spaces/hyphens with underscores
    slug = name.lower().replace("-", "_").replace(" ", "_")
    # Remove any characters that aren't alphanumeric or underscore
    slug = re.sub(r"[^a-z0-9_]", "", slug)
    # Ensure it doesn't start with a number
    if slug and slug[0].isdigit():
        slug = "_" + slug
    return slug


def initialize_project():
    """Initialize project structure based on pyproject.toml."""
    pyproject_path = Path("pyproject.toml")
    
    if not pyproject_path.exists():
        print("Error: pyproject.toml not found")
        return False
    
    # Read pyproject.toml
    content = pyproject_path.read_text()
    
    # Extract project name
    match = re.search(r'name\s*=\s*"([^"]+)"', content)
    if not match:
        print("Error: Could not find project name in pyproject.toml")
        return False
    
    project_name = match.group(1)
    
    # Check if it's still the placeholder
    if project_name in ["[project-name]", "project-name"]:
        print("Error: Please update the project name in pyproject.toml first")
        print('Change name = "[project-name]" to your actual project name')
        return False
    
    # Generate package name
    package_name = slugify(project_name)
    print(f"Initializing project: {project_name}")
    print(f"Package name: {package_name}")
    
    # Create package directory
    package_dir = Path("src") / package_name
    if package_dir.exists():
        print(f"Package directory already exists: {package_dir}")
        return False
    
    package_dir.mkdir(parents=True, exist_ok=True)
    
    # Extract version from pyproject.toml
    version_match = re.search(r'version\s*=\s*"([^"]+)"', content)
    version = version_match.group(1) if version_match else "0.1.0"
    
    # Create __init__.py
    init_file = package_dir / "__init__.py"
    init_content = f'''"""Package for {project_name}"""

__version__ = "{version}"
'''
    init_file.write_text(init_content)
    
    # Update pyproject.toml to include the correct package name
    content = re.sub(
        r'include = \["[^"]*"\]',
        f'include = ["{package_name}*"]',
        content
    )
    pyproject_path.write_text(content)
    
    print(f"\n✅ Project initialized successfully!")
    print(f"   - Created: src/{package_name}/")
    print(f"   - Created: src/{package_name}/__init__.py")
    print(f"   - Updated: pyproject.toml")
    print(f"\nNext steps:")
    print(f"   1. Create a virtual environment: python -m venv venv")
    print(f"   2. Activate it: venv\\Scripts\\activate (Windows) or source venv/bin/activate (macOS/Linux)")
    print(f"   3. Install in dev mode: pip install -e \".[dev]\"")
    
    return True


def main():
    # If run directly, initialize the project
    if __name__ == "__main__":
        if len(sys.argv) == 1:  # No arguments, just 'python setup.py'
            initialize_project()
        else:
            # Let setuptools handle other commands
            from setuptools import setup
            setup()
    else:
        # Called by pip/setuptools, do normal setup
        from setuptools import setup
        setup()


if __name__ == "__main__":
    main()
