# GroupDocs.Viewer for Python via .NET — getting started (verification harness).
# Source: products/content/viewer/python-net/_index.en.md  ·  install: pip install groupdocs-viewer-net
# Verified on groupdocs-viewer-net 26.11.0 (2026-11-26) with the sample files' catalog.pdf as resume.pdf.
from groupdocs.viewer import Viewer
from groupdocs.viewer.options import HtmlViewOptions

def render_pdf_to_html():
    # Instantiate Viewer
    with Viewer("resume.pdf") as viewer:

        # Set output HTML options, one file per page
        view_options = HtmlViewOptions.for_embedded_resources("page_{0}.html")

        # Render PDF to HTML with embedded resources
        viewer.view(view_options)

if __name__ == "__main__":
    render_pdf_to_html()
