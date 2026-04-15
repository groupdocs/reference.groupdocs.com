---
title: IUriExportStrategy class
second_title: GroupDocs.Markdown for Python via .NET API References
description: 
type: docs
url: /markdown/python-net/groupdocs.markdown/iuriexportstrategy/
is_root: false
weight: 160
---


## IUriExportStrategy class

Defines a strategy for customizing resource URIs that are written into the Markdown output during conversion.

Implement this interface to rewrite or transform the URIs that reference images or other external resources in the generated Markdown. For example, you can prepend a CDN base URL or change relative paths to absolute URLs.

The IUriExportStrategy type exposes the following members:

### Methods
| Method | Description |
| :- | :- |
| [update_resource_uri](/markdown/python-net/groupdocs.markdown/iuriexportstrategy/update_resource_uri/#context) | Called for each resource URI that will be written to the Markdown output, allowing modification of properties on `context` to customize the resulting URI. |

### See Also
* module [`groupdocs.markdown`](/markdown/python-net/groupdocs.markdown/)
