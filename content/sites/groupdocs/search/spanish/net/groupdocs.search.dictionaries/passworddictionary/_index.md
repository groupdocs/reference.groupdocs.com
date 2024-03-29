---
title: PasswordDictionary
second_title: GroupDocs.Buscar referencia de API de .NET
description: Representa un diccionario de contraseñas de documentos.
type: docs
weight: 460
url: /es/net/groupdocs.search.dictionaries/passworddictionary/
---
## PasswordDictionary class

Representa un diccionario de contraseñas de documentos.

```csharp
public class PasswordDictionary : DictionaryBase, IEnumerable<string>
```

## Propiedades

| Nombre | Descripción |
| --- | --- |
| [Count](../../groupdocs.search.dictionaries/passworddictionary/count) { get; } | Obtiene el número de elementos contenidos en el diccionario. |

## Métodos

| Nombre | Descripción |
| --- | --- |
| [Add](../../groupdocs.search.dictionaries/passworddictionary/add)(string, string) | Añade una contraseña para un documento al diccionario. |
| [Clear](../../groupdocs.search.dictionaries/passworddictionary/clear)() | Elimina todas las contraseñas de este[`PasswordDictionary`](../passworddictionary) objeto. |
| [Contains](../../groupdocs.search.dictionaries/passworddictionary/contains)(string) | Determina si el diccionario contiene una contraseña para el documento especificado. |
| [ExportDictionary](../../groupdocs.search.dictionaries/dictionarybase/exportdictionary)(string) | Exporta el diccionario a un archivo con el nombre especificado. |
| [GetEnumerator](../../groupdocs.search.dictionaries/passworddictionary/getenumerator)() | Devuelve un enumerador que itera a través de la colección. |
| [GetPassword](../../groupdocs.search.dictionaries/passworddictionary/getpassword)(string) | Obtiene la contraseña del archivo. |
| [ImportDictionary](../../groupdocs.search.dictionaries/dictionarybase/importdictionary)(string) | Importa un diccionario del archivo especificado. |
| [Remove](../../groupdocs.search.dictionaries/passworddictionary/remove)(string) | Elimina una contraseña del documento especificado del diccionario. |

### Observaciones

**Aprende más**

* [Indexación de documentos protegidos con contraseña](https://docs.groupdocs.com/display/searchnet/Indexing+password+protected+documents)
* [Gestión de contraseñas de documentos](https://docs.groupdocs.com/display/searchnet/Document+passwords)

### Ver también

* class [DictionaryBase](../dictionarybase)
* espacio de nombres [GroupDocs.Search.Dictionaries](../../groupdocs.search.dictionaries)
* asamblea [GroupDocs.Search](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Search.dll -->
