
# import streamlit as st
# import requests
# import json
# import psycopg2
# from psycopg2.extras import execute_values
# from leonardo_api import Leonardo

# # Initialize the Leonardo API client
# leonardo = Leonardo(auth_token='6ecdfa7b-f647-4667-99c8-a85076283cb2')

# # Default values for hidden parameters
# model_id = "de7d3faf-762f-48e0-b3b7-9d0ac3a3fcf3"
# style_uuid = "111dc692-d470-4eec-b791-3475abac4c46"

# # Database connection configuration
# db_connection = {
#     "host": "34.93.64.44",
#     "port": "5432",
#     "dbname": "genai",
#     "user": "postgres",
#     "password": "postgres-genai"
# }

# # Streamlit UI
# st.title("Fashion Mood Board Generation")
# st.write("Generate a fashion mood board based on a given prompt using Leonardo API.")

# # Get user input for data parameters
# prompt = st.text_area("Prompt")
# num_images = st.text_input("Number of Images", placeholder="Enter no of images between 1 and 8")
# if num_images:
#     try:
#         num_images_value = int(num_images)
#         if num_images_value < 1 or num_images_value > 8:
#             st.warning("Please enter a value for Number of Images between 1 and 8.")
#     except ValueError:
#         st.error("Please enter a valid number for Number of Images.")

# contrast = st.text_input("Contrast", placeholder="Enter the value between 1 and 4")
# contrast_value = None
# if contrast:
#     try:
#         contrast_value = int(contrast)
#         if contrast_value < 1 or contrast_value > 4:
#             st.warning("Please enter a valid number for contrast values.")
#     except ValueError:
#         st.error("Please enter a valid number for contrast values.")
        
# width = st.text_input("Width", placeholder="Enter the value between 100px and 1024px")
# width_value= None
# if width:
#     try:
#         width_value = int(width)
#         if width_value < 100 or width_value > 1024:
#             st.warning("Please enter a valid number for width values.")
#     except ValueError:
#         st.error("Please enter a valid number for width values.")
                      
# height = st.text_input("Height", placeholder="Enter a value between 100 and 1024")
# height_value = None
# if height:
#     try:
#         height_value = int(height)
#         if height_value < 100 or height_value > 1024:
#             st.warning("Please enter a valid number for height values.")
#     except ValueError:
#         st.error("Please enter a valid number for height values.")

# # alchemy = st.checkbox("Alchemy", value=False)
# # enhance_prompt = st.checkbox("Enhance Prompt", value=True)

# # Alchemy option
# alchemy = st.radio("Alchemy", options=[True, False], index= None, help="Alchemy is used for the image quality")

# if alchemy is not None:  # This checks if the user has made a selection
#     if alchemy:
#         st.info("Image quality will be good.")
#     else:
#         st.warning("Image quality will be moderate.")
        
# # # Alchemy option
# # ultra = st.radio("Ultra", options=[True, False], index= None, help="Ultra is used for the image quality")

# # Ultra Quality Selection
# # ultra = st.radio(
# #     "Ultra Quality",
# #     options=[True, False],
# #     index= None,  # Default selection: True for better quality
# #     help="Enable Ultra mode for the highest image quality. Disable for standard quality."
# # )

# # # Display a message based on the user's selection
# # if ultra is not None:
# #     if ultra :
# #         st.info("Ultra mode enabled: The image quality will be the highest.")
# #     else:
# #         st.warning("Ultra mode disabled: The image quality will be standard.")


# # Enhance Prompt option
# enhance_prompt = st.radio("Enhance Prompt", options=[True, False], index= None, help= "Enhance Prompt is used to give the prompt details further")

# # Conditionally capture enhanced prompt
# enhanced_prompt = None
# if enhance_prompt:
#     enhanced_prompt = st.text_area("Enhanced Prompt Details", 
#                                         placeholder="Provide additional details to refine the prompt.")

# # Define the URL and headers for the initial request
# url = "https://cloud.leonardo.ai/api/rest/v1/generations"
# headers = {
#     'accept': 'application/json',
#     'authorization': 'Bearer 6ecdfa7b-f647-4667-99c8-a85076283cb2',
#     'content-type': 'application/json'
# }

# # Validate and construct the payload
# try:
#     # Convert inputs to appropriate types with proper default values
#     # contrast_value = int(contrast) if contrast else 1
#     num_images_value = int(num_images) if num_images else 1
#     width_value = int(width) if width else 1024
#     height_value = int(height) if height else 1024
    
#     # Set contrast value (changing how we handle it)
#     if contrast:
#         contrast_value = int(contrast)
#     else:
#         contrast_value = 1
   
#     # Validate all inputs are within acceptable ranges
#     if not (1 <= num_images_value <= 8):
#         st.error("Number of images must be between 1 and 8")
#         st.stop()
        
#     if not (1 <= contrast_value <= 4):
#         st.error("Contrast must be between 1 and 4")
#         st.stop()
        
#     if not (100 <= width_value <= 1024):
#         st.error("Width must be between 100 and 1024")
#         st.stop()
    
#     if not (100 <= height_value <= 1024):
#         st.error("Height must be between 100 and 1024")
#         st.stop()
    
#     # Create the payload with correct parameter names
#     data = {
#         "modelId": model_id,
#         "prompt": prompt,
#         "num_images": num_images_value,  # Changed back to num_images
#         "width": width_value,
#         "height": height_value,
#         "contrast":int(contrast_value),
#         "alchemy": alchemy if alchemy is not None else False,
#         # "ultra": ultra  if ultra  is not None else False,
#         "styleUUID": style_uuid,
#         "enhancePrompt": enhance_prompt if enhance_prompt is not None else False
#     }

# except ValueError as e:
#     st.error(f"Please ensure all numerical inputs are valid numbers: {str(e)}")
#     st.stop()

# # PostgreSQL connection function
# def store_in_database(prompt, contrast, num_images, width, height, image_path, enhanced_prompt=None):
#     try:
#         conn = psycopg2.connect(**db_connection)
#         cursor = conn.cursor()
#         query = """
#             INSERT INTO leonardo_prompts (prompts, contrast, number_of_images, width, height, image_path, enhanced_prompts)
#             VALUES (%s, %s, %s, %s, %s, %s, %s)
#         """
#         cursor.execute(query, (prompt, contrast, num_images, width, height, image_path, enhanced_prompt))
#         conn.commit()
#         cursor.close()
#         conn.close()
#         st.success("Data stored in the database successfully!")
#     except Exception as e:
#         st.error(f"Error storing data in the database: {e}")

# # Trigger image generation on button click
# if st.button('Generate Mood Board'):
#     if not prompt.strip():
#         st.error("Prompt is required.")
#     else:
#         # Send the initial POST request
#         response = requests.post(url, headers=headers, data=json.dumps(data))

#         # Check if the request was successful
#         if response.status_code == 200:
#             st.success("Request successful!")
#             response_data = response.json()

#             # Check if the response contains the necessary information
#             if 'sdGenerationJob' in response_data and 'generationId' in response_data['sdGenerationJob']:
#                 generation_id = response_data['sdGenerationJob']['generationId']

#                 # Wait for the image generation to complete and retrieve the image data
#                 imageresponse = leonardo.wait_for_image_generation(generation_id=generation_id)

#                 # Check if the 'url' key is present in the response
#                 if 'url' in imageresponse:
#                     image_url = imageresponse['url']

#                     # Display the image in Streamlit
#                     st.image(image_url, caption='Generated Fashion Mood Board', use_container_width=True)
                    
#                     # Store data in the database
#                     store_in_database(prompt, contrast_value, num_images_value, width_value, height_value, image_url, enhanced_prompt)
#                 else:
#                     st.error("Image URL not found in the response.")
#                     st.write("Response:", imageresponse)
#             else:
#                 st.error("Generation ID not found in the response.")
#                 st.write("Response:", response_data)
#         else:
#             st.error(f"Request failed with status code {response.status_code}")
#             st.write("Response:", response.text)





import streamlit as st
import requests
import json
from leonardo_api import Leonardo
import psycopg2
import os
import toml

# Load secrets from secrets.toml
try:
    secrets = toml.load(".streamlit/secrets.toml")
    api_key = secrets["general"]["LEONARDO_API_KEY"]
except FileNotFoundError:
    api_key = os.getenv("LEONARDO_API_KEY")
    if not api_key:
        st.error("API Key not found in either 'secrets.toml' or environment variables.")
        st.stop()

# Initialize Leonardo API client
leonardo = Leonardo(auth_token=api_key)

# Default values for hidden parameters
MODEL_IDS = {
    "Phoenix_1.0": "de7d3faf-762f-48e0-b3b7-9d0ac3a3fcf3",
    "Lightning_XL": "aa77f04e-3eec-4034-9c07-d0f619684628",
    "Phoenix_0.9": "6b645e3a-d64f-4341-a6d8-7a3690fbf042",
    "Photoreal": "b24e16ff-06e3-43eb-8d33-4416c2d75876"
}

STYLE_UUID = "111dc692-d470-4eec-b791-3475abac4c46"

# Database connection configuration
DB_CONFIG = {
    "host": "34.93.64.44",
    "port": "5432",
    "dbname": "genai",
    "user": "postgres",
    "password": "postgres-genai"
}

def validate_inputs(num_images, width, height):
    """Validate user inputs and return processed values."""
    errors = []
   
    try:
        num_images = int(num_images) if num_images else 1
        if not (1 <= num_images <= 8):
            errors.append("Number of images must be between 1 and 8")
    except ValueError:
        errors.append("Invalid number of images")
        num_images = None

    try:
        width = int(width) if width else 1024
        if not (100 <= width <= 1024):
            errors.append("Width must be between 100 and 1024")
    except ValueError:
        errors.append("Invalid width value")
        width = None

    try:
        height = int(height) if height else 1024
        if not (100 <= height <= 1024):
            errors.append("Invalid height value")
    except ValueError:
        errors.append("Invalid height value")
        height = None

    return num_images, width, height, errors

def store_in_database(prompt, contrast, num_images, width, height, image_url, enhanced_prompt=None):
    """Store generated mood board details in the database."""
    try:
        with psycopg2.connect(**DB_CONFIG) as conn:
            with conn.cursor() as cursor:
                query = """
                    INSERT INTO leonardo_prompts
                    (prompts, contrast, number_of_images, width, height, image_path, enhanced_prompts)
                    VALUES (%s, %s, %s, %s, %s, %s, %s)
                """
                cursor.execute(query, (prompt, contrast, num_images, width, height,
                                    image_url, enhanced_prompt))
        st.success("Data stored in the database successfully!")
    except Exception as e:
        st.error(f"Error storing data in the database: {e}")

def generate_image(model_type, data):
    """Generate image using Leonardo API."""
    try:
        response = requests.post(
            "https://cloud.leonardo.ai/api/rest/v1/generations",
            headers={
                'accept': 'application/json',
                'authorization': f'Bearer {api_key}',
                'content-type': 'application/json'
            },
            data=json.dumps(data)
        )
       
        if response.status_code != 200:
            st.error(f"Request failed with status code {response.status_code}")
            st.write("Response:", response.text)
            return None

        response_data = response.json()
        if 'sdGenerationJob' not in response_data or 'generationId' not in response_data['sdGenerationJob']:
            st.error("Generation ID not found in the response")
            return None

        generation_id = response_data['sdGenerationJob']['generationId']
        image_response = leonardo.wait_for_image_generation(generation_id=generation_id)
       
        if 'url' not in image_response:
            st.error("Image URL not found in the response")
            return None
           
        return image_response['url']
       
    except Exception as e:
        st.error(f"Error generating image: {e}")
        return None

# Streamlit UI
st.title("Fashion Mood Board Generation")
st.write("Generate a fashion mood board based on a given prompt using Leonardo API.")

# Input fields
model_type = st.radio("Select Model", options=list(MODEL_IDS.keys()), index=None)
prompt = st.text_area("Prompt", help="Enter your fashion mood board description")

# User inputs with proper validation
num_images = st.text_input("Number of Images", placeholder="Enter number of images between 1 and 8")
width = st.text_input("Width", placeholder="Enter value between 100px and 1024px")
height = st.text_input("Height", placeholder="Enter value between 100px and 1024px")

# Alchemy selection
alchemy = st.radio("Alchemy", options=[True, False], index=None,
                   help="Alchemy is used for image quality enhancement")


# Model-specific settings
model_settings = {}
if model_type in ["Phoenix_1.0", "Phoenix_0.9"]:
    enhance_prompt = st.radio("Enhance Prompt", options=[True, False], index=1)
    if enhance_prompt:
        enhanced_prompt = st.text_area("Enhanced Prompt Details")
        model_settings["enhancePrompt"] = enhance_prompt 

elif model_type in ["Lightning_XL", "Photoreal"]:
    # Use radio button instead of checkbox for enabling photo realism
    photo_realism = st.radio("Enable Photo Realism", options=["True", "False"], index=0)
    model_settings.update({
        "photoReal": photo_realism == "True",  # Convert string to boolean (True/False)
        "presetStyle": st.selectbox("Select Style", ["CINEMATIC"]),
    })
    
    # Set photoRealVersion only if photoReal is enabled
    if model_settings.get("photoReal"):
        model_settings["photoRealVersion"] = "v2"

# Generate button
if st.button('Generate Mood Board'):
    if not prompt.strip():
        st.error("Prompt is required.")
    else:
        # Validate inputs
        num_images_val, width_val, height_val, errors = validate_inputs(num_images, width, height)
       
        if errors:
            for error in errors:
                st.error(error)
        else:
            # Prepare base data
            data = {
                "modelId": MODEL_IDS[model_type],
                "prompt": prompt,
                "num_images": num_images_val,
                "width": width_val,
                "height": height_val,
                "alchemy": alchemy,
                "styleUUID": STYLE_UUID,
                **model_settings
            }
           
            # Generate image
            image_url = generate_image(model_type, data)
            if image_url:
                st.image(image_url, caption='Generated Fashion Mood Board',
                        use_container_width=True)
                store_in_database(prompt, 1, num_images_val, width_val, height_val,
                                image_url, model_settings.get("enhancePrompt"))

