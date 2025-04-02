﻿---
title: XmpPagedTextPackage class
second_title: GroupDocs.Metadata for Python via .NET API References
description: 
type: docs
url: /python-net/groupdocs.metadata.standards.xmp.schemes/xmppagedtextpackage/
is_root: false
weight: 120
---

## XmpPagedTextPackage class

Represents the XMP Paged-Text package.



**Inheritance:** [`XmpPagedTextPackage`](/metadata/python-net/groupdocs.metadata.standards.xmp.schemes/xmppagedtextpackage) → 
[`XmpPackage`](/metadata/python-net/groupdocs.metadata.standards.xmp/xmppackage) → 
[`XmpMetadataContainer`](/metadata/python-net/groupdocs.metadata.standards.xmp/xmpmetadatacontainer) → 
[`CustomPackage`](/metadata/python-net/groupdocs.metadata.common/custompackage) → 
[`MetadataPackage`](/metadata/python-net/groupdocs.metadata.common/metadatapackage)



The XmpPagedTextPackage type exposes the following members:

### Constructors
| Constructor | Description |
| :- | :- |
| [__init__](/metadata/python-net/groupdocs.metadata.standards.xmp.schemes/xmppagedtextpackage/__init__/#) | Initializes a new instance of the [`XmpPagedTextPackage`](/metadata/python-net/groupdocs.metadata.standards.xmp.schemes/xmppagedtextpackage) class. |


### Properties
| Property | Description |
| :- | :- |
| [metadata_type](/metadata/python-net/groupdocs.metadata.standards.xmp.schemes/xmppagedtextpackage/metadata_type) | Gets the metadata type. |
| [keys](/metadata/python-net/groupdocs.metadata.standards.xmp.schemes/xmppagedtextpackage/keys) | Gets a collection of the metadata property names. |
| [property_descriptors](/metadata/python-net/groupdocs.metadata.standards.xmp.schemes/xmppagedtextpackage/property_descriptors) | Gets a collection of descriptors that contain information about properties accessible through the GroupDocs.Metadata search engine. |
| [count](/metadata/python-net/groupdocs.metadata.standards.xmp.schemes/xmppagedtextpackage/count) | Gets the number of metadata properties. |
| [prefix](/metadata/python-net/groupdocs.metadata.standards.xmp.schemes/xmppagedtextpackage/prefix) | Gets the xmlns prefix. |
| [namespace_uri](/metadata/python-net/groupdocs.metadata.standards.xmp.schemes/xmppagedtextpackage/namespace_uri) | Gets the namespace URI. |
| [xml_namespace](/metadata/python-net/groupdocs.metadata.standards.xmp.schemes/xmppagedtextpackage/xml_namespace) | Gets the XML namespace. |
| [colorants](/metadata/python-net/groupdocs.metadata.standards.xmp.schemes/xmppagedtextpackage/colorants) | Gets or sets an ordered array of colorants (swatches) that are used in the document (including any in contained documents). |
| [fonts](/metadata/python-net/groupdocs.metadata.standards.xmp.schemes/xmppagedtextpackage/fonts) | Gets or sets an unordered array of fonts that are used in the document (including any in contained documents). |
| [max_page_size](/metadata/python-net/groupdocs.metadata.standards.xmp.schemes/xmppagedtextpackage/max_page_size) | Gets or sets the size of the largest page in the document (including any in contained documents). |
| [number_of_pages](/metadata/python-net/groupdocs.metadata.standards.xmp.schemes/xmppagedtextpackage/number_of_pages) | Gets or sets the number of pages in the document. |
| [plate_names](/metadata/python-net/groupdocs.metadata.standards.xmp.schemes/xmppagedtextpackage/plate_names) | Gets or set an ordered array of plate names that are needed to print the document (including any in contained documents). |


### Methods
| Method | Description |
| :- | :- |
| [set](/metadata/python-net/groupdocs.metadata.standards.xmp.schemes/xmppagedtextpackage/set/#str-str) | Sets string property. |
| [set](/metadata/python-net/groupdocs.metadata.standards.xmp.schemes/xmppagedtextpackage/set/#str-groupdocs.metadata.standards.xmp.XmpArray) | Sets the value inherited from [`XmpArray`](/metadata/python-net/groupdocs.metadata.standards.xmp/xmparray) . |
| [set](/metadata/python-net/groupdocs.metadata.standards.xmp.schemes/xmppagedtextpackage/set/#str-int) | Sets integer property. |
| [set](/metadata/python-net/groupdocs.metadata.standards.xmp.schemes/xmppagedtextpackage/set/#str-bool) | Sets boolean property. |
| [set](/metadata/python-net/groupdocs.metadata.standards.xmp.schemes/xmppagedtextpackage/set/#str-DateTime) | Sets DateTime property. |
| [set](/metadata/python-net/groupdocs.metadata.standards.xmp.schemes/xmppagedtextpackage/set/#str-float) | Sets double property. |
| [set](/metadata/python-net/groupdocs.metadata.standards.xmp.schemes/xmppagedtextpackage/set/#str-groupdocs.metadata.standards.xmp.XmpValueBase) | Sets the value inherited from [`XmpValueBase`](/metadata/python-net/groupdocs.metadata.standards.xmp/xmpvaluebase) . |
| [set](/metadata/python-net/groupdocs.metadata.standards.xmp.schemes/xmppagedtextpackage/set/#str-groupdocs.metadata.standards.xmp.XmpComplexType) | Sets the value inherited from [`XmpComplexType`](/metadata/python-net/groupdocs.metadata.standards.xmp/xmpcomplextype) . |
| [contains](/metadata/python-net/groupdocs.metadata.standards.xmp.schemes/xmppagedtextpackage/contains/#str) | Determines whether the package contains a metadata property with the specified name. |
| [find_properties](/metadata/python-net/groupdocs.metadata.standards.xmp.schemes/xmppagedtextpackage/find_properties/#groupdocs.metadata.search.Specification) | Finds the metadata properties satisfying a specification. <br/>The search is recursive so it affects all nested packages as well. |
| [update_properties](/metadata/python-net/groupdocs.metadata.standards.xmp.schemes/xmppagedtextpackage/update_properties/#groupdocs.metadata.search.Specification-groupdocs.metadata.common.PropertyValue) | Updates known metadata properties satisfying a specification.<br/>The operation is recursive so it affects all nested packages as well. |
| [remove_properties](/metadata/python-net/groupdocs.metadata.standards.xmp.schemes/xmppagedtextpackage/remove_properties/#groupdocs.metadata.search.Specification) | Removes metadata properties satisfying a specification. |
| [add_properties](/metadata/python-net/groupdocs.metadata.standards.xmp.schemes/xmppagedtextpackage/add_properties/#groupdocs.metadata.search.Specification-groupdocs.metadata.common.PropertyValue) | Adds known metadata properties satisfying the specification.<br/>The operation is recursive so it affects all nested packages as well. |
| [set_properties](/metadata/python-net/groupdocs.metadata.standards.xmp.schemes/xmppagedtextpackage/set_properties/#groupdocs.metadata.search.Specification-groupdocs.metadata.common.PropertyValue) | Sets known metadata properties satisfying the specification.<br/>The operation is recursive so it affects all nested packages as well.<br/>This method is a combination of [`MetadataPackage.add_properties`](/metadata/python-net/groupdocs.metadata.common/metadatapackage/add_properties) and [`MetadataPackage.update_properties`](/metadata/python-net/groupdocs.metadata.common/metadatapackage/update_properties). <br/>If an existing property satisfies the specification its value is updated. <br/>If there is a known property missing in the package that satisfies the specification it is added to the package. |
| [sanitize](/metadata/python-net/groupdocs.metadata.standards.xmp.schemes/xmppagedtextpackage/sanitize/#) | Removes writable metadata properties from the package.<br/>The operation is recursive so it affects all nested packages as well. |
| [get_xmp_representation](/metadata/python-net/groupdocs.metadata.standards.xmp.schemes/xmppagedtextpackage/get_xmp_representation/#) | Converts the XMP value to the XML representation. |
| [remove](/metadata/python-net/groupdocs.metadata.standards.xmp.schemes/xmppagedtextpackage/remove/#str) | Removes the property with the specified name. |
| [clear](/metadata/python-net/groupdocs.metadata.standards.xmp.schemes/xmppagedtextpackage/clear/#) | Removes all XMP properties. |



### See Also
* module [`groupdocs.metadata.standards.xmp.schemes`](..)
* class [`CustomPackage`](/metadata/python-net/groupdocs.metadata.common/custompackage)
* class [`MetadataPackage`](/metadata/python-net/groupdocs.metadata.common/metadatapackage)
* class [`XmpArray`](/metadata/python-net/groupdocs.metadata.standards.xmp/xmparray)
* class [`XmpComplexType`](/metadata/python-net/groupdocs.metadata.standards.xmp/xmpcomplextype)
* class [`XmpMetadataContainer`](/metadata/python-net/groupdocs.metadata.standards.xmp/xmpmetadatacontainer)
* class [`XmpPackage`](/metadata/python-net/groupdocs.metadata.standards.xmp/xmppackage)
* class [`XmpPagedTextPackage`](/metadata/python-net/groupdocs.metadata.standards.xmp.schemes/xmppagedtextpackage)
* class [`XmpValueBase`](/metadata/python-net/groupdocs.metadata.standards.xmp/xmpvaluebase)
