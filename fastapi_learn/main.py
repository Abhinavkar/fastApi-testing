from fastapi import FastAPI

app=FastAPI()


@app.get('/')
def func():
    return "hey"

@app.get('/json')
def forSendingJson():
    return {"key":"value"}

@app.get("/json/{id}")
def forSendingJson(id:int):
    return {
            "data":
                {"key":id}
            }

@app.get("/json/{id}/comments")
def comments(id:int):
    return {"data":{"1","2"}}