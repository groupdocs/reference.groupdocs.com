// GroupDocs.Assembly for Java — getting started (verification harness).
import com.groupdocs.assembly.*;

public class Example {
    public static void main(String[] args) throws Exception {
        // Path to the main template
        String template = "chart_template.docx";

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
        asm.assembleDocument(template, "result.docx", data, design);
    }
}
