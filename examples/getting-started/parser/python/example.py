# GroupDocs.Parser for Python via .NET — getting started (verification harness).
# Source: products/content/parser/python-net/_index.en.md
from groupdocs.parser import Parser

# Load the document
with Parser("sample.pdf") as parser:
    # Extract text from the document
    text = parser.get_text()

    # Print all extracted text
    print(text)
