---
title: Load
second_title: Référence de l'API GroupDocs.Conversion pour .NET
description: Définir le nom du fichier du document source
type: docs
weight: 10
url: /fr/net/groupdocs.conversion.fluent/iconversionfrom/load/
---
## Load(string) {#load_2}

Définir le nom du fichier du document source

```csharp
public IConversionLoadOptionsOrSourceDocumentLoaded Load(string fileName)
```

| Paramètre | Taper | La description |
| --- | --- | --- |
| fileName | String | Documents sources |

### Voir également

* interface [IConversionLoadOptionsOrSourceDocumentLoaded](../../iconversionloadoptionsorsourcedocumentloaded)
* interface [IConversionFrom](../../iconversionfrom)
* espace de noms [GroupDocs.Conversion.Fluent](../../iconversionfrom)
* Assemblée [GroupDocs.Conversion](../../../)

---

## Load(string[]) {#load_3}

Définir les documents sources array

```csharp
public IConversionLoadOptionsOrSourceDocumentLoaded Load(string[] fileName)
```

| Paramètre | Taper | La description |
| --- | --- | --- |
| fileName | String[] | Ensemble de documents sources |

### Voir également

* interface [IConversionLoadOptionsOrSourceDocumentLoaded](../../iconversionloadoptionsorsourcedocumentloaded)
* interface [IConversionFrom](../../iconversionfrom)
* espace de noms [GroupDocs.Conversion.Fluent](../../iconversionfrom)
* Assemblée [GroupDocs.Conversion](../../../)

---

## Load(Func&lt;Stream&gt;) {#load_1}

Définir le flux de documents source

```csharp
public IConversionLoadOptionsOrSourceDocumentLoaded Load(Func<Stream> documentStreamProvider)
```

| Paramètre | Taper | La description |
| --- | --- | --- |
| documentStreamProvider | Func`1 | Fournisseur de flux de documents source |

### Exceptions

| exception | condition |
| --- | --- |
| [InvalidConverterSettingsException](../../../groupdocs.conversion.exceptions/invalidconvertersettingsexception) |  |

### Voir également

* interface [IConversionLoadOptionsOrSourceDocumentLoaded](../../iconversionloadoptionsorsourcedocumentloaded)
* interface [IConversionFrom](../../iconversionfrom)
* espace de noms [GroupDocs.Conversion.Fluent](../../iconversionfrom)
* Assemblée [GroupDocs.Conversion](../../../)

---

## Load(Func&lt;Stream[]&gt;) {#load}

Définir les flux de documents source array

```csharp
public IConversionLoadOptionsOrSourceDocumentLoaded Load(Func<Stream[]> documentStreamProvider)
```

| Paramètre | Taper | La description |
| --- | --- | --- |
| documentStreamProvider | Func`1 | Fournisseur de flux de documents source |

### Exceptions

| exception | condition |
| --- | --- |
| [InvalidConverterSettingsException](../../../groupdocs.conversion.exceptions/invalidconvertersettingsexception) |  |

### Voir également

* interface [IConversionLoadOptionsOrSourceDocumentLoaded](../../iconversionloadoptionsorsourcedocumentloaded)
* interface [IConversionFrom](../../iconversionfrom)
* espace de noms [GroupDocs.Conversion.Fluent](../../iconversionfrom)
* Assemblée [GroupDocs.Conversion](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Conversion.dll -->
