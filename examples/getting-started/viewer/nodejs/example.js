// GroupDocs.Viewer for Node.js via Java — getting started (verification harness).
// Source: products/content/viewer/nodejs-java/_index.en.md
// Run: set JAVA_HOME to a JDK, then `npm install` and `node example.js` (needs resume.pdf).
const groupdocs = require('@groupdocs/groupdocs.viewer');

// Instantiate Viewer
const viewer = new groupdocs.Viewer("resume.pdf");

// Set output HTML options, one file per page
const viewOptions = groupdocs.HtmlViewOptions.forEmbeddedResources();

// Render PDF to HTML with embedded resources
viewer.view(viewOptions);
viewer.close();
