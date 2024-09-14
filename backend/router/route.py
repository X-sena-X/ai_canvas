from fastapi import APIRouter
import base64
from PIL import Image
from io import BytesIO
from router.utils import analyze_img
from schema import ImageData

router = APIRouter()


@router.post("")
async def run(data: ImageData):
    image_data = base64.b64decode(data.image.split(",")[1])
    image_bytes = BytesIO(image_data)
    image = Image.open(image_bytes)
    print("Inside router")
    responses = analyze_img(image, data.dict_of_vars)
    data = []
    for response in responses:
        data.append(response)
    print("response in route: ", response)
    return {"message": "Image processed", "data": data, "status": "success"}
