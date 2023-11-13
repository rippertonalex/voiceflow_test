from fastapi import FastAPI
import asyncio

app = FastAPI()


@app.get("/delayed-api")
async def delayed_api():
    # Simulate a delay of 10 seconds (adjust as needed)
    await asyncio.sleep(10)

    # Return a dummy response
    return {"message": "Delayed API response"}


if __name__ == "__main__":
    import uvicorn

    # Run the FastAPI application
    uvicorn.run(app, host="127.0.0.1", port=8000)