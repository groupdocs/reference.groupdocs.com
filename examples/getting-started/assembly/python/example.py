# GroupDocs.Assembly for Python via .NET - getting started (verification harness).
# Source: products/content/assembly/python-net/_index.en.md
from groupdocs.assembly import DataSourceInfo, DocumentAssembler

# Chart data: one dict per manager
managers = [
    {"Manager": "Mei", "Total_Contract_Price": 230000},
    {"Manager": "Daniel", "Total_Contract_Price": 120000},
    {"Manager": "Sofia", "Total_Contract_Price": 80000},
]

# Set chart colors using another DataSourceInfo
color = DataSourceInfo("Coral", "color")

# Fill the template with data and save it to the output
DocumentAssembler().assemble_document(
    "dynamic-chart-series-color.docx", "chart-report.docx",
    [DataSourceInfo(managers, "managers"), color])
