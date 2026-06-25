// GroupDocs.Classification for .NET — getting started (verification harness).
// Source: products/content/classification/net/_index.en.md
using System;
using GroupDocs.Classification;

class Program { static void Main() {
// Create an instance of Classifier
var classifier = new GroupDocs.Classification.Classifier();

// Classify a PDF document using IAB-2 taxonomy
var response = classifier.Classify("document.pdf", ".", 3, Taxonomy.Iab2);

// Print the best class name and probability
Console.WriteLine(response.BestClassName);
Console.WriteLine(response.BestClassProbability);
} }
