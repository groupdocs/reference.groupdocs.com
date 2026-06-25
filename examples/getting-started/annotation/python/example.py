# GroupDocs.Annotation for Python via .NET — getting started (verification harness).
# Source: products/content/annotation/python-net/_index.en.md  ·  install: pip install groupdocs-annotation-net
from groupdocs.annotation import Annotator
from groupdocs.annotation.models import Rectangle
from groupdocs.annotation.models.annotation_models import AreaAnnotation
from groupdocs.pydrawing import Color

# Open your file with an Annotator instance
with Annotator("input.pdf") as annotator:
    # Create and configure an annotation
    area = AreaAnnotation()
    area.box = Rectangle(100, 100, 200, 80)
    area.background_color = Color.yellow.to_argb()
    area.page_number = 0
    area.message = "Review this section"

    # Add the annotation to the document
    annotator.add(area)

    # Save the annotated file
    annotator.save("annotated.pdf")
