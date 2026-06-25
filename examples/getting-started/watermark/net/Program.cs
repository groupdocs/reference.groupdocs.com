// GroupDocs.Watermark for .NET — getting started (verification harness).
// Source: products/content/watermark/net/_index.en.md
using System;
using GroupDocs.Watermark;
using GroupDocs.Watermark.Watermarks;
using GroupDocs.Watermark.Options.Pdf;

class Program { static void Main() {
// Instantiate Watermarker passing PDF path
PdfLoadOptions loadOptions = new PdfLoadOptions();
using (Watermarker watermarker =
    new Watermarker("source.pdf", loadOptions))
{
    // Customize watermark options
    TextWatermark textWatermark =
        new TextWatermark("Approved", new Font("Arial", 8));

    // Apply watermark to PDF document
    watermarker.Add(textWatermark);

    // Save result document
    watermarker.Save("result.pdf");
}
} }
