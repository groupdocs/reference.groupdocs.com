// GroupDocs.Editor for Java — getting started (verification harness).
import com.groupdocs.editor.*;
import com.groupdocs.editor.options.*;

public class Example {
    public static void main(String[] args) throws Exception {
        // Pass source document to initialize the Editor
        Editor editor = new Editor("input.docx");

        // Open document for edit
        EditableDocument originalDoc = editor.edit();

        // Get document as HTML
        String srcHtml = originalDoc.getEmbeddedHtml();

        // Edit document contents
        String editedHtml = srcHtml.replace("Old text", "New text");

        // Load edited document from HTML
        EditableDocument editedDoc = EditableDocument.fromMarkup(editedHtml, null);

        // Save edited document to file with desired format
        WordProcessingSaveOptions saveOptions = new WordProcessingSaveOptions();
        editor.save(editedDoc, "output.docx", saveOptions);
    }
}
