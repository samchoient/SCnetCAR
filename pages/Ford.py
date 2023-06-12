import pickle
import streamlit as st

st.set_page_config(
    page_title='FORD'
)

st.title('FORD CAR PRICE PREDICTION')

with st.container():
    col1, col2 = st.columns(2)
    with col1:
        st.image('202209131227-main.cropped_1663048959.jpg')
    with col2:
        st.write("Ford is an American car manufacturer that has been operating in the automotive industry for a long time. The brand is known for its range of reliable, functional and affordable car models. Ford offers a wide range of vehicles, from passenger cars such as sedans, hatchbacks, and SUVs, to trucks and sports cars. Ford cars often have a strong and masculine")
with st.container():
    col1, col2 = st.columns(2)
    with col1:
        st.write("design, with an emphasis on durability and performance. The brand is also known for their innovative technologies, such as the Ford synchronization system that integrates mobile devices with vehicles. Ford has also been a pioneer in the development of electric cars with models like the Mustang Mach-E. With a long history and dedication to quality, Ford continues to be one of the most popular and trusted car brands in the global market.")
    with col2:
        st.image('20210112011132_Ford_EcoSport_Storm_1.jpg')

st.markdown("<h3 style='text-align: center; '>Want to get it? Predict the price of your dream car below!</h3>",
            unsafe_allow_html=True)

model = pickle.load(open('Ford.sav', 'rb'))

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
