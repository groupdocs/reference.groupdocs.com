# GroupDocs.Signature for Python via .NET — getting started (verification harness).
# Source: products/content/signature/python-net/_index.en.md (corrected to the current package API:
#   TextSignOptions -> groupdocs.signature.options, Color -> groupdocs.pydrawing, snake_case members).
# install: pip install groupdocs-signature-net
from groupdocs.signature import Signature
from groupdocs.signature.options import TextSignOptions
from groupdocs.pydrawing import Color

# Select PDF document
with Signature("sample.pdf") as signature:
    # Provide text
    options = TextSignOptions("John Smith")

    # Set color
    options.fore_color = Color.red

    # Sign document and save to file
    signature.sign("signed.pdf", options)
