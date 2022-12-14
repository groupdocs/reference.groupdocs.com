---
title: CreateFilePathRegularExpression
second_title: GroupDocs.Suche nach .NET-API-Referenz
description: Erstellt einen Filter zum Überspringen von Dokumenten die keinem regulären Ausdruck entsprechen. Der reguläre Ausdruck wird auf den vollständigen Pfad eines Dokuments angewendet.
type: docs
weight: 40
url: /de/net/groupdocs.search.options/searchdocumentfilter/createfilepathregularexpression/
---
## CreateFilePathRegularExpression(string) {#createfilepathregularexpression}

Erstellt einen Filter zum Überspringen von Dokumenten, die keinem regulären Ausdruck entsprechen. Der reguläre Ausdruck wird auf den vollständigen Pfad eines Dokuments angewendet.

```csharp
public static ISearchDocumentFilter CreateFilePathRegularExpression(string pattern)
```

| Parameter | Typ | Beschreibung |
| --- | --- | --- |
| pattern | String | Das reguläre Ausdrucksmuster. |

### Rückgabewert

Ein Suchdokumentfilter nach Dateiname.

### Siehe auch

* interface [ISearchDocumentFilter](../../isearchdocumentfilter)
* class [SearchDocumentFilter](../../searchdocumentfilter)
* namensraum [GroupDocs.Search.Options](../../searchdocumentfilter)
* Montage [GroupDocs.Search](../../../)

---

## CreateFilePathRegularExpression(string, RegexOptions) {#createfilepathregularexpression_1}

Erstellt einen Filter zum Überspringen von Dokumenten, die keinem regulären Ausdruck entsprechen. Der reguläre Ausdruck wird auf den vollständigen Pfad eines Dokuments angewendet.

```csharp
public static ISearchDocumentFilter CreateFilePathRegularExpression(string pattern, 
    RegexOptions options)
```

| Parameter | Typ | Beschreibung |
| --- | --- | --- |
| pattern | String | Das reguläre Ausdrucksmuster. |
| options | RegexOptions | Die Optionen für reguläre Ausdrücke. |

### Rückgabewert

Ein Suchdokumentfilter nach Dateiname.

### Siehe auch

* interface [ISearchDocumentFilter](../../isearchdocumentfilter)
* class [SearchDocumentFilter](../../searchdocumentfilter)
* namensraum [GroupDocs.Search.Options](../../searchdocumentfilter)
* Montage [GroupDocs.Search](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Search.dll -->
