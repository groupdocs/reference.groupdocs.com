// GroupDocs.Search for Java — getting started (verification harness).
import com.groupdocs.search.*;
import com.groupdocs.search.results.*;

public class Example {
    public static void main(String[] args) throws Exception {
        // Create an index for your documents
        Index index = new Index("c:/MyIndex");

        // Add documents to the index for efficient searching
        index.add("c:/MyDocuments");

        // Search for specific words or phrases, such as
        // 'affect', 'effect', 'principles', 'principally'
        SearchResult results =
            index.search("?ffect & princip?(2~4)");
    }
}
