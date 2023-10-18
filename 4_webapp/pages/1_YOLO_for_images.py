import streamlit as st
from yolo_predictions import YOLO_Pred
from PIL import Image
import numpy as np

st.set_page_config(page_title="YOLO Object Detection",
                   layout='wide',
                   page_icon='./images/object.png')

st.title('Welcome to YOLO for Image')
st.write('Please Upload Image to get detections')

with st.spinner('Please wait while your model is loading'):
    yolo = YOLO_Pred(onnx_model='4_webapp/best.onnx',
                    data_yaml='4_webapp/data.yaml')

def upload_image():
    image_file = st.file_uploader(label='Upload Image')
    if image_file is not None:
        size_mb = image_file.size/(1024**2)
        details = {'filename': image_file.name,
                'filetype': image_file.type,
                'filesize ': "{:,.2f} MB".format(size_mb)}
        #st.json(details)

        if details['filetype'] in ('image/png', 'image/jpeg'):
            st.success('VALID IMAGE file type (png or jpg)')
            return {"file": image_file, "details": details}

        else:
            st.error('INVALID Image file type')
            st.error('Upload only png, jpg, jpeg')
            return None
        
def main():
    object = upload_image()

    if object:
        prediction = False
        image_obj = Image.open(object['file'])

        col1, col2 = st.columns(2)

        with col1:
            st.info('Preview of image')
            st.image(image_obj)
        
        with col2:
            st.subheader('Check below for file details')
            st.json(object['details'])

            button = st.button('Get detections from YOLO')
            if button:
                with st.spinner("""
                                Detecting Objects from image, please wait.
                                """):
                    image_array = np.array(image_obj)
                    pred_img = yolo.predictions(image_array)
                    pred_img_obj = Image.fromarray(pred_img)
                    prediction = True

        if prediction:
            st.subheader("Predicted Image")
            st.caption("Object detection from YOLO v5 model")
            st.image(pred_img_obj)

if __name__ == '__main__':
    main()
