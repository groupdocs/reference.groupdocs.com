# GroupDocs.Search for Python via .NET - getting started (verification harness).
# Source: products/content/search/python-net/_index.en.md
from groupdocs.search import Index

# Create an index for your documents
index = Index("./MyIndex")

# Add documents to the index for efficient searching
index.add("./MyDocuments")

# Search for specific words or phrases, such as
# 'affect', 'effect', 'principles', 'principally'
results = index.search("?ffect & princip?(2~4)")
