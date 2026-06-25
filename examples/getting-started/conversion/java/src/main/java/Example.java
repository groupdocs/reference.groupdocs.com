// GroupDocs.Conversion for Java — getting started (verification harness).
// Source: products/content/conversion/java/_index.en.md
import com.groupdocs.conversion.Converter;
import com.groupdocs.conversion.options.convert.WordProcessingConvertOptions;

public class Example {
    public static void main(String[] args) throws Exception {
        // Load the source PDF file
        Converter converter = new Converter("resume.pdf");

        // Set the convert options
        WordProcessingConvertOptions convertOptions = new WordProcessingConvertOptions();

        // Convert PDF to DOCX
        converter.convert("resume.docx", convertOptions);
    }
}
