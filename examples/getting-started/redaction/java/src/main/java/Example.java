// GroupDocs.Redaction for Java — getting started (verification harness).
import com.groupdocs.redaction.*;
import com.groupdocs.redaction.redactions.*;

public class Example {
    public static void main(String[] args) throws Exception {
        // Load your source file with a Redactor instance
        final Redactor redactor = new Redactor("sample.pdf");
        try
        {
            // Define the redaction criteria and settings
            ReplacementOptions ro = new ReplacementOptions("[redacted]");
            ExactPhraseRedaction red = new ExactPhraseRedaction("Data", ro);

            // Execute the redaction operation
            RedactorChangeLog result = redactor.apply(red);

            // Save the file with redactions applied
            redactor.save();
        }
        finally { redactor.close(); }
    }
}
