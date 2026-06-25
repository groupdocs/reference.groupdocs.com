// GroupDocs.Editor for .NET — getting started (verification harness).
// Source: products/content/editor/net/_index.en.md
using System;
using GroupDocs.Editor;
using GroupDocs.Editor.Options;

class Program { static void Main() {
// Pass source document to initialize the Editor
var editor = new Editor("input.docx");

// Open document for edit
var originalDoc = editor.Edit();

// Get document as HTML
var srcHtml = originalDoc.GetEmbeddedHtml();

// Edit document contents
var editedHtml = srcHtml.Replace("Old text", "New text");

// Load edited document from HTML
var editedDoc = EditableDocument.FromMarkup(editedHtml, null);

// Save edited document to file with desired format
var saveOptions = new WordProcessingSaveOptions();
editor.Save(editedDoc, "output.docx", saveOptions);
} }
