import pickle
import streamlit as st

st.set_page_config(
    page_title='VOLKSWAGEN'
)

st.title('VOLKSWAGEN CAR PRICE PREDICTION')

with st.container():
    col1, col2 = st.columns(2)
    with col1:
        st.image('DB2023AU00551_web_1600.jpg')
    with col2:
        st.write("Volkswagen is a German automaker that has become one of the world's leading automotive brands. The brand is known for its high-quality, innovative, and iconic cars. Volkswagen offers a variety of car models, ranging from hatchbacks, sedans, SUVs, to electric cars. Volkswagen cars often have an elegant and timeless design, with attention to detail and an attractive appearance. The brand is known for its solid construction quality")
with st.container():
    col1, col2 = st.columns(2)
    with col1:
        st.write("and use of quality materials. Volkswagen also features reliable performance and comfortable driving, with a pleasant and responsive driving experience. The brand also emphasizes the latest innovations and technologies, including advanced safety features and cutting-edge infotainment systems. With its combination of elegant design, good quality and reliable performance, Volkswagen continues to be one of the most popular and recognized car brands worldwide.")
    with col2:
        st.image('22VWArtRliDSG5drGryFL_800.jpg')

st.markdown("<h3 style='text-align: center; '>Want to get it? Predict the price of your dream car below!</h3>",
            unsafe_allow_html=True)

model = pickle.load(open('volkswagen.sav', 'rb'))

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
