---
title: GetFormattedText
second_title: Referencia de API de GroupDocs.Parser para .NET
description: Extrae un texto formateado del documento.
type: docs
weight: 80
url: /es/net/groupdocs.parser/parser/getformattedtext/
---
## GetFormattedText(FormattedTextOptions) {#getformattedtext}

Extrae un texto formateado del documento.

```csharp
public TextReader GetFormattedText(FormattedTextOptions options)
```

| Parámetro | Escribe | Descripción |
| --- | --- | --- |
| options | FormattedTextOptions | Las opciones de extracción de texto formateado. |

### Valor_devuelto

Una instancia deTextReader clase con el texto extraído; `nulo` si la extracción de texto con formato no es compatible.

### Observaciones

**Aprende más:**

* [Extraer texto formateado del documento](https://docs.groupdocs.com/display/parsernet/Extract+formatted+text+from+document)
* Extraer un texto de documento como[HTML](https://docs.groupdocs.com/display/parsernet/HTML)
* Extraer un texto de documento como[Reducción](https://docs.groupdocs.com/display/parsernet/Markdown)
* Extraer un texto de documento como[Texto sin formato](https://docs.groupdocs.com/display/parsernet/Plain+text)

### Ejemplos

El siguiente ejemplo muestra cómo extraer el texto de un documento como texto HTML:

```csharp
// Crea una instancia de la clase Parser
using (Parser parser = new Parser(filePath))
{
    // Extraer un texto formateado en el lector
    using (TextReader reader = parser.GetFormattedText(new FormattedTextOptions(FormattedTextMode.Html)))
    {
        // Imprime un texto formateado del documento
        // Si no se admite la extracción de texto con formato, un lector es nulo
        Console.WriteLine(reader == null ? "Formatted text extraction isn't suppported" : reader.ReadToEnd());
    }
}
```

### Ver también

* class [FormattedTextOptions](../../../groupdocs.parser.options/formattedtextoptions)
* class [Parser](../../parser)
* espacio de nombres [GroupDocs.Parser](../../parser)
* asamblea [GroupDocs.Parser](../../../)

---

## GetFormattedText(int, FormattedTextOptions) {#getformattedtext_1}

Extrae un texto formateado de la página del documento.

```csharp
public TextReader GetFormattedText(int pageIndex, FormattedTextOptions options)
```

| Parámetro | Escribe | Descripción |
| --- | --- | --- |
| pageIndex | Int32 | El índice de página de base cero. |
| options | FormattedTextOptions | Las opciones de extracción de texto formateado. |

### Valor_devuelto

Una instancia deTextReaderclase con el texto extraído; `nulo` si no se admite la extracción de páginas de texto con formato.

### Observaciones

**Aprende más:**

* [Extraer texto formateado de la página del documento](https://docs.groupdocs.com/display/parsernet/Extract+formatted+text+from+document+page)
* Extraer un texto de documento como[HTML](https://docs.groupdocs.com/display/parsernet/HTML)
* Extraer un texto de documento como[Reducción](https://docs.groupdocs.com/display/parsernet/Markdown)
* Extraer un texto de documento como[Texto sin formato](https://docs.groupdocs.com/display/parsernet/Plain+text)

### Ejemplos

El siguiente ejemplo muestra cómo extraer el texto de una página de documento como texto Markdown:

```csharp
// Crea una instancia de la clase Parser
using (Parser parser = new Parser(filePath))
{
    // Comprobar si el documento admite la extracción de texto formateado
    if (!parser.Features.FormattedText)
    {
        Console.WriteLine("Document isn't supports formatted text extraction.");
        return;
    }
    
    // Obtener la información del documento
    IDocumentInfo documentInfo = parser.GetDocumentInfo();
    // Comprobar si el documento tiene páginas
    if (documentInfo.PageCount == 0)
    {
        Console.WriteLine("Document hasn't pages.");
        return;
    }
    
    // Iterar sobre páginas
    for (int p = 0; p<documentInfo.PageCount; p++)
    {
        // Imprimir un número de página 
        Console.WriteLine(string.Format("Page {0}/{1}", p + 1, documentInfo.PageCount));
        // Extraer un texto formateado en el lector
        using (TextReader reader = parser.GetFormattedText(p, new FormattedTextOptions(FormattedTextMode.Markdown)))
        {
            // Imprime un texto formateado del documento
            // Ignoramos la comprobación de nulos ya que hemos comprobado anteriormente la compatibilidad con la función de extracción de texto formateado
            Console.WriteLine(reader.ReadToEnd());
        }
    }
}
```

### Ver también

* class [FormattedTextOptions](../../../groupdocs.parser.options/formattedtextoptions)
* class [Parser](../../parser)
* espacio de nombres [GroupDocs.Parser](../../parser)
* asamblea [GroupDocs.Parser](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Parser.dll -->