import pickle
import streamlit as st

st.set_page_config(
    page_title='AUDI'
)

st.title('AUDI CAR PRICE PREDICTION')

with st.container():
    col1, col2 = st.columns(2)
    with col1:
        st.image('0_Audi-A3-Sportback.jpg')
    with col2:
        st.markdown("<h5 style='text-align: justify; color: grey '>Audi is a German luxury car manufacturer known for its elegant design, strong performance, and advanced technological innovations. Audi cars often combine luxurious interior quality with advanced features such as sophisticated infotainment systems, all-wheel drive (quattro), and efficient and powerful engines. Audi offers a wide range of car models, including sedans, SUVs, and sports cars, such as the Audi A4, Q5, and R8. Audi cars are often associated with a sense of luxury, reliability and driving comfort.</h5>",
                    unsafe_allow_html=True)

st.markdown("<h3 style='text-align: center; '>Want to get it? Predict the price of your dream car below!</h3>",
            unsafe_allow_html=True)

model = pickle.load(open('Audi.sav', 'rb'))

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
