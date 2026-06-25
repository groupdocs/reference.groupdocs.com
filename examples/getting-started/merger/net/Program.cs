// GroupDocs.Merger for .NET — getting started (verification harness).
// Source: products/content/merger/net/_index.en.md
using System;
using GroupDocs.Merger;

class Program { static void Main() {
// Open the source PDF file
using (Merger merger = new Merger(@"c:\sample1.pdf"))
{
  // Append another PDF file for merging
  merger.Join(@"c:\sample2.pdf");

  // Combine PDF files and save the output
  merger.Save(@"c:\merged.pdf");
}
} }
