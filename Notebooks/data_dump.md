```python
%load_ext autoreload
%autoreload 2
```

```python
cd ..
```

```python
from poepp.data_processing.data_dump import download_files, unzip_files, ZIP_FILES
```

```python
download_files(ZIP_FILES, "data")
```

```python
unzip_files(ZIP_FILES, "data")
```
