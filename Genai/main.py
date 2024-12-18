# # from leonardo_api import Leonardo

# # leonardo = Leonardo(auth_token='6ecdfa7b-f647-4667-99c8-a85076283cb2')

# # response = leonardo.get_user_info()  # get your user info
# # print(response)


# # response = leonardo.post_generations(prompt="""You are an experienced fashion designer specializing in digital mood boards, with expertise in curating compelling visual concepts for collections. Your mood boards should consist of a curated collage of imagery, representing a cohesive fashion theme, paired with a corresponding color palette displayed at the bottom for easy reference. Each mood board must feature at least one model on the runway showcasing the collection’s key pieces.

# # Design Brief:
# # Create a mood board for a Spring/Summer collection aimed at girls aged 10-12 years. Use a warm color palette of glowing orange and rust, complemented by sand and khaki neutrals. Silhouettes should be rounded and minimalistic, paired with crinkled textures to add interest. Wooden bead accessories will provide an artisanal, craft-inspired touch to the designs.

# # Key considerations:

# # Maintain clean, youthful silhouettes appropriate for young girls.
# # Highlight crinkled fabric textures for added visual appeal.
# # Incorporate wooden beads as an accent to emphasize craftsmanship.
# # Use a warm, natural color palette that balances earthy tones with vibrant orange.
# # Include a model on the runway wearing the collection to complete the visual narrative.""", num_images=1,
# #                                            negative_prompt='Unstructured or messy collage layout, inconsistent spacing between images, individual photos not arranged in a grid or clean visual order, images without a color palette at the bottom, missing cohesive theme, overly busy or cluttered design, sharp shadows, mismatched lighting, irrelevant fashion styles or accessories, overly complex or abstract patterns, lack of crinkled fabric textures, unrelated or low-quality runway images,missing artisanal wooden bead details, washed-out colors, overly bright tones, absence of minimalistic and rounded silhouettes, blurry or pixelated images, chaotic backgrounds, inconsistent alignment, unrelated accessories, lack of visual balance.',
# #                                            model_id='e316348f-7773-490e-adcd-46757c738eb7', width=1024, height=768,
# #                                            guidance_scale=2)

# #         #e316348f-7773-490e-adcd-46757c738eb7
# # print(response)
# # response = leonardo.wait_for_image_generation(generation_id=response['sdGenerationJob']['generationId'])

# # print(response)



# import streamlit as st
# from leonardo_api import Leonardo

# # Initialize Leonardo API
# leonardo = Leonardo(auth_token='6ecdfa7b-f647-4667-99c8-a85076283cb2')

# # Streamlit UI
# st.set_page_config(page_title="AI Image Generator", layout="wide")
# st.title("AI Image Generator")
# st.write("Generate images based on your positive and negative text prompts using Leonardo AI!")

# # Input: Positive Prompt
# positive_prompt = st.text_area("Enter Positive Prompt:", height=150)

# # Input: Negative Prompt
# negative_prompt = st.text_area("Enter Negative Prompt:", height=150)

# # Input: Number of Images
# num_images = st.number_input("Number of Images to Generate", min_value=1, max_value=100, value=1, step=1)

# # Input: Aspect Ratio
# aspect_ratios = {
#     "2:3": (1024, 1536),  # 2:3 aspect ratio
#     "1:1": (1024, 1024),  # 1:1 aspect ratio
#     "16:9": (1920, 1080),  # 16:9 aspect ratio
# }

# st.write("Select an aspect ratio for the generated image:")
# aspect_ratio_choice = st.radio("Aspect Ratio:", ["2:3", "1:1", "16:9"])

# # Map user input to dimensions
# width, height = aspect_ratios[aspect_ratio_choice]

# # Select Generation Mode (Fast, Quality, Ultra)
# generation_mode = st.selectbox("Select Generation Mode:", ["Fast", "Quality", "Ultra"])

# # Button to trigger image generation
# if st.button("Generate Image"):

#     if positive_prompt:  # Check if the positive prompt is provided
#         try:
#             # API Request Payload
#             payload = {
#                 "prompt": positive_prompt,
#                 "negative_prompt": negative_prompt,
#                 "num_images": num_images,
#                 "width": width,
#                 "height": height,
#                 "alchemy": True,
#                 "styleUUID": "111dc692-d470-4eec-b791-3475abac4c46",  # Example style UUID
#                 "generation_mode": generation_mode,  # Include the generation mode in the request
#             }

#             # Headers
#             headers = {
#                 "Authorization": f"Bearer {leonardo.auth_token}",
#                 "Content-Type": "application/json"
#             }

#             # Make the API call
#             response = leonardo.post_generations(payload=payload, headers=headers)

#             # Wait for image generation to complete
#             generation_id = response['sdGenerationJob']['generationId']
#             st.write("Image Generation in Progress...")

#             # Wait for completion (you may want to add a check for the generation status here)
#             image_response = leonardo.wait_for_image_generation(generation_id=generation_id)

#             # Display the generated images
#             generated_images = image_response.get("generations", [])
#             if generated_images:
#                 for img in generated_images:
#                     st.image(img["url"], caption="Generated Image", use_column_width=True)
#             else:
#                 st.error("No images were generated. Please try again.")
        
#         except Exception as e:
#             st.error(f"Error generating images: {e}")

#     else:
#         st.warning("Please enter a positive prompt to generate images.")



# # import streamlit as st
# # from leonardo_api import Leonardo

# # # Initialize Leonardo API
# # leonardo = Leonardo(auth_token='6ecdfa7b-f647-4667-99c8-a85076283cb2')

# # # Streamlit UI
# # st.set_page_config(page_title="AI Image Generator", layout="wide")
# # st.title("AI Image Generator")
# # st.write("Generate images based on your text prompts using Leonardo AI!")

# # # Prompt Input
# # prompt = st.text_area("Enter your prompt:", height=150)

# # # Aspect Ratio Selection
# # st.write("### Select an aspect ratio for the generated image:")
# # aspect_ratio = st.radio(
# #     label="Aspect Ratio",
# #     options=["2:3", "1:1", "16:9"],
# #     index=1  # Default to 1:1
# # )

# # # Map aspect ratios to dimensions
# # aspect_ratios = {
# #     "2:3": (1024, 1536),
# #     "1:1": (1024, 1024),
# #     "16:9": (1920, 1080),
# # }
# # width, height = aspect_ratios[aspect_ratio]

# # # Number of Images
# # num_images = st.slider("Number of Images to Generate", min_value=1, max_value=4, value=1)

# # # Guidance Scale
# # guidance_scale = st.slider("Guidance Scale", min_value=1, max_value=20, value=7)

# # # Button to Generate Images
# # if st.button("Generate Images"):
# #     if prompt:
# #         try:
# #             # Call the Leonardo API
# #             with st.spinner("Generating images..."):
# #                 response = leonardo.post_generations(
# #                     prompt=prompt,
# #                     num_images=num_images,
# #                     negative_prompt="""Unstructured or messy collage layout, inconsistent spacing between images, 
# #                     individual photos not arranged in a grid or clean visual order, images without a color palette at the bottom, 
# #                     missing cohesive theme, overly busy or cluttered design, sharp shadows, mismatched lighting, irrelevant fashion 
# #                     styles or accessories, overly complex or abstract patterns, lack of crinkled fabric textures, unrelated or 
# #                     low-quality runway images, missing artisanal wooden bead details, washed-out colors, overly bright tones, 
# #                     absence of minimalistic and rounded silhouettes, blurry or pixelated images, chaotic backgrounds, inconsistent 
# #                     alignment, unrelated accessories, lack of visual balance.""",
# #                     model_id='e316348f-7773-490e-adcd-46757c738eb7',
# #                     width=width,
# #                     height=height,
# #                     guidance_scale=guidance_scale,
# #                 )
# #                 generation_id = response['sdGenerationJob']['generationId']
# #                 response = leonardo.wait_for_image_generation(generation_id=generation_id)

# #             # Display the Generated Images
# #             if response.get("generations"):
# #                 st.success("Image Generation Complete!")
# #                 for image in response["generations"]:
# #                     st.image(image["url"], width=300)
# #             else:
# #                 st.error("No images were generated. Please try again.")

# #         except Exception as e:
# #             st.error(f"Error generating images: {e}")
# #     else:
# #         st.warning("Please enter a prompt to generate images.")



# # from leonardo_api import Leonardo

# # # Initialize Leonardo API
# # leonardo = Leonardo(auth_token='6ecdfa7b-f647-4667-99c8-a85076283cb2')

# # # Define image dimensions for different aspect ratios
# # aspect_ratios = {
# #     "2:3": (1024, 1536),  # 2:3 aspect ratio
# #     "1:1": (1024, 1024),  # 1:1 aspect ratio
# #     "16:9": (1920, 1080), # 16:9 aspect ratio
# # }

# # # User selection for aspect ratio
# # print("Select an aspect ratio for the generated image:")
# # print("1. 2:3\n2. 1:1\n3. 16:9")
# # choice = input("Enter the number corresponding to your choice: ")

# # # Map user input to dimensions
# # if choice == "1":
# #     width, height = aspect_ratios["2:3"]
# # elif choice == "2":
# #     width, height = aspect_ratios["1:1"]
# # elif choice == "3":
# #     width, height = aspect_ratios["16:9"]
# # else:
# #     print("Invalid choice. Defaulting to 1:1.")
# #     width, height = aspect_ratios["1:1"]

# # # Get User Info
# # response = leonardo.get_user_info()
# # print("User Info:", response)

# # # Call the API for image generation
# # response = leonardo.post_generations(
# #     prompt="""You are an experienced fashion designer specializing in digital mood boards, with expertise in curating compelling visual concepts for collections. Your mood boards should consist of a curated collage of imagery, representing a cohesive fashion theme, paired with a corresponding color palette displayed at the bottom for easy reference. Each mood board must feature at least one model on the runway showcasing the collection’s key pieces.

# #     Design Brief:
# #     Create a mood board for a Spring/Summer collection aimed at girls aged 10-12 years. Use a warm color palette of glowing orange and rust, complemented by sand and khaki neutrals. Silhouettes should be rounded and minimalistic, paired with crinkled textures to add interest. Wooden bead accessories will provide an artisanal, craft-inspired touch to the designs.

# #     Key considerations:

# #     Maintain clean, youthful silhouettes appropriate for young girls.
# #     Highlight crinkled fabric textures for added visual appeal.
# #     Incorporate wooden beads as an accent to emphasize craftsmanship.
# #     Use a warm, natural color palette that balances earthy tones with vibrant orange.
# #     Include a model on the runway wearing the collection to complete the visual narrative.""",
# #     num_images=1,
# #     negative_prompt="""Unstructured or messy collage layout, inconsistent spacing between images, 
# #     individual photos not arranged in a grid or clean visual order, images without a color palette at the bottom, 
# #     missing cohesive theme, overly busy or cluttered design, sharp shadows, mismatched lighting, irrelevant fashion 
# #     styles or accessories, overly complex or abstract patterns, lack of crinkled fabric textures, unrelated or 
# #     low-quality runway images, missing artisanal wooden bead details, washed-out colors, overly bright tones, 
# #     absence of minimalistic and rounded silhouettes, blurry or pixelated images, chaotic backgrounds, inconsistent 
# #     alignment, unrelated accessories, lack of visual balance.""",
# #     model_id='e316348f-7773-490e-adcd-46757c738eb7',
# #     width=width,   # Dynamic width based on aspect ratio
# #     height=height, # Dynamic height based on aspect ratio
# #     guidance_scale=2
# # )

# # # Wait for Image Generation to Complete
# # generation_id = response['sdGenerationJob']['generationId']
# # print("Image Generation in Progress...")

# # response = leonardo.wait_for_image_generation(generation_id=generation_id)

# # # Display Response
# # print("Image Generation Complete!")
# # print("Generated Images:", response)



# import requests
# import json
# from leonardo_api import Leonardo


# leonardo = Leonardo(auth_token='6ecdfa7b-f647-4667-99c8-a85076283cb2')
# # Define the URL and headers
# url = "https://cloud.leonardo.ai/api/rest/v1/generations"
# headers = {
#     'accept': 'application/json',
#     'authorization': 'Bearer 6ecdfa7b-f647-4667-99c8-a85076283cb2',
#     'content-type': 'application/json'
# }

# # Define the payload (data)
# data = {
#     "modelId": "de7d3faf-762f-48e0-b3b7-9d0ac3a3fcf3",
#     "contrast": 4.0,
#     "prompt": "You are an experienced fashion designer specializing in digital mood boards, with expertise in curating compelling visual concepts for collections. Your mood boards should consist of a curated collage of imagery, representing a cohesive fashion theme, paired with a corresponding color palette displayed at the bottom for easy reference. Each mood board must feature at least one model on the runway showcasing the collection’s key pieces. Design Brief: Create a mood board for a Spring/Summer collection aimed at girls aged 10-12 years. Use a warm color palette of glowing orange and rust, complemented by sand and khaki neutrals. Silhouettes should be rounded and minimalistic, paired with crinkled textures to add interest. Wooden bead accessories will provide an artisanal, craft-inspired touch to the designs. Key considerations: Maintain clean, youthful silhouettes appropriate for young girls. Highlight crinkled fabric textures for added visual appeal. Incorporate wooden beads as an accent to emphasize craftsmanship. Use a warm, natural color palette that balances earthy tones with vibrant orange. Include a model on the runway wearing the collection to complete the visual narrative.",
#     "num_images": 1,
#     "width": 1472,
#     "height": 832,
#     # "alchemy": False,
#     "ultra": True,
#     "styleUUID": "111dc692-d470-4eec-b791-3475abac4c46",
#     "enhancePrompt": True
# }

# # Send the POST request
# response = requests.post(url, headers=headers, data=json.dumps(data))


# # Check the response
# if response.status_code == 200:
#     print("Request successful!")
#     print("Response:", response.json())  # Assuming the API returns JSON data
#     response_data=response.json()
#     imageresponse = leonardo.wait_for_image_generation(generation_id=response_data['sdGenerationJob']['generationId'])
#     print(imageresponse)
# else:
#     print(f"Request failed with status code {response.status_code}")
#     print("Response:", response.text)


# import requests
# import json
# from leonardo_api import Leonardo

# # Initialize the Leonardo API client
# leonardo = Leonardo(auth_token='6ecdfa7b-f647-4667-99c8-a85076283cb2')

# # Define the URL and headers for the initial request
# url = "https://cloud.leonardo.ai/api/rest/v1/generations"
# headers = {
#     'accept': 'application/json',
#     'authorization': 'Bearer 6ecdfa7b-f647-4667-99c8-a85076283cb2',
#     'content-type': 'application/json'
# }

# # Define the payload (data) for the initial request
# data = {
#     "modelId": "de7d3faf-762f-48e0-b3b7-9d0ac3a3fcf3",
#     "contrast": 4.0,
#     "prompt": "You are an experienced fashion designer specializing in digital mood boards, with expertise in curating compelling visual concepts for collections. Your mood boards should consist of a curated collage of imagery, representing a cohesive fashion theme, paired with a corresponding color palette displayed at the bottom for easy reference. Each mood board must feature at least one model on the runway showcasing the collection’s key pieces. Design Brief: Create a mood board for a Spring/Summer collection aimed at girls aged 10-12 years. Use a warm color palette of glowing orange and rust, complemented by sand and khaki neutrals. Silhouettes should be rounded and minimalistic, paired with crinkled textures to add interest. Wooden bead accessories will provide an artisanal, craft-inspired touch to the designs. Key considerations: Maintain clean, youthful silhouettes appropriate for young girls. Highlight crinkled fabric textures for added visual appeal. Incorporate wooden beads as an accent to emphasize craftsmanship. Use a warm, natural color palette that balances earthy tones with vibrant orange. Include a model on the runway wearing the collection to complete the visual narrative.",
#     "num_images": 1,
#     "width": 1472,
#     "height": 832,
#     "ultra": True,
#     "styleUUID": "111dc692-d470-4eec-b791-3475abac4c46",
#     "enhancePrompt": True
# }

# # Send the initial POST request
# response = requests.post(url, headers=headers, data=json.dumps(data))

# # Check if the request was successful
# if response.status_code == 200:
#     print("Request successful!")
#     response_data = response.json()
#     generation_id = response_data['sdGenerationJob']['generationId']
#     print("Generation ID:", generation_id)

#     # Wait for the image generation to complete and retrieve the image data
#     imageresponse = leonardo.wait_for_image_generation(generation_id=generation_id)
#     print("Image Generation Response:", imageresponse)

#     # Get the single generation details using the obtained generation_id
#     generation_details = leonardo.get_single_generation(generation_id=generation_id)
#     print("Single Generation Response:", generation_details)
# else:
#     print(f"Request failed with status code {response.status_code}")
#     print("Response:", response.text)


# import streamlit as st
# import requests
# import json
# from leonardo_api import Leonardo

# # Initialize the Leonardo API client
# leonardo = Leonardo(auth_token='6ecdfa7b-f647-4667-99c8-a85076283cb2')

# # Define the URL and headers for the initial request
# url = "https://cloud.leonardo.ai/api/rest/v1/generations"
# headers = {
#     'accept': 'application/json',
#     'authorization': 'Bearer 6ecdfa7b-f647-4667-99c8-a85076283cb2',
#     'content-type': 'application/json'
# }

# # Define the payload (data) for the initial request
# data = {
#     "modelId": "de7d3faf-762f-48e0-b3b7-9d0ac3a3fcf3",
#     "contrast": 4.0,
#     "prompt": "You are an experienced fashion designer specializing in digital mood boards, with expertise in curating compelling visual concepts for collections. Your mood boards should consist of a curated collage of imagery, representing a cohesive fashion theme, paired with a corresponding color palette displayed at the bottom for easy reference. Each mood board must feature at least one model on the runway showcasing the collection’s key pieces. Design Brief: Create a mood board for a Spring/Summer collection aimed at girls aged 10-12 years. Use a warm color palette of glowing orange and rust, complemented by sand and khaki neutrals. Silhouettes should be rounded and minimalistic, paired with crinkled textures to add interest. Wooden bead accessories will provide an artisanal, craft-inspired touch to the designs. Key considerations: Maintain clean, youthful silhouettes appropriate for young girls. Highlight crinkled fabric textures for added visual appeal. Incorporate wooden beads as an accent to emphasize craftsmanship. Use a warm, natural color palette that balances earthy tones with vibrant orange. Include a model on the runway wearing the collection to complete the visual narrative.",
#     "num_images": 1,
#     "width": 1472,
#     "height": 832,
#     "ultra": True,
#     "styleUUID": "111dc692-d470-4eec-b791-3475abac4c46",
#     "enhancePrompt": True
# }

# # Streamlit UI
# st.title("Fashion Mood Board Generation")
# st.write("Generate a fashion mood board based on a given prompt using Leonardo API.")

# # Trigger image generation on button click
# if st.button('Generate Mood Board'):
#     # Send the initial POST request
#     response = requests.post(url, headers=headers, data=json.dumps(data))

#     # Check if the request was successful
#     if response.status_code == 200:
#         st.success("Request successful!")
#         response_data = response.json()
#         generation_id = response_data['sdGenerationJob']['generationId']
#         st.write("Generation ID:", generation_id)

#         # Wait for the image generation to complete and retrieve the image data
#         imageresponse = leonardo.wait_for_image_generation(generation_id=generation_id)
#         st.write("Image Generation Response:", imageresponse)

#         # Get the image URL from the response
#         image_url = imageresponse['sdGenerationJob']['imageUrl']
#         st.write("Image URL:", image_url)

#         # Display the image in Streamlit
#         st.image(image_url, caption='Generated Fashion Mood Board', use_column_width=True)
#     else:
#         st.error(f"Request failed with status code {response.status_code}")
#         st.write("Response:", response.text)


# import streamlit as st
# import requests
# import json
# from leonardo_api import Leonardo

# # Initialize the Leonardo API client
# leonardo = Leonardo(auth_token='6ecdfa7b-f647-4667-99c8-a85076283cb2')

# # Define the URL and headers for the initial request
# url = "https://cloud.leonardo.ai/api/rest/v1/generations"
# headers = {
#     'accept': 'application/json',
#     'authorization': 'Bearer 6ecdfa7b-f647-4667-99c8-a85076283cb2',
#     'content-type': 'application/json'
# }

# # Define the payload (data) for the initial request
# data = {
#     "modelId": "de7d3faf-762f-48e0-b3b7-9d0ac3a3fcf3",
#     "contrast": 4.0,
#     "prompt": "You are an experienced fashion designer specializing in digital mood boards, with expertise in curating compelling visual concepts for collections. Your mood boards should consist of a curated collage of imagery, representing a cohesive fashion theme, paired with a corresponding color palette displayed at the bottom for easy reference. Each mood board must feature at least one model on the runway showcasing the collection's key pieces. Design Brief: Create a mood board for a Spring/Summer collection aimed at girls aged 10-12 years. Use a warm color palette of glowing orange and rust, complemented by sand and khaki neutrals. Silhouettes should be rounded and minimalistic, paired with crinkled textures to add interest. Wooden bead accessories will provide an artisanal, craft-inspired touch to the designs. Key considerations: Maintain clean, youthful silhouettes appropriate for young girls. Highlight crinkled fabric textures for added visual appeal. Incorporate wooden beads as an accent to emphasize craftsmanship. Use a warm, natural color palette that balances earthy tones with vibrant orange. Include a model on the runway wearing the collection to complete the visual narrative.",
#     "num_images": 1,
#     "width": 1472,
#     "height": 832,
#     "ultra": True,
#     "styleUUID": "111dc692-d470-4eec-b791-3475abac4c46",
#     "enhancePrompt": True
# }

# # Streamlit UI
# st.title("Fashion Mood Board Generation")
# st.write("Generate a fashion mood board based on a given prompt using Leonardo API.")

# # Trigger image generation on button click
# if st.button('Generate Mood Board'):
#     # Send the initial POST request
#     response = requests.post(url, headers=headers, data=json.dumps(data))

#     # Check if the request was successful
#     if response.status_code == 200:
#         st.success("Request successful!")
#         response_data = response.json()
#         generation_id = response_data['generationId']
#         st.write("Generation ID:", generation_id)

#         # Wait for the image generation to complete and retrieve the image data
#         imageresponse = leonardo.wait_for_image_generation(generation_id=generation_id)
#         st.write("Image Generation Response:", imageresponse)

#         # Check if the image URL is present in the response
#         if 'imageUrl' in imageresponse:
#             image_url = imageresponse['imageUrl']
#             st.write("Image URL:", image_url)

#             # Display the image in Streamlit
#             st.image(image_url, caption='Generated Fashion Mood Board', use_column_width=True)
#         else:
#             st.error("Image URL not found in the response.")
#             st.write("Response:", imageresponse)
#     else:
#         st.error(f"Request failed with status code {response.status_code}")
#         st.write("Response:", response.text)


# import streamlit as st
# import requests
# import json
# from leonardo_api import Leonardo

# # Initialize the Leonardo API client
# leonardo = Leonardo(auth_token='6ecdfa7b-f647-4667-99c8-a85076283cb2')

# # Define the URL and headers for the initial request
# url = "https://cloud.leonardo.ai/api/rest/v1/generations"
# headers = {
#     'accept': 'application/json',
#     'authorization': 'Bearer 6ecdfa7b-f647-4667-99c8-a85076283cb2',
#     'content-type': 'application/json'
# }

# # Define the payload (data) for the initial request
# data = {
#     "modelId": "de7d3faf-762f-48e0-b3b7-9d0ac3a3fcf3",
#     "contrast": 4.0,
#     "prompt": "You are an experienced fashion designer specializing in digital mood boards, with expertise in curating compelling visual concepts for collections. Your mood boards should consist of a curated collage of imagery, representing a cohesive fashion theme, paired with a corresponding color palette displayed at the bottom for easy reference. Each mood board must feature at least one model on the runway showcasing the collection's key pieces. Design Brief: Create a mood board for a Spring/Summer collection aimed at girls aged 10-12 years. Use a warm color palette of glowing orange and rust, complemented by sand and khaki neutrals. Silhouettes should be rounded and minimalistic, paired with crinkled textures to add interest. Wooden bead accessories will provide an artisanal, craft-inspired touch to the designs. Key considerations: Maintain clean, youthful silhouettes appropriate for young girls. Highlight crinkled fabric textures for added visual appeal. Incorporate wooden beads as an accent to emphasize craftsmanship. Use a warm, natural color palette that balances earthy tones with vibrant orange. Include a model on the runway wearing the collection to complete the visual narrative.",
#     "num_images": 1,
#     "width": 1472,
#     "height": 832,
#     "alchemy":False,
#     # "ultra": True,
#     "styleUUID": "111dc692-d470-4eec-b791-3475abac4c46",
#     "enhancePrompt": True
# }

# # Streamlit UI
# st.title("Fashion Mood Board Generation")
# st.write("Generate a fashion mood board based on a given prompt using Leonardo API.")

# # Trigger image generation on button click
# if st.button('Generate Mood Board'):
#     # Send the initial POST request
#     response = requests.post(url, headers=headers, data=json.dumps(data))

#     # Check if the request was successful
#     if response.status_code == 200:
#         st.success("Request successful!")
#         response_data = response.json()

#         # Check if the response contains the necessary information
#         if 'generationId' in response_data:
#             generation_id = response_data['generationId']
#             st.write("Generation ID:", generation_id)

#             # Wait for the image generation to complete and retrieve the image data
#             imageresponse = leonardo.wait_for_image_generation(generation_id=generation_id)
#             st.write("Image Generation Response:", imageresponse)

#             # Check if the image URL is present in the response
#             if 'imageUrl' in imageresponse:
#                 image_url = imageresponse['imageUrl']
#                 st.write("Image URL:", image_url)

#                 # Display the image in Streamlit
#                 st.image(image_url, caption='Generated Fashion Mood Board', use_column_width=True)
#             else:
#                 st.error("Image URL not found in the response.")
#                 st.write("Response:", imageresponse)
#         else:
#             st.error("Generation ID not found in the response.")
#             st.write("Response:", response_data)
#     else:
#         st.error(f"Request failed with status code {response.status_code}")
#         st.write("Response:", response.text)



# import streamlit as st
# import requests
# import json
# from leonardo_api import Leonardo

# # Initialize the Leonardo API client
# leonardo = Leonardo(auth_token='6ecdfa7b-f647-4667-99c8-a85076283cb2')

# # Define the URL and headers for the initial request
# url = "https://cloud.leonardo.ai/api/rest/v1/generations"
# headers = {
#     'accept': 'application/json',
#     'authorization': 'Bearer 6ecdfa7b-f647-4667-99c8-a85076283cb2',
#     'content-type': 'application/json'
# }

# # Define the payload (data) for the initial request
# data = {
#     "modelId": "de7d3faf-762f-48e0-b3b7-9d0ac3a3fcf3",
#     "contrast": 4.0,
#     "prompt": "You are an experienced fashion designer specializing in digital mood boards, with expertise in curating compelling visual concepts for collections. Your mood boards should consist of a curated collage of imagery, representing a cohesive fashion theme, paired with a corresponding color palette displayed at the bottom for easy reference. Each mood board must feature at least one model on the runway showcasing the collection's key pieces. Design Brief: Create a mood board for a Spring/Summer collection aimed at girls aged 10-12 years. Use a warm color palette of glowing orange and rust, complemented by sand and khaki neutrals. Silhouettes should be rounded and minimalistic, paired with crinkled textures to add interest. Wooden bead accessories will provide an artisanal, craft-inspired touch to the designs. Key considerations: Maintain clean, youthful silhouettes appropriate for young girls. Highlight crinkled fabric textures for added visual appeal. Incorporate wooden beads as an accent to emphasize craftsmanship. Use a warm, natural color palette that balances earthy tones with vibrant orange. Include a model on the runway wearing the collection to complete the visual narrative.",
#     "num_images": 1,
#     "width": 1472,
#     "height": 832,
#     "alchemy": False,
#     "styleUUID": "111dc692-d470-4eec-b791-3475abac4c46",
#     "enhancePrompt": True
# }

# # Streamlit UI
# st.title("Fashion Mood Board Generation")
# st.write("Generate a fashion mood board based on a given prompt using Leonardo API.")

# # Trigger image generation on button click
# if st.button('Generate Mood Board'):
#     # Send the initial POST request
#     response = requests.post(url, headers=headers, data=json.dumps(data))

#     # Check if the request was successful
#     if response.status_code == 200:
#         st.success("Request successful!")
#         response_data = response.json()

#         # Check if the response contains the necessary information
#         if 'sdGenerationJob' in response_data and 'generationId' in response_data['sdGenerationJob']:
#             generation_id = response_data['sdGenerationJob']['generationId']
#             st.write("Generation ID:", generation_id)

#             # Wait for the image generation to complete and retrieve the image data
#             imageresponse = leonardo.wait_for_image_generation(generation_id=generation_id)
#             st.write("Image Generation Response:", imageresponse)

#             # Check if the image URL is present in the response
#             if 'imageUrl' in imageresponse:
#                 image_url = imageresponse['imageUrl']
#                 st.write("Image URL:", image_url)

#                 # Display the image in Streamlit
#                 st.image(image_url, caption='Generated Fashion Mood Board', use_column_width=True)
#             else:
#                 st.error("Image URL not found in the response.")
#                 st.write("Response:", imageresponse)
#         else:
#             st.error("Generation ID not found in the response.")
#             st.write("Response:", response_data)
#     else:
#         st.error(f"Request failed with status code {response.status_code}")
#         st.write("Response:", response.text)


# import streamlit as st
# import requests
# import json
# from leonardo_api import Leonardo

# # Initialize the Leonardo API client
# leonardo = Leonardo(auth_token='6ecdfa7b-f647-4667-99c8-a85076283cb2')

# # Define the URL and headers for the initial request
# url = "https://cloud.leonardo.ai/api/rest/v1/generations"
# headers = {
#     'accept': 'application/json',
#     'authorization': 'Bearer 6ecdfa7b-f647-4667-99c8-a85076283cb2',
#     'content-type': 'application/json'
# }

# # Define the payload (data) for the initial request
# data = {
#     "modelId": "de7d3faf-762f-48e0-b3b7-9d0ac3a3fcf3",
#     "contrast": 4.0,
#     "prompt": "You are an experienced fashion designer specializing in digital mood boards, with expertise in curating compelling visual concepts for collections. Your mood boards should consist of a curated collage of imagery, representing a cohesive fashion theme, paired with a corresponding color palette displayed at the bottom for easy reference. Each mood board must feature at least one model on the runway showcasing the collection's key pieces. Design Brief: Create a mood board for a Spring/Summer collection aimed at girls aged 10-12 years. Use a warm color palette of glowing orange and rust, complemented by sand and khaki neutrals. Silhouettes should be rounded and minimalistic, paired with crinkled textures to add interest. Wooden bead accessories will provide an artisanal, craft-inspired touch to the designs. Key considerations: Maintain clean, youthful silhouettes appropriate for young girls. Highlight crinkled fabric textures for added visual appeal. Incorporate wooden beads as an accent to emphasize craftsmanship. Use a warm, natural color palette that balances earthy tones with vibrant orange. Include a model on the runway wearing the collection to complete the visual narrative.",
#     "num_images": 1,
#     "width": 1472,
#     "height": 832,
#     "alchemy": False,
#     "styleUUID": "111dc692-d470-4eec-b791-3475abac4c46",
#     "enhancePrompt": True
# }

# # Streamlit UI
# st.title("Fashion Mood Board Generation")
# st.write("Generate a fashion mood board based on a given prompt using Leonardo API.")

# # Trigger image generation on button click
# if st.button('Generate Mood Board'):
#     # Send the initial POST request
#     response = requests.post(url, headers=headers, data=json.dumps(data))

#     # Check if the request was successful
#     if response.status_code == 200:
#         st.success("Request successful!")
#         response_data = response.json()

#         # Check if the response contains the necessary information
#         if 'sdGenerationJob' in response_data and 'generationId' in response_data['sdGenerationJob']:
#             generation_id = response_data['sdGenerationJob']['generationId']
#             st.write("Generation ID:", generation_id)

#             # Wait for the image generation to complete and retrieve the image data
#             imageresponse = leonardo.wait_for_image_generation(generation_id=generation_id)
#             st.write("Image Generation Response:", imageresponse)

#             # Check if the 'url' key is present in the response
#             if 'url' in imageresponse:
#                 image_url = imageresponse['url']
#                 st.write("Image URL:", image_url)

#                 # Display the image in Streamlit
#                 st.image(image_url, caption='Generated Fashion Mood Board', use_column_width=True)
#             else:
#                 st.error("Image URL not found in the response.")
#                 st.write("Response:", imageresponse)
#         else:
#             st.error("Generation ID not found in the response.")
#             st.write("Response:", response_data)
#     else:
#         st.error(f"Request failed with status code {response.status_code}")
#         st.write("Response:", response.text)



# import streamlit as st
# import requests
# import json
# from leonardo_api import Leonardo

# # Initialize the Leonardo API client
# leonardo = Leonardo(auth_token='6ecdfa7b-f647-4667-99c8-a85076283cb2')

# # Streamlit UI
# st.title("Fashion Mood Board Generation")
# st.write("Generate a fashion mood board based on a given prompt using Leonardo API.")

# # Get user input for data parameters
# model_id = st.text_input("Model ID", "de7d3faf-762f-48e0-b3b7-9d0ac3a3fcf3")
# contrast = st.number_input("Contrast", min_value=0.0, max_value=10.0)
# prompt = st.text_area("Prompt")
# num_images = st.number_input("Number of Images", min_value=1, max_value=10)
# width = st.number_input("Width", min_value=100, max_value=2048)      #, value=1472
# height = st.number_input("Height", min_value=100, max_value=2048)    #, value=832
# alchemy = st.checkbox("Alchemy", value=False)
# style_uuid = st.text_input("Style UUID", "111dc692-d470-4eec-b791-3475abac4c46")
# enhance_prompt = st.checkbox("Enhance Prompt", value=True)

# # Define the URL and headers for the initial request
# url = "https://cloud.leonardo.ai/api/rest/v1/generations"
# headers = {
#     'accept': 'application/json',
#     'authorization': 'Bearer 6ecdfa7b-f647-4667-99c8-a85076283cb2',
#     'content-type': 'application/json'
# }

# # Define the payload (data) for the initial request
# data = {
#     "modelId": model_id,
#     "contrast": contrast,
#     "prompt": prompt,
#     "num_images": num_images,
#     "width": width,
#     "height": height,
#     "alchemy": alchemy,
#     "styleUUID": style_uuid,
#     "enhancePrompt": enhance_prompt
# }

# # Trigger image generation on button click
# if st.button('Generate Mood Board'):
#     # Send the initial POST request
#     response = requests.post(url, headers=headers, data=json.dumps(data))

#     # Check if the request was successful
#     if response.status_code == 200:
#         st.success("Request successful!")
#         response_data = response.json()

#         # Check if the response contains the necessary information
#         if 'sdGenerationJob' in response_data and 'generationId' in response_data['sdGenerationJob']:
#             generation_id = response_data['sdGenerationJob']['generationId']
#             # st.write("Generation ID:", generation_id)                    ###################################################################### commented 


#             # Wait for the image generation to complete and retrieve the image data
#             imageresponse = leonardo.wait_for_image_generation(generation_id=generation_id)
#             # st.write("Image Generation Response:", imageresponse)         ###################################################################### commented 


#             # Check if the 'url' key is present in the response
#             if 'url' in imageresponse:
#                 image_url = imageresponse['url']
#                 # st.write("Image URL:", image_url)        ###################################################################### commented 

#                 # Display the image in Streamlit
#                 st.image(image_url, caption='Generated Fashion Mood Board', use_column_width=True)
#             else:
#                 st.error("Image URL not found in the response.")
#                 st.write("Response:", imageresponse)
#         else:
#             st.error("Generation ID not found in the response.")
#             st.write("Response:", response_data)
#     else:
#         st.error(f"Request failed with status code {response.status_code}")
#         st.write("Response:", response.text)




import streamlit as st
import requests
import json
import psycopg2
from psycopg2.extras import execute_values
from leonardo_api import Leonardo

# Initialize the Leonardo API client
leonardo = Leonardo(auth_token='6ecdfa7b-f647-4667-99c8-a85076283cb2')

# Default values for hidden parameters
model_id = "de7d3faf-762f-48e0-b3b7-9d0ac3a3fcf3"
style_uuid = "111dc692-d470-4eec-b791-3475abac4c46"

# Database connection configuration
db_connection = {
    "host": "34.93.64.44",
    "port": "5432",
    "dbname": "genai",
    "user": "postgres",
    "password": "postgres-genai"
}

# Streamlit UI
st.title("Fashion Mood Board Generation")
st.write("Generate a fashion mood board based on a given prompt using Leonardo API.")

# Get user input for data parameters
prompt = st.text_area("Prompt")
num_images = st.text_input("Number of Images (Enter a value between 1 and 10)", "")
contrast = st.text_input("Contrast (Enter a value between 0.0 and 10.0)", "")
width = st.text_input("Width (Enter a value between 100 and 2048)", "")
height = st.text_input("Height (Enter a value between 100 and 2048)", "")
alchemy = st.checkbox("Alchemy", value=False)
enhance_prompt = st.checkbox("Enhance Prompt", value=True)

# Define the URL and headers for the initial request
url = "https://cloud.leonardo.ai/api/rest/v1/generations"
headers = {
    'accept': 'application/json',
    'authorization': 'Bearer 6ecdfa7b-f647-4667-99c8-a85076283cb2',
    'content-type': 'application/json'
}

# Validate and construct the payload
try:
    contrast_value = float(contrast) if contrast else 0.0
    num_images_value = int(num_images) if num_images else 1
    width_value = int(width) if width else 1472
    height_value = int(height) if height else 832

    data = {
        "modelId": model_id,
        "contrast": contrast_value,
        "prompt": prompt,
        "num_images": num_images_value,
        "width": width_value,
        "height": height_value,
        "alchemy": alchemy,
        "styleUUID": style_uuid,
        "enhancePrompt": enhance_prompt
    }
except ValueError:
    st.error("Please ensure all numerical inputs are valid numbers.")


# PostgreSQL connection function
def store_in_database(prompt, contrast, num_images, width, height, image_path):
    try:
        conn = psycopg2.connect(**db_connection)
        cursor = conn.cursor()
        query = """
            INSERT INTO leonardo_prompts (prompts, contrast, number_of_images, width, height, image_path)
            VALUES (%s, %s, %s, %s, %s, %s)
        """
        cursor.execute(query, (prompt, contrast, num_images, width, height, image_path))
        conn.commit()
        cursor.close()
        conn.close()
        st.success("Data stored in the database successfully!")
    except Exception as e:
        st.error(f"Error storing data in the database: {e}")

# Trigger image generation on button click
if st.button('Generate Mood Board'):
    if not prompt.strip():
        st.error("Prompt is required.")
    else:
        # Send the initial POST request
        response = requests.post(url, headers=headers, data=json.dumps(data))

        # Check if the request was successful
        if response.status_code == 200:
            st.success("Request successful!")
            response_data = response.json()

            # Check if the response contains the necessary information
            if 'sdGenerationJob' in response_data and 'generationId' in response_data['sdGenerationJob']:
                generation_id = response_data['sdGenerationJob']['generationId']

                # Wait for the image generation to complete and retrieve the image data
                imageresponse = leonardo.wait_for_image_generation(generation_id=generation_id)

                # Check if the 'url' key is present in the response
                if 'url' in imageresponse:
                    image_url = imageresponse['url']

                    # Display the image in Streamlit
                    st.image(image_url, caption='Generated Fashion Mood Board', use_column_width=True)
                    
                    # Store data in the database
                    store_in_database(prompt, contrast_value, num_images_value, width_value, height_value, image_url)
                else:
                    st.error("Image URL not found in the response.")
                    st.write("Response:", imageresponse)
            else:
                st.error("Generation ID not found in the response.")
                st.write("Response:", response_data)
        else:
            st.error(f"Request failed with status code {response.status_code}")
            st.write("Response:", response.text)
