import pickle
import streamlit as st

st.set_page_config(
    page_title='TOYOTA'
)

st.title('TOYOTA CAR PRICE PREDICTION')

with st.container():
    col1, col2 = st.columns(2)
    with col1:
        st.image('005_133_1578467218424_000.webp')
        st.image('005_134_1578467278807_000.jpg')
    with col2:
        st.write("Toyota is one of the world's largest car manufacturers from Japan. The brand is famous for its reliable, efficient, and high-quality cars. Toyota offers a variety of car models, ranging from sedans, hatchbacks, SUVs, to trucks. Toyota cars are often known for their practical, functional, and durable designs. The brand is known for its solid reputation for reliability and durability, with many models renowned for their durability and ability to cover long distances. Toyota also features advanced technologies, such as the hybrid system in the famous Prius model, which combines good performance with high fuel efficiency. The brand also pays attention to comfort, safety, and cutting-edge features, such as the latest infotainment systems and complete safety packages. Toyota has a good reputation for after-sales service and parts availability. With its combination of reliability, efficiency and quality, Toyota continues to be a popular and globally recognized car brand.")

st.markdown("<h3 style='text-align: center; '>Want to get it? Predict the price of your dream car below!</h3>",
            unsafe_allow_html=True)

model = pickle.load(open('Toyota.sav', 'rb'))

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
