# GroupDocs.Conversion for Python via .NET — getting started (verification harness).
# Source: products/content/conversion/python-net/_index.en.md  ·  install: pip install groupdocs-conversion-net
from groupdocs.conversion import Converter
from groupdocs.conversion.options.convert import PdfConvertOptions

# Load the source DOCX file
with Converter("business-plan.docx") as converter:
    # Set conversion options
    convert_options = PdfConvertOptions()

    # Convert DOCX to PDF
    converter.convert("converted.pdf", convert_options)
