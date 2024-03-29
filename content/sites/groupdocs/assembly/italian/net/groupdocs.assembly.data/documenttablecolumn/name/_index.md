---
title: Name
second_title: Riferimento API GroupDocs.Assembly per .NET
description: Ottiene o imposta il nome di questa colonna utilizzata per accedere ai dati della colonna in un documento modello passato a DocumentAssemblergroupdocs.assembly/documentassembler .
type: docs
weight: 30
url: /it/net/groupdocs.assembly.data/documenttablecolumn/name/
---
## DocumentTableColumn.Name property

Ottiene o imposta il nome di questa colonna utilizzata per accedere ai dati della colonna in un documento modello passato a [`DocumentAssembler`](../../../groupdocs.assembly/documentassembler) .

```csharp
public string Name { get; set; }
```

### Osservazioni

Se il nome della colonna viene letto da un documento (vedi[`FirstRowContainsColumnNames`](../../documenttableoptions/firstrowcontainscolumnnames) ), il nome viene corretto automaticamente in modo che sia valido. Tuttavia, se il nome della colonna viene impostato manualmente tramite questa proprietà e il nome non è valido, viene generata un'eccezione.

Il nome della colonna è considerato valido se sono soddisfatte le seguenti condizioni:

* Il nome non è vuoto.
* Il primo carattere del nome è una lettera o un trattino basso.
* Il resto dei caratteri del nome sono lettere, trattini bassi, cifre o i seguenti caratteri: '@', '#', '$'.
* Il corrispondente[`DocumentTable`](../../documenttable) l'oggetto non contiene a[`DocumentTableColumn`](../../documenttablecolumn) istanza con lo stesso nome.

### Guarda anche

* class [DocumentTableColumn](../../documenttablecolumn)
* spazio dei nomi [GroupDocs.Assembly.Data](../../documenttablecolumn)
* assemblea [GroupDocs.Assembly](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Assembly.dll -->
