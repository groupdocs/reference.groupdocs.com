# GroupDocs.Watermark for Python via .NET — getting started (verification harness).
# Source: products/content/watermark/python-net/_index.en.md
import groupdocs.watermark as gw
import groupdocs.watermark.watermarks as gww
import groupdocs.watermark.options.pdf as gwop
import groupdocs.watermark.common as gwc

# Instantiate Watermarker passing PDF path
pdf_lo = gwop.PdfLoadOptions()
with gw.Watermarker("source.pdf", pdf_lo) as watermarker:
    options = gwop.PdfArtifactWatermarkOptions()

    # Customize watermark options
    text_watermark = gww.TextWatermark("Approved", gww.Font("Arial", 8.0))
    text_watermark.horizontal_alignment = gwc.HorizontalAlignment.RIGHT

    # Apply watermark to PDF document
    watermarker.add(text_watermark, options)

    # Save result document
    watermarker.save("result.pdf")
