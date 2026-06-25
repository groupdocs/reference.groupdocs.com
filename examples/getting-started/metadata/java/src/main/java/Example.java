// GroupDocs.Metadata for Java — getting started (verification harness).
import com.groupdocs.metadata.*;

public class Example {
    public static void main(String[] args) throws Exception {
        try (Metadata metadata = new Metadata("input.pdf")) {
            // Remove all detected metadata packages
            int affected = metadata.sanitize();
            System.out.println("Properties removed: " + affected);
            metadata.save("output.pdf");
        }
    }
}
