# pip install uvicorn
# pip install "fastapi[all]"
# uvicorn src.main:app # 서버기동


from fastapi import FastAPI
# 공식문서 참조 https://fastapi.tiangolo.com/ko/
from pydantic import BaseModel
from typing import Union

app = FastAPI(
    title="FastAPI - Hello World code",
    description="This is the Hello World of FastAPI.",
    version="1.0.0",
)


# Pydantic모듈의 BaseModel Item 클래스 정의(Requsest Body로 받을 데이터를 정의)
class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None


@app.get("/")
def hello_world():
    return "FastAPI World!!"


@app.get("/get_test/{input_val}")
def get_test1(input_val):
    return {"values": input_val}
# http://127.0.0.1:8000/get_test/test_value_message


@app.get("/get_test2/{input_val}")
def get_test2(input_val: int, q: str):
    return {"item_id": input_val, "q": q}
# http://127.0.0.1:8000/get_test2/123?q=2424


@app.post('/post_test')
def post_test(item: Item):
    return item
# http://127.0.0.1:8000/post_test
# # JSON 샘플
# {
#     "name": "Foo Bar",
#     "description": "Foo Bar Books",
#     "price": 60,
#     "tax": 6
# }