# GroupDocs.Signature for Python via .NET - getting started (verification harness).
# Source: products/content/signature/python-net/_index.en.md (the hero snippet, same code).
# Verified 2026-10-08 against groupdocs-signature-net 26.10.0 (PyPI).
# install: pip install groupdocs-signature-net
from groupdocs.pydrawing import Color
from groupdocs.signature import Signature
from groupdocs.signature.options import TextSignOptions


def sign_with_text():
    # Select PDF document
    with Signature("sample.pdf") as signature:

        # Provide text
        options = TextSignOptions("John Smith")

        # Set color
        options.fore_color = Color.red

        # Sign document and save to file
        signature.sign("signed.pdf", options)


if __name__ == "__main__":
    sign_with_text()
