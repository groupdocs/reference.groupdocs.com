// GroupDocs.Signature for .NET — getting started (verification harness).
// Source: products/content/signature/net/_index.en.md  ·  install: dotnet add package GroupDocs.Signature
using GroupDocs.Signature;
using GroupDocs.Signature.Options;
using System.Drawing;

// Select PDF document
using (Signature signature = new Signature("sample.pdf"))
{
    // Provide text
    var options = new TextSignOptions("John Smith")
    {
        // Set color
        ForeColor = Color.Red
    };

    // Sign document and save to file
    signature.Sign("signed.pdf", options);
}
