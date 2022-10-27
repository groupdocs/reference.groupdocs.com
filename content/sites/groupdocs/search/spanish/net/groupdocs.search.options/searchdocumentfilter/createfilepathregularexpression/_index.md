---
title: CreateFilePathRegularExpression
second_title: GroupDocs.Buscar referencia de API de .NET
description: Crea un filtro para omitir documentos que no coinciden con una expresión regular. La expresión regular se aplica a la ruta completa de un documento.
type: docs
weight: 40
url: /es/net/groupdocs.search.options/searchdocumentfilter/createfilepathregularexpression/
---
## CreateFilePathRegularExpression(string) {#createfilepathregularexpression}

Crea un filtro para omitir documentos que no coinciden con una expresión regular. La expresión regular se aplica a la ruta completa de un documento.

```csharp
public static ISearchDocumentFilter CreateFilePathRegularExpression(string pattern)
```

| Parámetro | Escribe | Descripción |
| --- | --- | --- |
| pattern | String | El patrón de expresión regular. |

### Valor_devuelto

Un filtro de documentos de búsqueda por nombre de archivo.

### Ver también

* interface [ISearchDocumentFilter](../../isearchdocumentfilter)
* class [SearchDocumentFilter](../../searchdocumentfilter)
* espacio de nombres [GroupDocs.Search.Options](../../searchdocumentfilter)
* asamblea [GroupDocs.Search](../../../)

---

## CreateFilePathRegularExpression(string, RegexOptions) {#createfilepathregularexpression_1}

Crea un filtro para omitir documentos que no coinciden con una expresión regular. La expresión regular se aplica a la ruta completa de un documento.

```csharp
public static ISearchDocumentFilter CreateFilePathRegularExpression(string pattern, 
    RegexOptions options)
```

| Parámetro | Escribe | Descripción |
| --- | --- | --- |
| pattern | String | El patrón de expresión regular. |
| options | RegexOptions | Las opciones de expresiones regulares. |

### Valor_devuelto

Un filtro de documentos de búsqueda por nombre de archivo.

### Ver también

* interface [ISearchDocumentFilter](../../isearchdocumentfilter)
* class [SearchDocumentFilter](../../searchdocumentfilter)
* espacio de nombres [GroupDocs.Search.Options](../../searchdocumentfilter)
* asamblea [GroupDocs.Search](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Search.dll -->