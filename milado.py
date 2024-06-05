import streamlit as st 
import google.generativeai as genai
import os
from dotenv import load_dotenv
load_dotenv()
from PIL import Image 
from secrets import *



# os.environ['GOOGLE_API_KEY']   = GOOGLE_API_KEY
genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))


def get_gemini_response(input_prompt, image):
    model = genai.GenerativeModel('gemini-pro-vision')
    response = model.generate_content([input_prompt, image[0]])
    return response.text

def input_image_setup(uploaded_file):

    if uploaded_file is not None:
        bytes_data = uploaded_file.getvalue()

        image_parts = [
            {
            "mime_type": uploaded_file.type,
            "data": bytes_data
            }
        ]

        return image_parts
    
    else:
        raise FileNotFoundError("No file uploaded")
    

#initialize the streamlit app
    
st.set_page_config(page_title="MilaDo : A String Matcher App")

st.header("MilaDo : A String Matcher App 💑")
st.markdown("Developed By : Rajat Mittal, Powered By Gemini AI")

st.write("Your personal cupid's assistant, helping you explore the delightful perks and occasional quirks of dating your crush!")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
image = ""

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", use_column_width=True)

submit = st.button("Tell me about the person")

input_prompt="""
               Give output in both English and HINDI Language. English first then HINDI.
               You are an expert in relationships and your task is to analyze the appearance of 
               individual depicted in image, identifying the what will be the Pros and Cons of 
               dating him/her based on his/her looks. Additionally, you are expected to offer 
               insights on how one should approach the individual in the image to make a favorable 
               impression. IMPORTANT NOTE: If Image does not consider human then simply say image should contain a human's photo and ask them to try again with the photo with a face.
               
               ----
               ----
             """

## If submit button is clicked


if submit:
    if not uploaded_file:
        st.subheader("Please upload your crush's beautiful photo first! 😁")
        # print("please upload image file")
    else:   
        try:
            image_data=input_image_setup(uploaded_file)
            response=get_gemini_response(input_prompt,image_data)
            # print("hi", response)

        except:
            response = "Internal Server Error"

        finally:
            st.subheader("The Response is")
            st.write(response)
            st.header("Good Luck with your search!")