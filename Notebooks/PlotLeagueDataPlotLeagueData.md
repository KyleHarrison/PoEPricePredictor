---
jupyter:
  jupytext:
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.3'
      jupytext_version: 1.10.2
  kernelspec:
    display_name: poepp
    language: python
    name: poepp
---

```python
%load_ext autoreload
%autoreload 2
```

```python
from DumpProcessing import PoEDataImporter
```

```python
poe = PoEDataImporter()
```

```python
poe.df["Exalted Orb"]
```

```python
poe.plot_currency()
```

```python

```
