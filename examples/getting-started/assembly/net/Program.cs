// GroupDocs.Assembly for .NET — getting started (verification harness).
// Source: products/content/assembly/net/_index.en.md
using System;
using GroupDocs.Assembly;
using GroupDocs.Assembly.Data;

class Program { static void Main() {
// Path to the main template
string template = "chart_template.docx";

// Retrieve managers' productivity data from the source
DocumentTable data_table =
    new DocumentTable("Managers.json", 1);

// Create an instance of DataSourceInfo with the data
DataSourceInfo data
    = new DataSourceInfo(data_table, "managers");

// Set chart colors using another DataSourceInfo
DataSourceInfo design =
    new DataSourceInfo("red", "color");

// Fill the template with data and save it to the output
DocumentAssembler asm = new DocumentAssembler();
asm.AssembleDocument(template, "result.docx", data, design);
} }
