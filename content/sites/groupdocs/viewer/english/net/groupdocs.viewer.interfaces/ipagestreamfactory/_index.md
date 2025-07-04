---
title: IPageStreamFactory
second_title: GroupDocs.Viewer for .NET API Reference
description: Defines the methods that are required for instantiating and releasing output page stream.
type: docs
weight: 310
url: /net/groupdocs.viewer.interfaces/ipagestreamfactory/
---
## IPageStreamFactory interface

Defines the methods that are required for instantiating and releasing output page stream.

```csharp
public interface IPageStreamFactory
```

## Methods

| Name | Description |
| --- | --- |
| [CreatePageStream](../../groupdocs.viewer.interfaces/ipagestreamfactory/createpagestream)(int) | Creates the stream used to write output page data. |
| [ReleasePageStream](../../groupdocs.viewer.interfaces/ipagestreamfactory/releasepagestream)(int, Stream) | Releases the stream created by [`CreatePageStream`](./createpagestream) method. |

### See Also

* namespace [GroupDocs.Viewer.Interfaces](../../groupdocs.viewer.interfaces)
* assembly [GroupDocs.Viewer](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.viewer.dll -->
