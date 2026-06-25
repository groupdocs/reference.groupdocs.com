# Getting-started examples — verification harness

Each folder is a **minimal, runnable app** for one product + platform, embedding the exact
getting-started snippet shown on that product's family page (`reference.groupdocs.com/<product>/`).
They exist to **verify the snippets compile against the real GroupDocs SDKs**, so the family pages
never show code that doesn't build.

The verified snippets are mirrored into [`../data/getting_started.yaml`](../data/getting_started.yaml),
which `themes/docs/layouts/_default/family.html` renders into the family page's "Getting started" block.
Snippets are sourced from the official products content
(`products/content/<product>/<platform>/_index.en.md`), with imports added and, where the package API
had drifted, corrected to what the current SDK actually exposes.

## Layout

```
examples/getting-started/<product>/
  net/      example.csproj + Program.cs   → dotnet build
  java/     pom.xml + src/main/java/Example.java → mvn compile
  python/   example.py                     → import-resolve against the installed package
```

## Verify

- **.NET:**  `cd <product>/net && dotnet build`
- **Java:**  `cd <product>/java && mvn compile`
  (the GroupDocs.Signature jar has a >16 MB manifest, so its project carries
  `.mvn/jvm.config` with `-Djdk.jar.maxSignatureFileSize` raised for JDK 17+.)
- **Python:** install one package at a time into a clean env and import it — the `*-net` packages are
  .NET-backed and **conflict if several share one environment**, so verify each in isolation:
  `pip install groupdocs-<product>-net && python example.py` (running needs an input file; importing
  the modules/symbols is enough to verify the API names).

## Status

| Product     | .NET | Java | Python | Node.js |
|-------------|:----:|:----:|:------:|:-------:|
| conversion  |  ✓   |  ✓   |   ✓    |  defer  |
| annotation  |  ✓   |  ✓   |  n/a¹  |  defer  |
| viewer      |  ✓   |  ✓   |   ✓    |  defer  |
| signature   |  ✓   |  ✓   |   ✓²   |  defer  |

✓ compile-verified against the real SDK · defer = Node.js (node-java bridge) verified in a later pass;
the family page falls back to `npm i …` until then.

¹ `groupdocs-annotation-net` on PyPI is a **0.0.0 stub**, so annotation/Python can't be verified yet;
the family page falls back to the `pip install` command.
² the official products snippet was outdated — corrected to the current API
(`TextSignOptions` in `groupdocs.signature.options`, `Color` in `groupdocs.pydrawing`, snake_case members).

Remaining products (assembly, classification, comparison, editor, markdown, merger, metadata, parser,
redaction, search, watermark) are pending this same treatment.
