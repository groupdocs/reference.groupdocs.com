---
title: AviHeaderFlags
second_title: Referencia de API de GroupDocs.Metadata para .NET
description: Representa banderas de encabezado AVI.
type: docs
weight: 2390
url: /es/net/groupdocs.metadata.formats.video/aviheaderflags/
---
## AviHeaderFlags enumeration

Representa banderas de encabezado AVI.

```csharp
[Flags]
public enum AviHeaderFlags
```

### Valores

| Nombre | Valor | Descripción |
| --- | --- | --- |
| HasIndex | `10` | Indica que el archivo AVI tiene un índice. |
| MustUseIndex | `20` | Indica que la aplicación debe usar el índice, en lugar del orden físico de los fragmentos en el archivo, para determinar el orden de presentación de los datos. Por ejemplo, esta bandera podría usarse para crear una lista de marcos para editar. |
| IsInterleaved | `100` | Indica que el archivo AVI está intercalado. |
| TrustCkType | `800` | Usa CKType para buscar fotogramas clave. |
| WasCaptureFile | `10000` | Indica que el archivo AVI es un archivo especialmente asignado que se usa para capturar video en tiempo real. Las aplicaciones deben advertir al usuario antes de escribir sobre un archivo con este indicador establecido porque el usuario probablemente desfragmentó este archivo. |
| Copyrighted | `20000` | Indica que el archivo AVI contiene datos y software protegidos por derechos de autor. Cuando se usa este indicador, el software no debe permitir que los datos se dupliquen. |

### Ver también

* espacio de nombres [GroupDocs.Metadata.Formats.Video](../../groupdocs.metadata.formats.video)
* asamblea [GroupDocs.Metadata](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Metadata.dll -->