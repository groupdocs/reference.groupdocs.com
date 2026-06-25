# GroupDocs.Editor for Python via .NET — getting started (verification harness).
# Source: products/content/editor/python-net/_index.en.md
from groupdocs.editor import Editor, EditableDocument
from groupdocs.editor.formats import WordProcessingFormats
from groupdocs.editor.options import WordProcessingSaveOptions

# Pass source document to initialize the Editor
with Editor("input.docx") as editor:

    # Open document for edit
    original = editor.edit()

    # Get document as HTML
    html = original.get_embedded_html()

    # Edit document contents
    edited_html = html.replace("Old text", "New text")

    # Load edited document from HTML
    edited = EditableDocument.from_markup(edited_html)

    # Save edited document to file with desired format
    editor.save(edited, "output.docx", WordProcessingSaveOptions(WordProcessingFormats.DOCX))
