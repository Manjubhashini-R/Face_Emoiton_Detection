import streamlit as st
import cv2

class VideoCamera:
    def __init__(self):
        # Initialize the camera (you may need to adjust parameters here)
        self.video = cv2.VideoCapture(0)

    def __del__(self):
        # Release the camera when done
        self.video.release()

    def get_frame(self):
        # Read a frame from the camera
        success, image = self.video.read()
        if not success:
            return None
        # Convert the frame to JPEG format
        _, jpeg = cv2.imencode('.jpg', image)
        return jpeg.tobytes()

def main():
    st.title('Face Emotion Recognition')

    camera = VideoCamera()

    st.write('Camera Stream')
    # Display the camera stream
    while True:
        frame = camera.get_frame()
        if frame is not None:
            st.image(frame, channels='BGR', use_column_width=True)
        else:
            st.error('Failed to read frame from camera')

if __name__ == '__main__':
    main()
