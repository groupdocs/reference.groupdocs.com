---
title: JsonDataSource
second_title: GroupDocs.Assembly for .NET API Reference
description: Creates a new data source with data from a JSON file using default options for parsing JSON data.
type: docs
weight: 10
url: /net/groupdocs.assembly.data/jsondatasource/jsondatasource/
---
## JsonDataSource(string) {#constructor_4}

Creates a new data source with data from a JSON file using default options for parsing JSON data.

```csharp
public JsonDataSource(string jsonPath)
```

| Parameter | Type | Description |
| --- | --- | --- |
| jsonPath | String | The path to the JSON file to be used as the data source. |

### See Also

* class [JsonDataSource](../../jsondatasource)
* namespace [GroupDocs.Assembly.Data](../../../groupdocs.assembly.data)
* assembly [GroupDocs.Assembly](../../../)

---

## JsonDataSource(string, JsonDataLoadOptions) {#constructor_5}

Creates a new data source with data from a JSON file using the specified options for parsing JSON data.

```csharp
public JsonDataSource(string jsonPath, JsonDataLoadOptions options)
```

| Parameter | Type | Description |
| --- | --- | --- |
| jsonPath | String | The path to the JSON file to be used as the data source. |
| options | JsonDataLoadOptions | Options for parsing JSON data. |

### See Also

* class [JsonDataLoadOptions](../../jsondataloadoptions)
* class [JsonDataSource](../../jsondatasource)
* namespace [GroupDocs.Assembly.Data](../../../groupdocs.assembly.data)
* assembly [GroupDocs.Assembly](../../../)

---

## JsonDataSource(Stream) {#constructor}

Creates a new data source with data from a JSON stream using default options for parsing JSON data.

```csharp
public JsonDataSource(Stream jsonStream)
```

| Parameter | Type | Description |
| --- | --- | --- |
| jsonStream | Stream | The stream of JSON data to be used as the data source. |

### See Also

* class [JsonDataSource](../../jsondatasource)
* namespace [GroupDocs.Assembly.Data](../../../groupdocs.assembly.data)
* assembly [GroupDocs.Assembly](../../../)

---

## JsonDataSource(Stream, JsonDataLoadOptions) {#constructor_1}

Creates a new data source with data from a JSON stream using the specified options for parsing JSON data.

```csharp
public JsonDataSource(Stream jsonStream, JsonDataLoadOptions options)
```

| Parameter | Type | Description |
| --- | --- | --- |
| jsonStream | Stream | The stream of JSON data to be used as the data source. |
| options | JsonDataLoadOptions | Options for parsing JSON data. |

### See Also

* class [JsonDataLoadOptions](../../jsondataloadoptions)
* class [JsonDataSource](../../jsondatasource)
* namespace [GroupDocs.Assembly.Data](../../../groupdocs.assembly.data)
* assembly [GroupDocs.Assembly](../../../)

---

## JsonDataSource(string, string) {#constructor_6}

Creates a new data source with data from a JSON file using a JSON Schema file and default options for parsing JSON data.

```csharp
public JsonDataSource(string jsonPath, string jsonSchemaPath)
```

| Parameter | Type | Description |
| --- | --- | --- |
| jsonPath | String | The path to the JSON file to be used as the data source. |
| jsonSchemaPath | String | The path to the JSON Schema file describing the data. |

### Remarks

When a JSON Schema is specified, template expressions are validated against the schema rather than against the data. Members declared in the schema can be referenced in a template even if they are absent, null or empty in the data, for example, inside a conditional block whose condition is false for this data. Members not declared in the schema still cause an error, so misspelled member names are detected as usual.

Types of values come from the schema: "integer" values are represented as `long?`, "number" values as `double?`, "boolean" values as `bool?`, "string" values having "date-time" or "date" format as `DateTime?`, and other "string" values as `string`. So, [`SimpleValueParseMode`](../../jsondataloadoptions/simplevalueparsemode) and [`ExactDateTimeParseFormats`](../../jsondataloadoptions/exactdatetimeparseformats) are not applied; date-time values must follow ISO 8601. Data members not declared in the schema are ignored.

The following JSON Schema keywords are supported: "type" (including nullable types such as ["string", "null"]), "properties", "items", "format", "enum", "const", "allOf", and local "$ref" pointers (such as "#/$defs/..." or "#/definitions/..."). Keywords "oneOf", "anyOf" and "not", remote and recursive "$ref" pointers, tuple-form "items" and arrays of arrays are not supported and cause an exception.

### See Also

* class [JsonDataSource](../../jsondatasource)
* namespace [GroupDocs.Assembly.Data](../../../groupdocs.assembly.data)
* assembly [GroupDocs.Assembly](../../../)

---

## JsonDataSource(string, string, JsonDataLoadOptions) {#constructor_7}

Creates a new data source with data from a JSON file using a JSON Schema file and the specified options for parsing JSON data.

```csharp
public JsonDataSource(string jsonPath, string jsonSchemaPath, JsonDataLoadOptions options)
```

| Parameter | Type | Description |
| --- | --- | --- |
| jsonPath | String | The path to the JSON file to be used as the data source. |
| jsonSchemaPath | String | The path to the JSON Schema file describing the data. |
| options | JsonDataLoadOptions | Options for parsing JSON data. |

### Remarks

See remarks of [`JsonDataSource`](../jsondatasource) for information on how a JSON Schema is applied. Only [`AlwaysGenerateRootObject`](../../jsondataloadoptions/alwaysgeneraterootobject) of the specified options is applied when a JSON Schema is used.

### See Also

* class [JsonDataLoadOptions](../../jsondataloadoptions)
* class [JsonDataSource](../../jsondatasource)
* namespace [GroupDocs.Assembly.Data](../../../groupdocs.assembly.data)
* assembly [GroupDocs.Assembly](../../../)

---

## JsonDataSource(Stream, Stream) {#constructor_2}

Creates a new data source with data from a JSON stream using a JSON Schema stream and default options for parsing JSON data.

```csharp
public JsonDataSource(Stream jsonStream, Stream jsonSchemaStream)
```

| Parameter | Type | Description |
| --- | --- | --- |
| jsonStream | Stream | The stream of JSON data to be used as the data source. |
| jsonSchemaStream | Stream | The stream of the JSON Schema describing the data. |

### Remarks

See remarks of [`JsonDataSource`](../jsondatasource) for information on how a JSON Schema is applied.

### See Also

* class [JsonDataSource](../../jsondatasource)
* namespace [GroupDocs.Assembly.Data](../../../groupdocs.assembly.data)
* assembly [GroupDocs.Assembly](../../../)

---

## JsonDataSource(Stream, Stream, JsonDataLoadOptions) {#constructor_3}

Creates a new data source with data from a JSON stream using a JSON Schema stream and the specified options for parsing JSON data.

```csharp
public JsonDataSource(Stream jsonStream, Stream jsonSchemaStream, JsonDataLoadOptions options)
```

| Parameter | Type | Description |
| --- | --- | --- |
| jsonStream | Stream | The stream of JSON data to be used as the data source. |
| jsonSchemaStream | Stream | The stream of the JSON Schema describing the data. |
| options | JsonDataLoadOptions | Options for parsing JSON data. |

### Remarks

See remarks of [`JsonDataSource`](../jsondatasource) for information on how a JSON Schema is applied. Only [`AlwaysGenerateRootObject`](../../jsondataloadoptions/alwaysgeneraterootobject) of the specified options is applied when a JSON Schema is used.

### See Also

* class [JsonDataLoadOptions](../../jsondataloadoptions)
* class [JsonDataSource](../../jsondatasource)
* namespace [GroupDocs.Assembly.Data](../../../groupdocs.assembly.data)
* assembly [GroupDocs.Assembly](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Assembly.dll -->
