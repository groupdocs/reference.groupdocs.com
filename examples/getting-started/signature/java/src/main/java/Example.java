// GroupDocs.Signature for Java — getting started (verification harness).
// Source: products/content/signature/java/_index.en.md
import com.groupdocs.signature.Signature;
import com.groupdocs.signature.options.sign.TextSignOptions;
import java.awt.Color;

public class Example {
    public static void main(String[] args) throws Exception {
        // Select PDF document
        Signature signature = new Signature("sample.pdf");

        // Provide text
        TextSignOptions options = new TextSignOptions("John Smith");
        options.setForeColor(Color.RED);

        // Sign document and save to file
        signature.sign("signed.pdf", options);
    }
}
