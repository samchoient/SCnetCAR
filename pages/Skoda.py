import pickle
import streamlit as st

st.set_page_config(
    page_title='SKODA'
)

st.title('SKODA CAR PRICE PREDICTION')

with st.container():
    col1, col2 = st.columns(2)
    with col1:
        st.write("Skoda is a car manufacturer from the Czech Republic that has gained global recognition. The brand is known for its practical, functional, and affordable cars. Skoda offers a range of models, from hatchbacks, sedans, station wagons, to SUVs. Skoda cars often have an elegant design with smooth lines and balanced proportions. The brand is known for its spacious cabin space, use of quality materials, and good finishing. Skoda also")
    with col2:
        st.image('20190529111435_2020-Skoda-Superb-front.webp')
with st.container():
    col1, col2 = st.columns(2)
    with col1:
        st.image('06_24.webp')
    with col2:
        st.write('emphasizes comfort, reliability, and fuel efficiency in each of its models. The brand often uses innovative technologies and features, such as the latest infotainment systems and comprehensive safety systems. Skoda has built a solid reputation for durability and reliable performance, at a more affordable price compared to its peers.')

st.markdown("<h3 style='text-align: center; '>Want to get it? Predict the price of your dream car below!</h3>",
            unsafe_allow_html=True)

model = pickle.load(open('Skoda.sav', 'rb'))

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
