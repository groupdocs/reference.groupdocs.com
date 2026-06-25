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
| conversion  |  ✓   |  ✓   |   ✓    |   ✓³    |
| annotation  |  ✓   |  ✓   |  n/a¹  |  n/a⁴   |
| viewer      |  ✓   |  ✓   |   ✓    |   ✓³    |
| signature   |  ✓   |  ✓   |   ✓²   |  der⁵   |

✓ compile-verified against the real SDK.

¹ `groupdocs-annotation-net` on PyPI is a **0.0.0 stub**, so annotation/Python can't be verified yet;
the family page falls back to the `pip install` command.
² the official products snippet was outdated — corrected to the current API
(`TextSignOptions` in `groupdocs.signature.options`, `Color` in `groupdocs.pydrawing`, snake_case members).
³ Node.js compile-run via a prebuilt `node-java` binary.
⁴ no `@groupdocs/groupdocs.*` npm package → no Node.js tab.
⁵ **der** = snippet **derived from the verified Java snippet**. Of the 6 products with a Node.js tab,
conversion & viewer are compile-run via a prebuilt `node-java`; **signature, merger, metadata, and
editor** ship derived Node.js snippets because `node-java`'s native build fails on Node 22 in this
environment (no usable prebuilt), so they can't be locally compile-run. The derivation follows the
proven conversion/viewer node-java pattern (`groupdocs.<ClassName>`, camelCase methods, explicit
`.close()`).

The other products' .NET/Java/Python are verified the same way. No Node.js tab for: annotation,
assembly, classification, markdown, parser, redaction (no npm package); and comparison, search,
watermark (npm package exists, but the site has no Node.js API-reference content for them yet).
