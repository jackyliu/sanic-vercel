from sanic import Sanic
from sanic.response import json
app = Sanic()
 
 
@app.route('/')
@app.route('/<path:path>')
async def index(request, path=""):
    return json({'hello': path})

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=3000)
