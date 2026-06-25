// GroupDocs.Markdown for .NET — getting started (verification harness).
// Source: products/content/markdown/net/_index.en.md
using System;
using GroupDocs.Markdown;

class Program { static void Main() {
// Import the namespace

// Load the source document
using var converter = new MarkdownConverter("business-plan.pdf");

// Export to Markdown
converter.Convert("business-plan.md");
} }
