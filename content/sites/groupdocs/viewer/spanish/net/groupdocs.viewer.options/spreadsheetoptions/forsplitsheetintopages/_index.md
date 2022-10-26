---
title: ForSplitSheetIntoPages
second_title: Referencia de API de GroupDocs.Viewer para .NET
description: Inicializa una nueva instancia deSpreadsheetOptionsgroupdocs.viewer.options/spreadsheetoptions para convertir la hoja en páginas.
type: docs
weight: 40
url: /es/net/groupdocs.viewer.options/spreadsheetoptions/forsplitsheetintopages/
---
## ForSplitSheetIntoPages(int) {#forsplitsheetintopages}

Inicializa una nueva instancia de[`SpreadsheetOptions`](../../spreadsheetoptions) para convertir la hoja en páginas.

```csharp
public static SpreadsheetOptions ForSplitSheetIntoPages(int countRowsPerPage)
```

| Parámetro | Escribe | Descripción |
| --- | --- | --- |
| countRowsPerPage | Int32 | Las filas cuentan para incluir en cada página. |

### Valor_devuelto

Nueva instancia de[`SpreadsheetOptions`](../../spreadsheetoptions) para convertir hojas en páginas.

### Excepciones

| excepción | condición |
| --- | --- |
| ArgumentException | arrojado cuando*countRowsPerPage* es igual o menor que cero. |

### Ver también

* class [SpreadsheetOptions](../../spreadsheetoptions)
* espacio de nombres [GroupDocs.Viewer.Options](../../spreadsheetoptions)
* asamblea [GroupDocs.Viewer](../../../)

---

## ForSplitSheetIntoPages(int, int) {#forsplitsheetintopages_1}

Inicializa una nueva instancia de[`SpreadsheetOptions`](../../spreadsheetoptions) para convertir la hoja en páginas.

```csharp
public static SpreadsheetOptions ForSplitSheetIntoPages(int countRowsPerPage, 
    int countColumnsPerPage)
```

| Parámetro | Escribe | Descripción |
| --- | --- | --- |
| countRowsPerPage | Int32 | Las filas cuentan para incluir en cada página. |
| countColumnsPerPage | Int32 | Las columnas cuentan para incluir en cada página. |

### Valor_devuelto

Nueva instancia de[`SpreadsheetOptions`](../../spreadsheetoptions) para convertir hojas en páginas.

### Excepciones

| excepción | condición |
| --- | --- |
| ArgumentException | arrojado cuando*countRowsPerPage* es igual o menor que cero. |
| ArgumentException | arrojado cuando*countColumnsPerPage* es igual o menor que cero. |

### Ver también

* class [SpreadsheetOptions](../../spreadsheetoptions)
* espacio de nombres [GroupDocs.Viewer.Options](../../spreadsheetoptions)
* asamblea [GroupDocs.Viewer](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Viewer.dll -->