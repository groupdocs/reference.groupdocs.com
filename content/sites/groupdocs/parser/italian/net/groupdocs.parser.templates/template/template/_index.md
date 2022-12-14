---
title: Template
second_title: Riferimento API GroupDocs.Parser per .NET
description: Inizializza una nuova istanza diTemplategroupdocs.parser.templates/template classe.
type: docs
weight: 10
url: /it/net/groupdocs.parser.templates/template/template/
---
## Template constructor

Inizializza una nuova istanza di[`Template`](../../template) classe.

```csharp
public Template(IEnumerable<TemplateItem> items)
```

| Parametro | Tipo | Descrizione |
| --- | --- | --- |
| items | IEnumerable`1 | La raccolta di[`TemplateItem`](../../templateitem)oggetti. |

### Esempi

Utilizzo:

```csharp
// Crea un array di campi modello
TemplateItem[] fields = new TemplateItem[]
{
   new TemplateField(new TemplateRegexPosition("From"), "From", 0),
   new TemplateField(
       new TemplateLinkedPosition("From", new Size(100, 10), new TemplateLinkedPositionEdges(false, false, false, true)),
       "FromCompany",
       0),
   new TemplateField(
       new TemplateLinkedPosition("FromCompany", new Size(100, 30), new TemplateLinkedPositionEdges(false, false, false, true)),
       "FromAddress",
       0)
};

// Crea un modello di documento
Template template = new Template(fields);
```

### Guarda anche

* class [TemplateItem](../../templateitem)
* class [Template](../../template)
* spazio dei nomi [GroupDocs.Parser.Templates](../../template)
* assemblea [GroupDocs.Parser](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Parser.dll -->
