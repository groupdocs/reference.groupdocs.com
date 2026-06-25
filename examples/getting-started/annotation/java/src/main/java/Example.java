// GroupDocs.Annotation for Java — getting started (verification harness).
// Source: products/content/annotation/java/_index.en.md
import com.groupdocs.annotation.Annotator;
import com.groupdocs.annotation.models.Rectangle;
import com.groupdocs.annotation.models.annotationmodels.AreaAnnotation;

public class Example {
    public static void main(String[] args) throws Exception {
        // Load your source file with an Annotator instance
        Annotator annotator = new Annotator("input.pdf");
        try {
            // Create and configure an annotation
            AreaAnnotation area = new AreaAnnotation();
            area.setBox(new Rectangle(100, 100, 200, 80));
            area.setBackgroundColor(65535);
            area.setPageNumber(0);
            area.setMessage("Review this section");

            // Add the annotation to the document
            annotator.add(area);

            // Save the file with annotations applied
            annotator.save("annotated.pdf");
        } finally {
            annotator.dispose();
        }
    }
}
