---
title: Password
second_title: GroupDocs.Editor for .NET API Reference
description: Allows to specify modify and obtain the password which will be used for opening the Presentation document if it is encoded. Set to NULL or empty string in order to remove the password.
type: docs
weight: 20
url: /net/groupdocs.editor.options/presentationloadoptions/password/
---
## PresentationLoadOptions.Password property

Allows to specify, modify and obtain the password, which will be used for opening the Presentation document, if it is encoded. Set to NULL or empty string in order to remove the password.

```csharp
public string Password { get; set; }
```

### Remarks

By default this property has NULL value — password is not set. If input Presentation document is password-protected, the password is mandatory and an exception will be thrown if password is not specified or is invalid. If input Presentation document is NOT password-protected, but password is set, it will be ignored.

### See Also

* class [PresentationLoadOptions](../../presentationloadoptions)
* namespace [GroupDocs.Editor.Options](../../presentationloadoptions)
* assembly [GroupDocs.Editor](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Editor.dll -->