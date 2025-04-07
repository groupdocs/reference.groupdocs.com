﻿---
title: XmpDimensions class
second_title: GroupDocs.Metadata for Python via .NET API References
description: 
type: docs
url: /python-net/groupdocs.metadata.standards.xmp/xmpdimensions/
is_root: false
weight: 120
---

## XmpDimensions class

Containing dimensions for a drawn object.



**Inheritance:** [`XmpDimensions`](/metadata/python-net/groupdocs.metadata.standards.xmp/xmpdimensions) → 
[`XmpComplexType`](/metadata/python-net/groupdocs.metadata.standards.xmp/xmpcomplextype) → 
[`XmpMetadataContainer`](/metadata/python-net/groupdocs.metadata.standards.xmp/xmpmetadatacontainer) → 
[`CustomPackage`](/metadata/python-net/groupdocs.metadata.common/custompackage) → 
[`MetadataPackage`](/metadata/python-net/groupdocs.metadata.common/metadatapackage)



The XmpDimensions type exposes the following members:

### Constructors
| Constructor | Description |
| :- | :- |
| [__init__](/metadata/python-net/groupdocs.metadata.standards.xmp/xmpdimensions/__init__/#) | Initializes a new instance of the [`XmpDimensions`](/metadata/python-net/groupdocs.metadata.standards.xmp/xmpdimensions) class. |
| [__init__](/metadata/python-net/groupdocs.metadata.standards.xmp/xmpdimensions/__init__/#float-float) | Initializes a new instance of the [`XmpDimensions`](/metadata/python-net/groupdocs.metadata.standards.xmp/xmpdimensions) class. |


### Properties
| Property | Description |
| :- | :- |
| [metadata_type](/metadata/python-net/groupdocs.metadata.standards.xmp/xmpdimensions/metadata_type) | Gets the metadata type. |
| [keys](/metadata/python-net/groupdocs.metadata.standards.xmp/xmpdimensions/keys) | Gets a collection of the metadata property names. |
| [property_descriptors](/metadata/python-net/groupdocs.metadata.standards.xmp/xmpdimensions/property_descriptors) | Gets a collection of descriptors that contain information about properties accessible through the GroupDocs.Metadata search engine. |
| [count](/metadata/python-net/groupdocs.metadata.standards.xmp/xmpdimensions/count) | Gets the number of metadata properties. |
| [prefixes](/metadata/python-net/groupdocs.metadata.standards.xmp/xmpdimensions/prefixes) | Gets the namespace prefixes that are used in the [`XmpComplexType`](/metadata/python-net/groupdocs.metadata.standards.xmp/xmpcomplextype) instance. |
| [namespace_uris](/metadata/python-net/groupdocs.metadata.standards.xmp/xmpdimensions/namespace_uris) | Gets the namespace URIs that are used in the [`XmpComplexType`](/metadata/python-net/groupdocs.metadata.standards.xmp/xmpcomplextype) instance. |
| [width](/metadata/python-net/groupdocs.metadata.standards.xmp/xmpdimensions/width) | Gets or sets the width. |
| [height](/metadata/python-net/groupdocs.metadata.standards.xmp/xmpdimensions/height) | Gets or sets the height. |
| [units](/metadata/python-net/groupdocs.metadata.standards.xmp/xmpdimensions/units) | Gets or sets the units. |


### Methods
| Method | Description |
| :- | :- |
| [contains](/metadata/python-net/groupdocs.metadata.standards.xmp/xmpdimensions/contains/#str) | Determines whether the package contains a metadata property with the specified name. |
| [find_properties](/metadata/python-net/groupdocs.metadata.standards.xmp/xmpdimensions/find_properties/#groupdocs.metadata.search.Specification) | Finds the metadata properties satisfying a specification. <br/>The search is recursive so it affects all nested packages as well. |
| [update_properties](/metadata/python-net/groupdocs.metadata.standards.xmp/xmpdimensions/update_properties/#groupdocs.metadata.search.Specification-groupdocs.metadata.common.PropertyValue) | Updates known metadata properties satisfying a specification.<br/>The operation is recursive so it affects all nested packages as well. |
| [remove_properties](/metadata/python-net/groupdocs.metadata.standards.xmp/xmpdimensions/remove_properties/#groupdocs.metadata.search.Specification) | Removes metadata properties satisfying a specification. |
| [add_properties](/metadata/python-net/groupdocs.metadata.standards.xmp/xmpdimensions/add_properties/#groupdocs.metadata.search.Specification-groupdocs.metadata.common.PropertyValue) | Adds known metadata properties satisfying the specification.<br/>The operation is recursive so it affects all nested packages as well. |
| [set_properties](/metadata/python-net/groupdocs.metadata.standards.xmp/xmpdimensions/set_properties/#groupdocs.metadata.search.Specification-groupdocs.metadata.common.PropertyValue) | Sets known metadata properties satisfying the specification.<br/>The operation is recursive so it affects all nested packages as well.<br/>This method is a combination of [`MetadataPackage.add_properties`](/metadata/python-net/groupdocs.metadata.common/metadatapackage/add_properties) and [`MetadataPackage.update_properties`](/metadata/python-net/groupdocs.metadata.common/metadatapackage/update_properties). <br/>If an existing property satisfies the specification its value is updated. <br/>If there is a known property missing in the package that satisfies the specification it is added to the package. |
| [sanitize](/metadata/python-net/groupdocs.metadata.standards.xmp/xmpdimensions/sanitize/#) | Removes writable metadata properties from the package.<br/>The operation is recursive so it affects all nested packages as well. |
| [get_xmp_representation](/metadata/python-net/groupdocs.metadata.standards.xmp/xmpdimensions/get_xmp_representation/#) | Returns string contained value in XMP format. |
| [get_namespace_uri](/metadata/python-net/groupdocs.metadata.standards.xmp/xmpdimensions/get_namespace_uri/#str) | Gets the namespace URI associated with the specified prefix. |



### See Also
* module [`groupdocs.metadata.standards.xmp`](..)
* class [`CustomPackage`](/metadata/python-net/groupdocs.metadata.common/custompackage)
* class [`MetadataPackage`](/metadata/python-net/groupdocs.metadata.common/metadatapackage)
* class [`XmpComplexType`](/metadata/python-net/groupdocs.metadata.standards.xmp/xmpcomplextype)
* class [`XmpDimensions`](/metadata/python-net/groupdocs.metadata.standards.xmp/xmpdimensions)
* class [`XmpMetadataContainer`](/metadata/python-net/groupdocs.metadata.standards.xmp/xmpmetadatacontainer)
