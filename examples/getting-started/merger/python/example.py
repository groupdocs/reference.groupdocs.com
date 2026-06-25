# GroupDocs.Merger for Python via .NET — getting started (verification harness).
# Source: products/content/merger/python-net/_index.en.md
from groupdocs.merger import Merger

def run():

    # Load the original PDF file
    with Merger("sample1.pdf") as merger:

        # Add another PDF file for merging
        merger.join("sample2.pdf")

        # Combine the PDF files and save the output
        merger.save("merged.pdf")
run()

