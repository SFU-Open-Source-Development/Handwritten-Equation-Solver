## DO NOT WRITE ANY CODE IN THIS FILE
## backend code only!
from fastapi import FastAPI, UploadFile, File, status, Response

app = FastAPI()

@app.get("/", status_code=status.HTTP_200_OK)
async def main():
    return {"message": "Hello World"}

@app.post("/upload", status_code = status.HTTP_201_CREATED)
async def upload_file(response: Response, file: UploadFile = File(...)):
    try:
        # if file is not .png or .jpg, raise 422 status code
        if not file.filename.endswith(".png") and not file.filename.endswith(".jpg"):
            response.status_code = status.HTTP_422_UNPROCESSABLE_ENTITY
            return {"message": "File format not supported"}
        file_extension = file.filename[-4:]
        #Write File in image + file_extension format
        with open("image"+file_extension, "wb") as f:
            f.write(file.file.read())
    
    #Raise 204 if error occurs
    except Exception as e:
        response.status_code = status.HTTP_204_NO_CONTENT
        return {"message": str(e)}

    return {"message": "File uploaded successfully"}