# GroupDocs.Comparison for Python via .NET — getting started (verification harness).
# Source: products/content/comparison/python-net/_index.en.md
from groupdocs.comparison import Comparer

def compare_word_documents():
    # Specify the source document
    with Comparer("source.docx") as comparer:

        # Add one or more target documents
        comparer.add("target.docx")

        # Compare and save result
        comparer.compare("result.docx")

if __name__ == "__main__":
    compare_word_documents()
