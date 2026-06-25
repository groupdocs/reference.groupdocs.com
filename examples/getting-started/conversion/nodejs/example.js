// GroupDocs.Conversion for Node.js via Java — getting started (verification harness).
// Source: products/content/conversion/nodejs-java/_index.en.md
// Run: set JAVA_HOME to a JDK, then `npm install` and `node example.js` (needs source.docx).
const groupdocs = require('@groupdocs/groupdocs.conversion');

// Load the source DOCX file
const converter = new groupdocs.Converter("source.docx");

// Set the convert options
const convertOptions = new groupdocs.PdfConvertOptions();

// Convert DOCX to PDF
converter.convert("converted.pdf", convertOptions);
