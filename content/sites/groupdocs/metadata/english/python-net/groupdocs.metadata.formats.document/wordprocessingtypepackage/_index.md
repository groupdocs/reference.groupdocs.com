﻿---
title: WordProcessingTypePackage class
second_title: GroupDocs.Metadata for Python via .NET API References
description: 
type: docs
url: /python-net/groupdocs.metadata.formats.document/wordprocessingtypepackage/
is_root: false
weight: 390
---

## WordProcessingTypePackage class

Represents a metadata package containing document-specific file format information.



**Inheritance:** [`WordProcessingTypePackage`](/metadata/python-net/groupdocs.metadata.formats.document/wordprocessingtypepackage) → 
[`FileTypePackage`](/metadata/python-net/groupdocs.metadata.common/filetypepackage) → 
[`CustomPackage`](/metadata/python-net/groupdocs.metadata.common/custompackage) → 
[`MetadataPackage`](/metadata/python-net/groupdocs.metadata.common/metadatapackage)



The WordProcessingTypePackage type exposes the following members:

### Properties
| Property | Description |
| :- | :- |
| [metadata_type](/metadata/python-net/groupdocs.metadata.formats.document/wordprocessingtypepackage/metadata_type) | Gets the metadata type. |
| [keys](/metadata/python-net/groupdocs.metadata.formats.document/wordprocessingtypepackage/keys) | Gets a collection of the metadata property names. |
| [property_descriptors](/metadata/python-net/groupdocs.metadata.formats.document/wordprocessingtypepackage/property_descriptors) | Gets a collection of descriptors that contain information about properties accessible through the GroupDocs.Metadata search engine. |
| [count](/metadata/python-net/groupdocs.metadata.formats.document/wordprocessingtypepackage/count) | Gets the number of metadata properties. |
| [file_format](/metadata/python-net/groupdocs.metadata.formats.document/wordprocessingtypepackage/file_format) | Gets the file format. |
| [mime_type](/metadata/python-net/groupdocs.metadata.formats.document/wordprocessingtypepackage/mime_type) | Gets the MIME type. |
| [extension](/metadata/python-net/groupdocs.metadata.formats.document/wordprocessingtypepackage/extension) | Gets the file extension. |
| [word_processing_format](/metadata/python-net/groupdocs.metadata.formats.document/wordprocessingtypepackage/word_processing_format) | Gets the exact word processing format. |


### Methods
| Method | Description |
| :- | :- |
| [contains](/metadata/python-net/groupdocs.metadata.formats.document/wordprocessingtypepackage/contains/#str) | Determines whether the package contains a metadata property with the specified name. |
| [find_properties](/metadata/python-net/groupdocs.metadata.formats.document/wordprocessingtypepackage/find_properties/#groupdocs.metadata.search.Specification) | Finds the metadata properties satisfying a specification. <br/>The search is recursive so it affects all nested packages as well. |
| [update_properties](/metadata/python-net/groupdocs.metadata.formats.document/wordprocessingtypepackage/update_properties/#groupdocs.metadata.search.Specification-groupdocs.metadata.common.PropertyValue) | Updates known metadata properties satisfying a specification.<br/>The operation is recursive so it affects all nested packages as well. |
| [remove_properties](/metadata/python-net/groupdocs.metadata.formats.document/wordprocessingtypepackage/remove_properties/#groupdocs.metadata.search.Specification) | Removes metadata properties satisfying a specification. |
| [add_properties](/metadata/python-net/groupdocs.metadata.formats.document/wordprocessingtypepackage/add_properties/#groupdocs.metadata.search.Specification-groupdocs.metadata.common.PropertyValue) | Adds known metadata properties satisfying the specification.<br/>The operation is recursive so it affects all nested packages as well. |
| [set_properties](/metadata/python-net/groupdocs.metadata.formats.document/wordprocessingtypepackage/set_properties/#groupdocs.metadata.search.Specification-groupdocs.metadata.common.PropertyValue) | Sets known metadata properties satisfying the specification.<br/>The operation is recursive so it affects all nested packages as well.<br/>This method is a combination of [`MetadataPackage.add_properties`](/metadata/python-net/groupdocs.metadata.common/metadatapackage/add_properties) and [`MetadataPackage.update_properties`](/metadata/python-net/groupdocs.metadata.common/metadatapackage/update_properties). <br/>If an existing property satisfies the specification its value is updated. <br/>If there is a known property missing in the package that satisfies the specification it is added to the package. |
| [sanitize](/metadata/python-net/groupdocs.metadata.formats.document/wordprocessingtypepackage/sanitize/#) | Removes writable metadata properties from the package.<br/>The operation is recursive so it affects all nested packages as well. |



### See Also
* module [`groupdocs.metadata.formats.document`](..)
* class [`CustomPackage`](/metadata/python-net/groupdocs.metadata.common/custompackage)
* class [`FileTypePackage`](/metadata/python-net/groupdocs.metadata.common/filetypepackage)
* class [`MetadataPackage`](/metadata/python-net/groupdocs.metadata.common/metadatapackage)
* class [`WordProcessingTypePackage`](/metadata/python-net/groupdocs.metadata.formats.document/wordprocessingtypepackage)
