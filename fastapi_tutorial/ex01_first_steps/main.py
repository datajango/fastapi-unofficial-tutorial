from fastapi import FastAPI, Request

app = FastAPI()

@app.get("/")
@app.post("/")
@app.put("/")
@app.patch("/")
@app.delete("/")
@app.options("/")
@app.head("/")
@app.trace("/")
async def root(request: Request):

    method = request.method

    if method=='GET':
        return {
            "method": 'GET',
            "message": "Hello World"
        }
    elif method=='POST':
        req = await request.json()
        return {
            "method": 'POST',
            "request": req
        }
    elif method=='PATCH':
        req = await request.json()
        return {
            "method": 'PATCH',
            "request": req
        }
    elif method=='PUT':
        req = await request.json()
        return {
            "method": 'PUT',
            "request": req
        }
    elif method=='DELETE':
        req = await request.json()
        return {
            "method": 'DELETE',
            "request": req
        }
    elif method=='OPTIONS':
        return {
            "method": 'OPTIONS',
        }
    elif method=='HEAD':
        return {
            "method": 'HEAD',
        }
    elif method=='TRACE':
        return {
            "method": 'TRACE',
        }
