from fastapi import APIRouter
from fastapi import FastAPI, HTTPException
from fastapi.responses import StreamingResponse
import base64
from io import BytesIO
from api.database.crud import Photo
route_photo = APIRouter()

@route_photo.get("/photo_by_id/{image_id}")
def show_photo(photo_id: int):
    try:
        photo = Photo.get_photo(photo_id)

        image_data = base64.b64decode(photo.base)

        image_io = BytesIO(image_data)

        return StreamingResponse(image_io, media_type="image/jpeg") 
    except HTTPException:
        raise HTTPException(status_code=404, detail="Image not found")
