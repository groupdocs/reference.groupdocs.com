# GroupDocs.Metadata for Python via .NET — getting started (verification harness).
# Source: products/content/metadata/python-net/_index.en.md
from groupdocs.metadata import Metadata

def read_document_info():
    # Provide Spreadsheet path to Metadata
    with Metadata("./input.xlsx") as metadata:
        # Process metadata from the document
        info = metadata.get_document_info()
        print(f"File format: {info.file_type.file_format}")
        print(f"File extension: {info.file_type.extension}")
        print(f"MIME Type: {info.file_type.mime_type}")
        print(f"Number of pages: {info.page_count}")
        print(f"Document size: {info.size} bytes")
        print(f"Is document encrypted: {info.is_encrypted}")

if __name__ == "__main__":
    read_document_info()
