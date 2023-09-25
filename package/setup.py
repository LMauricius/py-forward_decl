import setuptools
from pathlib import Path

# read the contents of your README file
this_directory = Path(__file__).parent
long_description = (this_directory.parent / "README.md").read_text()

setuptools.setup(
    name="forward_decl",
    version="0.1.1",
    author="LMauricius",
    packages=["forward_decl"],
    description="A simple module for supporting forward references",
    long_description=long_description,
    long_description_content_type='text/markdown'
)