// GroupDocs.Redaction for .NET — getting started (verification harness).
// Source: products/content/redaction/net/_index.en.md
using System;
using GroupDocs.Redaction;
using GroupDocs.Redaction.Redactions;

class Program { static void Main() {
// Pass the input file to a Redactor instance
using (Redactor redactor = new Redactor("source.pdf"))
{
    // Configure the redaction options
    var repl_opt = new ReplacementOptions("[redacted]");
    var red = new ExactPhraseRedaction("Data", repl_opt);

    // Run the redaction process
    RedactorChangeLog result = redactor.Apply(red);

    // Save the redacted file
    if (result.Status != RedactionStatus.Failed)
    {
        redactor.Save();
    }
}
} }
