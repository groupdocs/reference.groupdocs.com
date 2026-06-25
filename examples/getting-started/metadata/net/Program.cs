// GroupDocs.Metadata for .NET — getting started (verification harness).
// Source: products/content/metadata/net/_index.en.md
using System;
using GroupDocs.Metadata;

class Program { static void Main() {
using (Metadata metadata = new Metadata("input.pdf"))
{
    // Remove all detected metadata packages
    int affected = metadata.Sanitize();
    Console.WriteLine("Properties removed: {0}", affected);
    metadata.Save("output.pdf");
}
} }
