from fastapi import FastAPI

app = FastAPI()

def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

@app.get("/{n}")
async def read_item(n: int):
    return fibonacci(n)
