// GroupDocs.Comparison for Java — getting started (verification harness).
import com.groupdocs.comparison.*;
import com.groupdocs.comparison.options.*;

public class Example {
    public static void main(String[] args) throws Exception {
        // Specify the source document
        try (Comparer comparer = new Comparer("source.docx"))
        {
          // Add one or more target documents
          comparer.add("target.docx");

          // Specify comparison options
          CompareOptions options = new CompareOptions();
          options.setShowRevisions(false);

          // Compare and save result
          comparer.compare("result.docx", options);
        }
    }
}
