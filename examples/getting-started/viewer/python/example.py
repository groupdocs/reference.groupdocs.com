# GroupDocs.Viewer for Python via .NET — getting started (verification harness).
# Source: products/content/viewer/python-net/_index.en.md  ·  install: pip install groupdocs-viewer-net
from groupdocs.viewer import Viewer
from groupdocs.viewer.options import HtmlViewOptions

# Instantiate Viewer
with Viewer("resume.pdf") as viewer:
    # Set output HTML options, one file per page
    view_options = HtmlViewOptions.for_embedded_resources("page_{0}.html")

    # Render PDF to HTML with embedded resources
    viewer.view(view_options)
