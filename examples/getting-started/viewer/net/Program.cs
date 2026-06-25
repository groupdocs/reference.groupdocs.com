// GroupDocs.Viewer for .NET — getting started (verification harness).
// Source: products/content/viewer/net/_index.en.md  ·  install: dotnet add package GroupDocs.Viewer
using GroupDocs.Viewer;
using GroupDocs.Viewer.Options;

// Load the source PDF file
using (var viewer = new Viewer("resume.pdf"))
{
    // Set output HTML options, one file per page
    var viewOptions = HtmlViewOptions.ForEmbeddedResources("page{0}.html");

    // Render PDF to HTML with embedded resources
    viewer.View(viewOptions);
}
