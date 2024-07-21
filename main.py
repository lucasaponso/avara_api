from fastapi import FastAPI, Response, status
import routes.example_route as example_route

app = FastAPI()

app.include_router(example_route.router)

@app.get("/", tags=["Debugging"], status_code=status.HTTP_200_OK, description="A basic root API endpoint to check whether the API is running.")
def read_root():
    return Response("Server is Up\n")
