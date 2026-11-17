// Source: data/getting_started.yaml → redaction.nodejs
const groupdocs = require('@groupdocs/groupdocs.redaction');

// Load your source file with a Redactor instance
const redactor = new groupdocs.Redactor("sample.pdf");

// Define the redaction criteria and settings
const replOpt = new groupdocs.ReplacementOptions("[redacted]");
const red = new groupdocs.ExactPhraseRedaction("Data", replOpt);

// Execute the redaction operation
const result = redactor.apply(red);

// Save the file with redactions applied
redactor.save();
redactor.close();
