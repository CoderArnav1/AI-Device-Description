import logging
from fastapi import APIRouter, HTTPException
from models.device_model import DeviceSpecs
from services.ai_service import generate_device_description

logger=logging.getLogger(__name__)
handler=logging.FileHandler('logs/api.log')
formatter=logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
router = APIRouter()


@router.post("/generate")  
def generate_description(device: DeviceSpecs):
    if not device.model_name.strip():
        logger.error("'model_name' is missing in the request!")
        raise HTTPException(status_code=500,detail="ERROR: 'model_name' is required.")
    try:
        response = generate_device_description(
            device.model_name, device.camera, device.processor, device.battery, device.display
        )
        return{"Discription:":response}
    except Exception as e:
        logger.error(f"ERROR: {str(e)} ")
        raise HTTPException(status_code=500,detail=f"Internal Server Error:{str(e)}")
    