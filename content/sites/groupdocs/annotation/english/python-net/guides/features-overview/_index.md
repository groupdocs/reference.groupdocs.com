---
title: Features Overview
linkTitle: "Features overview"
second_title: GroupDocs.Annotation for Python via .NET API References
description: 
type: docs
url: /python-net/guides/features-overview/
is_root: false
weight: 20
---


GroupDocs.Annotation for Python via .NET adds annotations, markup, and review comments across a wide range of [supported document formats](https://docs.groupdocs.com/annotation/python-net/supported-document-formats/). Every annotation follows the same workflow: open a document with [`Annotator`](/annotation/python-net/groupdocs.annotation/annotator/), add one or more annotations with `add()`, then `save()` the result — back to the original format or to another supported format. The capabilities below can be combined freely in a single pass.

## Text markup

Mark up the text of a document with highlight, underline, strikeout, and squiggly-underline annotations, or replace and redact text. Text-markup annotations are positioned with a list of [`Point`](/annotation/python-net/groupdocs.annotation.models/point/) objects that describe the region they cover, and you can set colors such as `font_color`, `underline_color`, and `squiggly_color` (all passed as packed ARGB integers). See [Add Annotations](https://docs.groupdocs.com/annotation/python-net/developer-guide/basic-usage/add-annotations/).

## Graphic (shape) annotations

Draw geometric shapes over a page — area (rectangle), ellipse, point, arrow, distance, and polyline. Box-style shapes use a [`Rectangle`](/annotation/python-net/groupdocs.annotation.models/rectangle/) (`box`) for position and size, while line-based shapes use [`Point`](/annotation/python-net/groupdocs.annotation.models/point/) coordinates. You can configure fill and pen colors (as ARGB integers) and the pen style. See [Add Annotations](https://docs.groupdocs.com/annotation/python-net/developer-guide/basic-usage/add-annotations/).

## Watermarks, text fields, links, and image stamps

Add a [`WatermarkAnnotation`](/annotation/python-net/groupdocs.annotation.models.annotation_models/watermarkannotation/) over a page, an editable [`TextFieldAnnotation`](/annotation/python-net/groupdocs.annotation.models.annotation_models/textfieldannotation/), a clickable [`LinkAnnotation`](/annotation/python-net/groupdocs.annotation.models.annotation_models/linkannotation/), or stamp an [`ImageAnnotation`](/annotation/python-net/groupdocs.annotation.models.annotation_models/imageannotation/) onto the document. These rich annotations let you label, brand, or augment a document without altering its underlying content. See [Add Annotations](https://docs.groupdocs.com/annotation/python-net/developer-guide/basic-usage/add-annotations/).

## Comments and replies

Attach an author and threaded review comments to any annotation. Each annotation carries a `user` ([`User`](/annotation/python-net/groupdocs.annotation.models/user/) with a [`Role`](/annotation/python-net/groupdocs.annotation.models/role/) of viewer or editor) and a list of `replies` ([`Reply`](/annotation/python-net/groupdocs.annotation.models/reply/) objects with a comment, an author, and a timestamp), so you can model a full review conversation. See [Comments and Replies](https://docs.groupdocs.com/annotation/python-net/developer-guide/basic-usage/comments-and-replies/).

## Managing annotations

Add, update, get, and remove annotations. Retrieve all annotations, or filter by type with `get(type=AnnotationType.X)`; remove a single annotation by id or instance, or clear them all. See [Get Annotations](https://docs.groupdocs.com/annotation/python-net/developer-guide/basic-usage/get-annotations/) and [Remove Annotations](https://docs.groupdocs.com/annotation/python-net/developer-guide/basic-usage/remove-annotations/).

## Document information

Inspect a document before annotating it — read the page count, file type, page dimensions, and size through `get_document_info()`, and list every format the API supports with `FileType.get_supported_file_types()`. See [Get Document Info](https://docs.groupdocs.com/annotation/python-net/developer-guide/basic-usage/get-document-info/) and [Supported File Formats](https://docs.groupdocs.com/annotation/python-net/developer-guide/basic-usage/get-supported-file-formats/).

## Loading and saving

Load documents from a local path or from a stream, including password-protected files, by passing [`LoadOptions`](/annotation/python-net/groupdocs.annotation.options/loadoptions/). When saving, write back to the original format, save to a different path, restrict the output to specific pages with `SaveOptions.first_page`/`last_page` (1-based), or save only certain annotation types. See [Loading Documents](https://docs.groupdocs.com/annotation/python-net/developer-guide/advanced-usage/loading-documents/) and [Saving Documents](https://docs.groupdocs.com/annotation/python-net/developer-guide/advanced-usage/saving-documents/).

## On-premise

GroupDocs.Annotation for Python via .NET runs entirely on your own infrastructure — your documents never leave your environment. The package is a self-contained wheel that bundles everything it needs, so no Microsoft Office, OpenOffice, Adobe Acrobat, or separate runtime has to be installed. See [System Requirements](https://docs.groupdocs.com/annotation/python-net/system-requirements/) for the supported platforms and native dependencies.
</content>
</invoke>
