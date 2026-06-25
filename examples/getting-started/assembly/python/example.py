# GroupDocs.Assembly for Python via .NET — getting started (verification harness).
# Source: products/content/assembly/python-net/_index.en.md
import groupdocs.assembly as ga

def run():
    # Path to the main template
    template = "chart_template.docx"

    # Retrieve managers' productivity data from the source
    data_table = ga.data.DocumentTable("Managers.json", 1)

    # Create an instance of DataSourceInfo with the data
    data = ga.DataSourceInfo(data_table, "managers")

    # Set chart colors using another DataSourceInfo
    design = ga.DataSourceInfo("red", "color")

    # Fill the template with data and save it to the output
    asm = ga.DocumentAssembler()
    asm.assemble_document(template, "result.docx",
        data, design)
run()

