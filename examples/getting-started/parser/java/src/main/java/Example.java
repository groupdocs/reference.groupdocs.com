// GroupDocs.Parser for Java — getting started (verification harness).
import com.groupdocs.parser.*;
import com.groupdocs.parser.data.*;

public class Example {
    public static void main(String[] args) throws Exception {
        // Pass source file to Parser instance
        try (Parser parser = new Parser("source.pdf"))
        {
            // Pass document text to TextReader
            try (TextReader reader = parser.getText())
            {
                // Process document text
                System.out.println(reader == null
                    ? ""
                    : reader.readToEnd());
            }
        }
    }
}
