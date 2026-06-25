// GroupDocs.Merger for Java — getting started (verification harness).
import com.groupdocs.merger.*;

public class Example {
    public static void main(String[] args) throws Exception {
        // Load the source PDF file
        Merger merger = new Merger("sample1.pdf");

        // Add another PDF file to combine
        merger.join("sample2.pdf");

        // Merge PDF files and save the output
        merger.save("merged.pdf");
    }
}
