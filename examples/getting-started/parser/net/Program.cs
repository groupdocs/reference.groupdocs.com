// GroupDocs.Parser for .NET — getting started (verification harness).
// Source: products/content/parser/net/_index.en.md
using System;
using GroupDocs.Parser;

class Program { static void Main() {
// Pass source file to Parser instance
using (var parser = new Parser("source.pdf"))
{
    // Pass document text to TextReader
    using (var textReader = parser.GetText())
    {
        // Process document text
        Console.WriteLine(textReader?.ReadToEnd());
    }
}
} }
