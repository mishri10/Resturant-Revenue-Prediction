import streamlit as st
import pandas as pd
import pickle
import PIL
from PIL import Image

# Load the saved model
with open('random_forest_model.pkl', 'rb') as f:
    loaded_model = pickle.load(f)

# Encoding dictionaries
cuisine_encoding = {'Italian': 0.5, 'American': 0.4, 'Indian': 0.6, 'Mexican': 0.2, 'French': 0.3, 'Japanese': 0.1}
location_encoding = {'Rural': 0, 'Urban': 2, 'SemiUrban': 1}
parking_encoding = {'Yes': 1, 'No': 0}




# Sidebar for input
st.sidebar.title('Input Options')

cuisine = st.sidebar.selectbox('Select Cuisine', list(cuisine_encoding.keys()))


rating = st.sidebar.slider('Rating', 0, 5, 4)
seating_capacity = st.sidebar.slider('Seating Capacity', 30, 200, 100)
average_meal_price = st.sidebar.slider('Average Meal Price', 200, 2000, 200)
social_media_followers = st.sidebar.slider('Social Media Followers', 1000, 100000, 1000)
chef_experience_years = st.sidebar.slider('Chef Experience Years', 0, 20, 2)

weekend_reservations = st.sidebar.slider('Weekend Reservations', 0, 100, 1)
weekday_reservations = st.sidebar.slider('Weekday Reservations', 0, 100, 1)

# Prepare input data
input_data = pd.DataFrame({
    'Location': [0],
    'Cuisine': [cuisine_encoding.get(cuisine, 4)],
    'Rating': [rating],
    'Seating Capacity': [seating_capacity],
    'Average Meal Price': [average_meal_price],
    'Social Media Followers': [social_media_followers],
    'Chef Experience Years': [chef_experience_years],
    'Number of Reviews': [1000],
    'Parking Availability': [0],
    'Weekend Reservations': [weekend_reservations],
    'Weekday Reservations': [weekday_reservations]
})

# Display the input options and the predicted result
st.title('Restaurant Revenue Prediction')
image=Image.open('img.jpeg')
st.image(image, '')


st.write('### Options Chosen')
st.write(input_data.drop(columns=['Location', 'Number of Reviews', 'Parking Availability']))

# Predict and display the result
if st.sidebar.button('Predict Revenue'):
    prediction = loaded_model.predict(input_data)
    st.write(f'### Approx. Annual Revenue is: ₹{prediction[0]:,.2f}')
    
