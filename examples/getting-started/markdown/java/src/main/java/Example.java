// GroupDocs.Markdown for Java — getting started (verification harness).
// Source: data/getting_started.yaml -> markdown.java
import com.groupdocs.markdown.MarkdownConverter;

public class Example {
    public static void main(String[] args) throws Exception {
        // Load the source document
        MarkdownConverter converter = new MarkdownConverter("business-plan.pdf");

        // Export to Markdown
        converter.convert("business-plan.md");
    }
}
