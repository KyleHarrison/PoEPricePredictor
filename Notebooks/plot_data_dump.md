---
jupyter:
  jupytext:
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.3'
      jupytext_version: 1.11.1
  kernelspec:
    display_name: PoEPricePredictor
    language: python
    name: poepricepredictor
---

```python
%load_ext autoreload
%autoreload 2
```

```python
cd ..
```

```python
import poepp
```

```python
import pandas as pd
```

```python
from poepp.data_processing import dump_processing
```

```python
file_paths = dump_processing.get_currency_file_paths()
```

```python
df = dump_processing.get_data(file_paths)
```

```python
dump_processing.plot_currency(df)
```

```python

```
