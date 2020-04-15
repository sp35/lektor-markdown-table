import ast
import re

from setuptools import setup, find_packages
from os import path


this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

_description_re = re.compile(r"description\s+=\s+(?P<description>.*)")

with open(path.join(this_directory, "lektor_markdown_table.py"), "rb") as f:
    description = str(
        ast.literal_eval(
            _description_re.search(f.read().decode("utf-8")).group(1)
        )
    )

setup(
    author="Shubham Pandey",
    author_email="shubhampcpandey13@gmail.com",
    description=description,
    keywords="Lektor plugin",
    license="MIT",
    long_description=long_description,
    long_description_content_type="text/markdown",
    name="lektor-markdown-table",
    packages=find_packages(),
    py_modules=["lektor_markdown_table"],
    url="https://github.com/sp35/lektor-markdown-table",
    version="0.1",
    classifiers=["Framework :: Lektor", "Environment :: Plugins",],
    entry_points={
        "lektor.plugins": [
            "markdown-table = lektor_markdown_table:MarkdownTablePlugin",
        ]
    },
)
