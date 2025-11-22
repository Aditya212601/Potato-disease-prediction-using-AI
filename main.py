
from fastapi import FastAPI, File, UploadFile
import uvicorn
import numpy as np
from PIL import Image

app = FastAPI()
MODEL  = tf.keras.models.load_model("../")
@app.get("/ping")
async def ping():
    return {"message": "hello world"}  # return as JSON

def read_imagefile(file) -> np.ndarray:
    image = np.array(Image.open(BytesIO(data)))
    return image    

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    image = read_imagefile(await file.read())
    return


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8888)
