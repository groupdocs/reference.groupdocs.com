// GroupDocs.Conversion for .NET — getting started (verification harness).
// Source: products/content/conversion/net/_index.en.md  ·  install: dotnet add package GroupDocs.Conversion
using GroupDocs.Conversion;
using GroupDocs.Conversion.Options.Convert;

// Load the source PDF file
using (var converter = new Converter("resume.pdf"))
{
    // Set the convert options
    var convertOptions = new WordProcessingConvertOptions();

    // Convert PDF to DOCX
    converter.Convert("resume.docx", convertOptions);
}
