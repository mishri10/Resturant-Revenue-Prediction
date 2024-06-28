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
location = st.sidebar.selectbox('Select Location', list(location_encoding.keys()))
cuisine = st.sidebar.selectbox('Select Cuisine', list(cuisine_encoding.keys()))
parking = st.sidebar.selectbox('Parking Availability', list(parking_encoding.keys()))

rating = st.sidebar.slider('Rating', 0, 5, 1)
seating_capacity = st.sidebar.slider('Seating Capacity', 40, 100, 1)
average_meal_price = st.sidebar.slider('Average Meal Price', 200, 2000, 1)
social_media_followers = st.sidebar.slider('Social Media Followers', 0, 100000, 1)
chef_experience_years = st.sidebar.slider('Chef Experience Years', 0, 20, 1)
number_of_reviews = st.sidebar.slider('Number of Reviews', 0, 2000, 1)
weekend_reservations = st.sidebar.slider('Weekend Reservations', 0, 100, 1)
weekday_reservations = st.sidebar.slider('Weekday Reservations', 0, 100, 1)

# Prepare input data
input_data = pd.DataFrame({
    'Location': [location_encoding.get(location, 0)],
    'Cuisine': [cuisine_encoding.get(cuisine, 0)],
    'Rating': [rating],
    'Seating Capacity': [seating_capacity],
    'Average Meal Price': [average_meal_price],
    'Social Media Followers': [social_media_followers],
    'Chef Experience Years': [chef_experience_years],
    'Number of Reviews': [number_of_reviews],
    'Parking Availability': [parking_encoding.get(parking, 0)],
    'Weekend Reservations': [weekend_reservations],
    'Weekday Reservations': [weekday_reservations]
})

# Display the input options and the predicted result
st.title('Restaurant Revenue Prediction')
image=Image.open('img.jpeg')
st.image(image, '')


st.write('### Options Chosen')
st.write(input_data)

# Predict and display the result
if st.sidebar.button('Predict Revenue'):
    prediction = loaded_model.predict(input_data)
    st.write(f'### Approx. Annual Revenue is: ₹{prediction[0]:,.2f}')
    
