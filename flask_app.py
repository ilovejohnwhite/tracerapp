from flask_socketio import emit
from trigger_workflow import get_images  # Importing your workflow triggering function
import base64
import websocket

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('image-upload')
def handle_image_upload(data):
    cluster_option = data['clusterOption']
    image_data = data['image']  # Assuming this is base64 encoded
    
    # Decode the image from base64
    decoded_image_data = base64.b64decode(image_data.split(',')[1])
    
    # Here you need to save the decoded image temporarily or pass it directly if your workflow supports that
    temp_image_path = 'path/to/save/temp_image.jpg'
    with open(temp_image_path, 'wb') as image_file:
        image_file.write(decoded_image_data)
    
    # Connect to ComfyUI WebSocket
    ws = websocket.WebSocket()
    ws.connect(f"ws://{server_address}/ws?clientId={client_id}")
    
    # Assuming your workflow can be triggered with the image path or requires modification to do so
    # This part might need adjustment based on how you integrate the image with your workflow
    images = get_images(ws, your_workflow_modified_to_include_image)
    
    # Process the images returned by the workflow
    # You need to adjust this part to handle the response from your workflow
    # For example, you might emit URLs to the processed images to the client
    emit('image-processed', {'images': images})
