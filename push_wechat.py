import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/")
async def my_data(aa,bb):
    kk = aa + bb
    return {"message": "%s" % kk}




if __name__ == '__main__':
    uvicorn.run(app='push_wechat:app', host="127.0.0.1", port=8000, reload=True, debug=True)