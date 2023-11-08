from fastapi import FastAPI, HTTPException

app = FastAPI()

def fibonacci(n: int) -> int:
    """
    Calculate the n-th Fibonacci number.

    Parameters:
    n (int): The index (n) of the Fibonacci sequence to compute.

    Returns:
    int: The n-th Fibonacci number.
    """
    if n < 0:
        raise ValueError("Input must be a non-negative integer.")
    if n == 0:
        return 0
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

@app.get("/{n}", response_model=int)
async def read_item(n: int) -> int:
    """
    Endpoint to retrieve the n-th Fibonacci number.

    Parameters:
    n (int): The index (n) of the Fibonacci sequence to retrieve.

    Responses:
    200: Return the n-th Fibonacci number.
    422: Validation error for invalid input.
    """
    try:
        return fibonacci(n)
    except ValueError as e:
        raise HTTPException(status_code=422, detail=str(e))
