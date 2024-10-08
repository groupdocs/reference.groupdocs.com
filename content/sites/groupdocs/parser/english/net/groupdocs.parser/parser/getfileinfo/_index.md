---
title: GetFileInfo
second_title: GroupDocs.Parser for .NET API Reference
description: Returns the general information about a file.
type: docs
weight: 250
url: /net/groupdocs.parser/parser/getfileinfo/
---
## GetFileInfo(string) {#getfileinfo_2}

Returns the general information about a file.

```csharp
public static FileInfo GetFileInfo(string filePath)
```

| Parameter | Type | Description |
| --- | --- | --- |
| filePath | String | The path to the file. |

### Return Value

An instance of [`FileInfo`](../../../groupdocs.parser.options/fileinfo) class.

### Examples

The following code shows how to check whether a file is password-protected:

```csharp
// Get a file info
Options.FileInfo info = Parser.GetFileInfo(filePath);
// Check IsEncrypted property
Console.WriteLine(info.IsEncrypted ? "Password is required" : "");
```

### See Also

* class [FileInfo](../../../groupdocs.parser.options/fileinfo)
* class [Parser](../../parser)
* namespace [GroupDocs.Parser](../../../groupdocs.parser)
* assembly [GroupDocs.Parser](../../../)

---

## GetFileInfo(string, LoadOptions) {#getfileinfo_3}

Returns the general information about a file.

```csharp
public static FileInfo GetFileInfo(string filePath, LoadOptions loadOptions)
```

| Parameter | Type | Description |
| --- | --- | --- |
| filePath | String | The path to the file. |
| loadOptions | LoadOptions | The options to open the file. |

### Return Value

An instance of [`FileInfo`](../../../groupdocs.parser.options/fileinfo) class.

### Examples

The following code shows how to check a file type of the password-protected document:

```csharp
// Get a file info
Options.FileInfo info = Parser.GetFileInfo(filePath, new LoadOptions("password"));
// Check IsEncrypted property
Console.WriteLine(info.IsEncrypted ? "Password is required" : "");
// Print the file type
Console.WriteLine(info.FileType.ToString());
```

### See Also

* class [FileInfo](../../../groupdocs.parser.options/fileinfo)
* class [LoadOptions](../../../groupdocs.parser.options/loadoptions)
* class [Parser](../../parser)
* namespace [GroupDocs.Parser](../../../groupdocs.parser)
* assembly [GroupDocs.Parser](../../../)

---

## GetFileInfo(Stream) {#getfileinfo}

Returns the general information about a file.

```csharp
public static FileInfo GetFileInfo(Stream document)
```

| Parameter | Type | Description |
| --- | --- | --- |
| document | Stream | The source input stream. |

### Return Value

An instance of [`FileInfo`](../../../groupdocs.parser.options/fileinfo) class.

### Examples

The following code shows how to check whether a file is password-protected:

```csharp
// Get a file info
Options.FileInfo info = Parser.GetFileInfo(document);
// Check IsEncrypted property
Console.WriteLine(info.IsEncrypted ? "Password is required" : "");
```

### See Also

* class [FileInfo](../../../groupdocs.parser.options/fileinfo)
* class [Parser](../../parser)
* namespace [GroupDocs.Parser](../../../groupdocs.parser)
* assembly [GroupDocs.Parser](../../../)

---

## GetFileInfo(Stream, LoadOptions) {#getfileinfo_1}

Returns the general information about a file.

```csharp
public static FileInfo GetFileInfo(Stream document, LoadOptions loadOptions)
```

| Parameter | Type | Description |
| --- | --- | --- |
| document | Stream | The source input stream. |
| loadOptions | LoadOptions | The options to open the file. |

### Return Value

An instance of [`FileInfo`](../../../groupdocs.parser.options/fileinfo) class.

### Examples

The following code shows how to check a file type of the password-protected document:

```csharp
// Get a file info
Options.FileInfo info = Parser.GetFileInfo(document);
// Check IsEncrypted property
Console.WriteLine(info.IsEncrypted ? "Password is required" : "");
// Print the file type
Console.WriteLine(info.FileType.ToString());
```

### See Also

* class [FileInfo](../../../groupdocs.parser.options/fileinfo)
* class [LoadOptions](../../../groupdocs.parser.options/loadoptions)
* class [Parser](../../parser)
* namespace [GroupDocs.Parser](../../../groupdocs.parser)
* assembly [GroupDocs.Parser](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.parser.dll -->
