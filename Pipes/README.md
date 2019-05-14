# Pipes en Python

En programación, especialmente en sistemas operativos UNIX, una tuberia es una técnica para pasar información de un proceso a otro

```python
from multiprocessing import Pipe

server_pipe, client_pipe = Pipe()
```