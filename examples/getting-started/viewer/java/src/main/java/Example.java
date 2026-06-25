// GroupDocs.Viewer for Java — getting started (verification harness).
// Source: products/content/viewer/java/_index.en.md
import com.groupdocs.viewer.Viewer;
import com.groupdocs.viewer.options.HtmlViewOptions;

public class Example {
    public static void main(String[] args) throws Exception {
        // Instantiate Viewer
        try (Viewer viewer = new Viewer("resume.pdf")) {
            // Set output HTML options, one file per page
            HtmlViewOptions viewOptions = HtmlViewOptions.forEmbeddedResources();

            // Render PDF to HTML with embedded resources
            viewer.view(viewOptions);
        }
    }
}
