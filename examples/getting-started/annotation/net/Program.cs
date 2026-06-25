// GroupDocs.Annotation for .NET — getting started (verification harness).
// Source: products/content/annotation/net/_index.en.md  ·  install: dotnet add package GroupDocs.Annotation
using GroupDocs.Annotation;
using GroupDocs.Annotation.Models;
using GroupDocs.Annotation.Models.AnnotationModels;

// Open the file with an Annotator instance
using (Annotator annotator = new Annotator("input.pdf"))
{
    // Create and configure an annotation
    AreaAnnotation area = new AreaAnnotation
    {
        Box = new Rectangle(100, 100, 200, 80),
        BackgroundColor = 65535,
        PageNumber = 0,
        Message = "Review this section"
    };

    // Add the annotation to the document
    annotator.Add(area);

    // Save the annotated file
    annotator.Save("annotated.pdf");
}
