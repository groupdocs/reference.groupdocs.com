---
title: FormFieldSearchOptions
second_title: Referencia de API de GroupDocs.Signature para .NET
description: Representa opciones de búsqueda para firmas de campos de formulario.
type: docs
weight: 1370
url: /es/net/groupdocs.signature.options/formfieldsearchoptions/
---
## FormFieldSearchOptions class

Representa opciones de búsqueda para firmas de campos de formulario.

```csharp
public class FormFieldSearchOptions : SearchOptions
```

## Constructores

| Nombre | Descripción |
| --- | --- |
| [FormFieldSearchOptions](formfieldsearchoptions)() | Inicializa una nueva instancia de la clase FormFieldSearchOptions con valores predeterminados. |

## Propiedades

| Nombre | Descripción |
| --- | --- |
| [AllPages](../../groupdocs.signature.options/searchoptions/allpages) { get; set; } | Indicador para buscar en cada página del documento. De forma predeterminada, este valor se establece en true. |
| [Name](../../groupdocs.signature.options/formfieldsearchoptions/name) { get; set; } | Especifica el patrón de expresión regular del nombre de la firma del campo de formulario si se debe buscar. Puede usarlo simple como "texto" o expresión regular como "abc\d+". El valor predeterminado es una cadena vacía. |
| [PageNumber](../../groupdocs.signature.options/searchoptions/pagenumber) { get; set; } | Obtiene o establece el número de página del documento para la búsqueda. El valor es opcional. |
| [PagesSetup](../../groupdocs.signature.options/searchoptions/pagessetup) { get; set; } | Opciones para especificar páginas para la búsqueda de firmas. |
| [SkipExternal](../../groupdocs.signature.options/searchoptions/skipexternal) { get; set; } | Indicador para devolver solo las firmas marcadas como IsSignature. Por defecto, el valor es falso que indica que se devuelvan todas las firmas que coincidan con los criterios especificados. |
| [Type](../../groupdocs.signature.options/formfieldsearchoptions/type) { get; set; } | Especifica el tipo de firma de campo de formulario si se debe buscar. El valor predeterminado es nulo. |
| [Value](../../groupdocs.signature.options/formfieldsearchoptions/value) { get; set; } | Especifica el valor de la firma del campo de formulario si se debe buscar. El valor predeterminado es nulo. |

### Observaciones

**Aprende más**

* Uso básico de búsqueda de firma electrónica FormField por GroupDocs. Firma: [ Cómo realizar búsquedas electrónicas de firmas FormField en un documento](https://docs.groupdocs.com/display/signaturenet/Search+for+Form+Field+e-signatures)
* Uso avanzado de configuraciones de búsqueda de firma electrónica FormField con GroupDocs.Signature: [Uso avanzado de firmas de eSearch FormField en un documento y configuraciones adicionales](https://docs.groupdocs.com/display/signaturenet/Advanced+search+for+Form+Field+signatures)

### Ver también

* class [SearchOptions](../searchoptions)
* espacio de nombres [GroupDocs.Signature.Options](../../groupdocs.signature.options)
* asamblea [GroupDocs.Signature](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Signature.dll -->
