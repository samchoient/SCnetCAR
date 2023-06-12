import pickle
import streamlit as st

st.set_page_config(
    page_title='HYUNDAI'
)

st.title('HYUNDAI CAR PRICE PREDICTION')

with st.container():
    col1, col2 = st.columns(2)
    with col1:
        st.write("Hyundai is a South Korean automaker that has become one of the leading automotive brands in the world. The brand is known for its high-quality cars, attractive designs, and advanced features. Hyundai offers a wide range of vehicles, from sedans, hatchbacks, SUVs, to electric cars. Hyundai cars often have a modern and dynamic design, with sharp lines and elegant details. They also feature quality in terms of comfort, safety, and the latest technology. Hyundai has a good reputation for")
    with col2:
        st.image('img_001.webp')
with st.container():
    col1, col2 = st.columns(2)
    with col1:
        st.image('2020-hyundai-elantra-2-1617982857.jpg')
    with col2:
        st.write('fuel efficiency and environmental friendliness with models like the Hyundai Ioniq Electric. In addition, Hyundai is also known for its extensive warranty coverage, giving consumers confidence. With a combination of innovation, quality, and competitive pricing, Hyundai continues to be a popular choice in the global automobile market.')

st.markdown("<h3 style='text-align: center; '>Want to get it? Predict the price of your dream car below!</h3>",
            unsafe_allow_html=True)

model = pickle.load(open('Hyundai.sav', 'rb'))

year = st.number_input('Input Tahun Mobil')
mileage = st.number_input('Input KM Mobil')
tax = st.number_input('Input Pajak Mobil')
mpg = st.number_input('Input Konsumsi BBM')
engineSize = st.number_input('Input Engine Size')

predict = ''

if st.button('Estimasi Harga'):
    predict = model.predict([[year, mileage, tax, mpg, engineSize]])
    st.write('Estimasi Harga Mobil Bekas dalam Pounds: ', predict)
    st.write('Estimasi Harga Mobil Bekas dalam Rupiah: ', predict*18642.79)
