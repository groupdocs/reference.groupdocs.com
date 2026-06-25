// GroupDocs.Search for .NET — getting started (verification harness).
// Source: products/content/search/net/_index.en.md
using GroupDocs.Search;
using GroupDocs.Search.Results;

class Program { static void Main() {
// Create an index for your documents
Index index = new Index("c:/MyIndex");

// Add documents to the index for efficient searching
index.Add("c:/MyDocuments");

// Search for specific words or phrases, such as
// 'affect', 'effect', 'principles', 'principally'
SearchResult results =
    index.Search("?ffect & princip?(2~4)");
} }
