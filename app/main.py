from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import os

from routers import user_api  # ⬅️ Import router API

app = FastAPI()

# Gắn router
app.include_router(user_api.router)

# Mount thư mục static/html/ thành URL /static/
app.mount("/static", StaticFiles(directory="static/html"), name="static")

# Trả về HTML khi truy cập "/"
@app.get("/")
def serve_index():
    return FileResponse(os.path.join("static", "html", "index.html"))

if __name__ == "__main__":
    import uvicorn

    # Lấy PORT từ env, mặc định là 8000 nếu không có
    port = int(os.getenv("PORT", 8000))

    uvicorn.run("main:app", host="0.0.0.0", port=port, reload=True)
