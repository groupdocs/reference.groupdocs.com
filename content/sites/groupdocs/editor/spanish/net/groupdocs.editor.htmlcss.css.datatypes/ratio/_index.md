---
title: Ratio
second_title: Referencia de API de GroupDocs.Editor para .NET
description: Representa un tipo de datos CSS de proporción que se utiliza para describir relaciones de aspecto en consultas de medios y para imágenes ráster al indicar la proporción entre dos valores sin unidad llamados numerador y denominador. Estructura inmutable.
type: docs
weight: 280
url: /es/net/groupdocs.editor.htmlcss.css.datatypes/ratio/
---
## Ratio structure

Representa un tipo de datos CSS de "proporción", que se utiliza para describir relaciones de aspecto en consultas de medios y para imágenes ráster al indicar la proporción entre dos valores sin unidad llamados "numerador" y "denominador". Estructura inmutable.

```csharp
public struct Ratio : ICloneable, ICssDataType, IEquatable<Ratio>
```

## Propiedades

| Nombre | Descripción |
| --- | --- |
| [Denominator](../../groupdocs.editor.htmlcss.css.datatypes/ratio/denominator) { get; } | Devuelve un denominador de esta razón |
| [Numerator](../../groupdocs.editor.htmlcss.css.datatypes/ratio/numerator) { get; } | Devuelve un numerador de esta razón |

## Métodos

| Nombre | Descripción |
| --- | --- |
| static [Create](../../groupdocs.editor.htmlcss.css.datatypes/ratio/create)(ushort, ushort) | Crea y devuelve una instancia de Ratio a partir del numerador y el denominador especificados |
| [Calculate](../../groupdocs.editor.htmlcss.css.datatypes/ratio/calculate)() | Calcula y devuelve esta relación como un único número de punto flotante |
| [Clone](../../groupdocs.editor.htmlcss.css.datatypes/ratio/clone)() | Devuelve una copia completa de este ratio |
| override [Equals](../../groupdocs.editor.htmlcss.css.datatypes/ratio/equals#equals_1)(object) | Determina si esta instancia es igual al objeto no emitido especificado, que presumiblemente es otra instancia de "Ratio" |
| [Equals](../../groupdocs.editor.htmlcss.css.datatypes/ratio/equals#equals)(Ratio) | Determina si esta instancia es igual a la instancia "Ratio" especificada |
| override [GetHashCode](../../groupdocs.editor.htmlcss.css.datatypes/ratio/gethashcode)() | Devuelve un código hash para esta instancia, que no se puede cambiar durante su vigencia |
| [GetInverseRatio](../../groupdocs.editor.htmlcss.css.datatypes/ratio/getinverseratio)() | Genera y devuelve una relación inversa (recíproca) para esta relación |
| [SerializeDefault](../../groupdocs.editor.htmlcss.css.datatypes/ratio/serializedefault)() | Serializa esta relación a la cadena y la devuelve |
| override [ToString](../../groupdocs.editor.htmlcss.css.datatypes/ratio/tostring)() | Devuelve una representación de cadena de esta relación; igual que "SerializeDefault()" |
| [operator ==](../../groupdocs.editor.htmlcss.css.datatypes/ratio/op_equality) | Compara dos razones y devuelve un valor booleano que indica si las dos coinciden. |
| [operator !=](../../groupdocs.editor.htmlcss.css.datatypes/ratio/op_inequality) | Compara dos razones y devuelve un valor booleano que indica si las dos no coinciden. |

## Campos

| Nombre | Descripción |
| --- | --- |
| static readonly [Single](../../groupdocs.editor.htmlcss.css.datatypes/ratio/single) | Proporción predeterminada única 1/1 |

### Observaciones

https://developer.mozilla.org/en-US/docs/Web/CSS/ratio

### Ver también

* interface [ICssDataType](../icssdatatype)
* espacio de nombres [GroupDocs.Editor.HtmlCss.Css.DataTypes](../../groupdocs.editor.htmlcss.css.datatypes)
* asamblea [GroupDocs.Editor](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Editor.dll -->
