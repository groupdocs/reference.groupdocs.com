---
title: Name
second_title: GroupDocs.Assembly for .NET API Reference
description: Gets or sets the name of this column used to access the columns data in a template document passed to DocumentAssemblergroupdocs.assembly/documentassembler.
type: docs
weight: 30
url: /net/groupdocs.assembly.data/documenttablecolumn/name/
---
## DocumentTableColumn.Name property

Gets or sets the name of this column used to access the column's data in a template document passed to [`DocumentAssembler`](../../../groupdocs.assembly/documentassembler).

```csharp
public string Name { get; set; }
```

### Remarks

If the column's name is read from a document (see [`FirstRowContainsColumnNames`](../../documenttableoptions/firstrowcontainscolumnnames)), the name is automatically corrected so that it to be valid. However, if the column's name is set manually through this property and the name is invalid, an exception is thrown.

The column's name is considered to be valid, if the following conditions are met:

* The name is not empty.
* The name's first character is a letter or underscore.
* The rest of the name's characters are letters, underscores, digits, or the following characters: '@', '#', '$'.
* The corresponding [`DocumentTable`](../../documenttable) object does not contain a [`DocumentTableColumn`](../../documenttablecolumn) instance with the same name.

### See Also

* class [DocumentTableColumn](../../documenttablecolumn)
* namespace [GroupDocs.Assembly.Data](../../documenttablecolumn)
* assembly [GroupDocs.Assembly](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Assembly.dll -->