// GroupDocs.Watermark for Java — getting started (verification harness).
import com.groupdocs.watermark.*;
import com.groupdocs.watermark.watermarks.*;
import com.groupdocs.watermark.options.*;

public class Example {
    public static void main(String[] args) throws Exception {
        // Instantiate Watermarker passing PDF path
        PdfLoadOptions loadOptions = new PdfLoadOptions();
        Watermarker watermarker =
            new Watermarker("source.pdf", loadOptions);

        // Customize watermark options
        TextWatermark textWatermark =
            new TextWatermark("Approved", new Font("Arial", 8));

        // Apply watermark to PDF document
        watermarker.add(textWatermark);

        // Save result document
        watermarker.save("result.pdf");
        watermarker.close();
    }
}
