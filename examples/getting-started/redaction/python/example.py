# GroupDocs.Redaction for Python via .NET — getting started (verification harness).
# Source: products/content/redaction/python-net/_index.en.md
from groupdocs.redaction import Redactor
from groupdocs.redaction.redactions import ExactPhraseRedaction, ReplacementOptions

# Adjust the redaction parameters
repl_opt = ReplacementOptions("[redacted]")
red = ExactPhraseRedaction("Data", repl_opt)

# Load your file into the Redactor instance
with Redactor("sample.pdf") as redactor:

    # Start the redaction process
    result = redactor.apply(red)

    # Export the cleaned file
    result_path = redactor.save()
