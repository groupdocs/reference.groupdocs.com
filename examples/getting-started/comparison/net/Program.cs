// GroupDocs.Comparison for .NET — getting started (verification harness).
// Source: products/content/comparison/net/_index.en.md
using System;
using GroupDocs.Comparison;
using GroupDocs.Comparison.Options;

class Program { static void Main() {
// Specify the source document
using (Comparer comparer = new Comparer("source.docx"))
{
    // Add one or more target documents
    comparer.Add("target.docx");

    // Specify comparison options
    CompareOptions options = new CompareOptions()
    {ShowRevisions = false};

    // Compare and save result
    comparer.Compare("result.docx", options);
}
} }
