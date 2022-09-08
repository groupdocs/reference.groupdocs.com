---
title: FromStream
second_title: GroupDocs.Viewer for .NET API Reference
description: Detects file type by reading the file signature.
type: docs
weight: 1900
url: /net/groupdocs.viewer/filetype/fromstream/
---
## FromStream(Stream) {#fromstream}

Detects file type by reading the file signature.

```csharp
public static FileType FromStream(Stream stream)
```

| Parameter | Type | Description |
| --- | --- | --- |
| stream | Stream | The file stream. |

### See Also

* class [FileType](../../filetype)
* namespace [GroupDocs.Viewer](../../filetype)
* assembly [GroupDocs.Viewer](../../../)

---

## FromStream(Stream, string) {#fromstream_2}

Detects file type by reading the file signature.

```csharp
public static FileType FromStream(Stream stream, string password)
```

| Parameter | Type | Description |
| --- | --- | --- |
| stream | Stream | The file stream. |
| password | String | The password to open the file. |

### See Also

* class [FileType](../../filetype)
* namespace [GroupDocs.Viewer](../../filetype)
* assembly [GroupDocs.Viewer](../../../)

---

## FromStream(Stream, ILogger) {#fromstream_1}

Detects file type by reading the file signature.

```csharp
public static FileType FromStream(Stream stream, ILogger logger)
```

| Parameter | Type | Description |
| --- | --- | --- |
| stream | Stream | The file stream. |
| logger | ILogger | The logger. |

### Return Value

Returns file type in case it was detected successfully otherwise returns default [`Unknown`](../unknown) file type.

### See Also

* interface [ILogger](../../../groupdocs.viewer.logging/ilogger)
* class [FileType](../../filetype)
* namespace [GroupDocs.Viewer](../../filetype)
* assembly [GroupDocs.Viewer](../../../)

---

## FromStream(Stream, string, ILogger) {#fromstream_3}

Detects file type by reading the file signature.

```csharp
public static FileType FromStream(Stream stream, string password, ILogger logger)
```

| Parameter | Type | Description |
| --- | --- | --- |
| stream | Stream | The file stream. |
| password | String | The password to open the file. |
| logger | ILogger | The logger. |

### Return Value

Returns file type in case it was detected successfully otherwise returns default [`Unknown`](../unknown) file type.

### See Also

* interface [ILogger](../../../groupdocs.viewer.logging/ilogger)
* class [FileType](../../filetype)
* namespace [GroupDocs.Viewer](../../filetype)
* assembly [GroupDocs.Viewer](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.viewer.dll -->