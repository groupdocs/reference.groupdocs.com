---
title: DataSourceInfo
second_title: GroupDocs.Assembly for .NET API Reference
description: Creates a new instance of this class without any properties specified.
type: docs
weight: 10
url: /net/groupdocs.assembly/datasourceinfo/datasourceinfo/
---
## DataSourceInfo() {#constructor}

Creates a new instance of this class without any properties specified.

```csharp
public DataSourceInfo()
```

### See Also

* class [DataSourceInfo](../../datasourceinfo)
* namespace [GroupDocs.Assembly](../../datasourceinfo)
* assembly [GroupDocs.Assembly](../../../)

---

## DataSourceInfo(object) {#constructor_1}

Creates a new instance of this class with the data source object specified.

```csharp
public DataSourceInfo(object dataSource)
```

| Parameter | Type | Description |
| --- | --- | --- |
| dataSource | Object | The data source object. |

### Remarks

The data source object can be of one of the following types:

* [`XmlDataSource`](../../../groupdocs.assembly.data/xmldatasource)
* [`JsonDataSource`](../../../groupdocs.assembly.data/jsondatasource)
* [`CsvDataSource`](../../../groupdocs.assembly.data/csvdatasource)
* [`DocumentTableSet`](../../../groupdocs.assembly.data/documenttableset)
* [`DocumentTable`](../../../groupdocs.assembly.data/documenttable)
* DataSet
* DataTable
* DataRow
* IDataReader
* IDataRecord
* DataView
* DataRowView
* Any other arbitrary non-dynamic and non-anonymous .NET type

For information on how to work with data sources of different types in template documents, see template syntax reference (https://docs.groupdocs.com/display/assemblynet/Template+Syntax+-+Part+1+of+2#TemplateSyntax-Part1of2-UsingDataSources).

### See Also

* class [DataSourceInfo](../../datasourceinfo)
* namespace [GroupDocs.Assembly](../../datasourceinfo)
* assembly [GroupDocs.Assembly](../../../)

---

## DataSourceInfo(object, string) {#constructor_2}

Creates a new instance of this class with the data source object and its name specified.

```csharp
public DataSourceInfo(object dataSource, string name)
```

| Parameter | Type | Description |
| --- | --- | --- |
| dataSource | Object | The data source object. |
| name | String | The name of the data source object to be used to access the data source object in a template document. |

### Remarks

The data source object can be of one of the following types:

* [`XmlDataSource`](../../../groupdocs.assembly.data/xmldatasource)
* [`JsonDataSource`](../../../groupdocs.assembly.data/jsondatasource)
* [`CsvDataSource`](../../../groupdocs.assembly.data/csvdatasource)
* [`DocumentTableSet`](../../../groupdocs.assembly.data/documenttableset)
* [`DocumentTable`](../../../groupdocs.assembly.data/documenttable)
* DataSet
* DataTable
* DataRow
* IDataReader
* IDataRecord
* DataView
* DataRowView
* Any other arbitrary non-dynamic and non-anonymous .NET type

For information on how to work with data sources of different types in template documents, see template syntax reference (https://docs.groupdocs.com/display/assemblynet/Template+Syntax+-+Part+1+of+2#TemplateSyntax-Part1of2-UsingDataSources).

When the name of the data source object is specified, you can access the data source object and its members in a template document using the name.

When the name of the data source object is null or empty, you can still access members of the data source object in a template document using context object member access (see Template Syntax Reference for more information), but you cannot access the data source object itself.

When passing multiple [`DataSourceInfo`](../../datasourceinfo) instances to [`DocumentAssembler`](../../documentassembler), only the name of the first data source object can be null or empty. Names of the rest ones must be specified and unique.

### See Also

* class [DataSourceInfo](../../datasourceinfo)
* namespace [GroupDocs.Assembly](../../datasourceinfo)
* assembly [GroupDocs.Assembly](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Assembly.dll -->
