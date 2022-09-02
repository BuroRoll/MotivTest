from fastapi import FastAPI, Query
from typing import Union

from repository.content import get_content_info

app = FastAPI()


@app.get("/")
async def read_items(hash: Union[int, None] = Query(default=None)):
    if not hash:
        return {'error': 'empty request'}
    content_data = get_content_info(hash)
    return content_data
