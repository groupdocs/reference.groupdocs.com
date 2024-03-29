---
title: JpgViewOptions
second_title: Riferimento API GroupDocs.Viewer per .NET
description: Inizializza una nuova istanza diJpgViewOptionsgroupdocs.viewer.options/jpgviewoptions classe.
type: docs
weight: 10
url: /it/net/groupdocs.viewer.options/jpgviewoptions/jpgviewoptions/
---
## JpgViewOptions(CreatePageStream) {#constructor_1}

Inizializza una nuova istanza di[`JpgViewOptions`](../../jpgviewoptions) classe.

```csharp
public JpgViewOptions(CreatePageStream createPageStream)
```

| Parametro | Tipo | Descrizione |
| --- | --- | --- |
| createPageStream | CreatePageStream | Il metodo che crea un'istanza del flusso utilizzato per scrivere i dati della pagina di output. |

### Eccezioni

| eccezione | condizione |
| --- | --- |
| ArgumentNullException | Lanciato quando*createPageStream* è zero. |

### Guarda anche

* delegate [CreatePageStream](../../../groupdocs.viewer.interfaces/createpagestream)
* class [JpgViewOptions](../../jpgviewoptions)
* spazio dei nomi [GroupDocs.Viewer.Options](../../jpgviewoptions)
* assemblea [GroupDocs.Viewer](../../../)

---

## JpgViewOptions(CreatePageStream, ReleasePageStream) {#constructor_2}

Inizializza una nuova istanza di[`JpgViewOptions`](../../jpgviewoptions) classe.

```csharp
public JpgViewOptions(CreatePageStream createPageStream, ReleasePageStream releasePageStream)
```

| Parametro | Tipo | Descrizione |
| --- | --- | --- |
| createPageStream | CreatePageStream | Il metodo che crea un'istanza del flusso utilizzato per scrivere i dati della pagina di output. |
| releasePageStream | ReleasePageStream | Il metodo che rilascia il flusso creato dal metodo assegnato al delegato passato a*createPageStream* parametro. |

### Eccezioni

| eccezione | condizione |
| --- | --- |
| ArgumentNullException | Lanciato quando*createPageStream* è zero. |
| ArgumentNullException | Lanciato quando*releasePageStream* è zero. |

### Guarda anche

* delegate [CreatePageStream](../../../groupdocs.viewer.interfaces/createpagestream)
* delegate [ReleasePageStream](../../../groupdocs.viewer.interfaces/releasepagestream)
* class [JpgViewOptions](../../jpgviewoptions)
* spazio dei nomi [GroupDocs.Viewer.Options](../../jpgviewoptions)
* assemblea [GroupDocs.Viewer](../../../)

---

## JpgViewOptions(IPageStreamFactory) {#constructor_3}

Inizializza una nuova istanza di[`JpgViewOptions`](../../jpgviewoptions) classe.

```csharp
public JpgViewOptions(IPageStreamFactory pageStreamFactory)
```

| Parametro | Tipo | Descrizione |
| --- | --- | --- |
| pageStreamFactory | IPageStreamFactory | La factory che implementa i metodi per la creazione e il rilascio del flusso della pagina di output. |

### Eccezioni

| eccezione | condizione |
| --- | --- |
| ArgumentNullException | Lanciato quando*pageStreamFactory* è zero. |

### Guarda anche

* interface [IPageStreamFactory](../../../groupdocs.viewer.interfaces/ipagestreamfactory)
* class [JpgViewOptions](../../jpgviewoptions)
* spazio dei nomi [GroupDocs.Viewer.Options](../../jpgviewoptions)
* assemblea [GroupDocs.Viewer](../../../)

---

## JpgViewOptions() {#constructor}

Inizializza una nuova istanza di[`JpgViewOptions`](../../jpgviewoptions) classe.

```csharp
public JpgViewOptions()
```

### Osservazioni

Questo costruttore inizializza una nuova istanza di[`JpgViewOptions`](../../jpgviewoptions) con "p_{0}.jpg" come formato del percorso file per i file di output. I file di output verranno inseriti nella directory di lavoro corrente dell'applicazione.

### Guarda anche

* class [JpgViewOptions](../../jpgviewoptions)
* spazio dei nomi [GroupDocs.Viewer.Options](../../jpgviewoptions)
* assemblea [GroupDocs.Viewer](../../../)

---

## JpgViewOptions(string) {#constructor_4}

Inizializza una nuova istanza di[`JpgViewOptions`](../../jpgviewoptions) classe.

```csharp
public JpgViewOptions(string filePathFormat)
```

| Parametro | Tipo | Descrizione |
| --- | --- | --- |
| filePathFormat | String | Il formato del percorso del file, ad esempio "page_{0}.jpg". |

### Eccezioni

| eccezione | condizione |
| --- | --- |
| ArgumentException | Lanciato quando*filePathFormat* è nullo o vuoto. |

### Guarda anche

* class [JpgViewOptions](../../jpgviewoptions)
* spazio dei nomi [GroupDocs.Viewer.Options](../../jpgviewoptions)
* assemblea [GroupDocs.Viewer](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Viewer.dll -->
