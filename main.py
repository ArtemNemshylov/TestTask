import json
from fastapi.responses import JSONResponse
from fastapi import FastAPI

app = FastAPI()


class CustomJSONResponse(JSONResponse):
    def render(self, content: any) -> bytes:
        return json.dumps(
            content,
            ensure_ascii=False,
            indent=4,
            separators=(',', ': ')
        ).encode('utf-8')


@app.get('/')
def all_prods():
    with open('result.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data


@app.get('/{name}')
def prod(name):
    with open('result.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
        return data[name]


@app.get('/{name}/{key}')
def prod_value(name, value):
    with open('result.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
        return data[name][value]
