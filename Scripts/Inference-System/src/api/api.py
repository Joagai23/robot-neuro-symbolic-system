from flask import Blueprint, request, jsonify
from ..affordance_inference.affordance_inference import AffordanceInference

api_bp = Blueprint('api_bp', __name__)

# Start Inference System
affordance_system = AffordanceInference()

@api_bp.post('/capture_perception')
def capture_perception():
    try:
        # Read request body
        body = request.get_json()
        image_bytes = body['image']
        camera, jar = body['camera'], body['jar']
        caption, affordances = affordance_system.evaluate_image(image_bytes, camera, jar)
        response = {}
        response['caption'] = caption
        response['affordances'] = affordances
        return jsonify(response)
    except Exception as error:
        print(error)
        return 'POST /capture_perception error in server', 500