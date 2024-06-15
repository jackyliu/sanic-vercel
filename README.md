# Vercel of Sanic

## Deploy

### 使用 Vercel 进行部署

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/import/project?template=https://github.com/jasminebd/sanic-vercel)

### sanic.app.Sanic 实例

```python
#api/index.py
from sanic import Sanic
from sanic.response import json
app = Sanic("app")

@app.route('/')
@app.route('/<path:path>')
async def index(request, path=""):
    return json({'hello': path})
```

![screenshot](images/screenshot.png)

[Vercel](https://vercel.com/docs/functions/runtimes/python#asynchronous-server-gateway-interface) | [Sanic](https://sanic.dev/en)
