import pickle
import streamlit as st

st.set_page_config(
    page_title='MERCEDES BENZ'
)

st.title('MERCEDES BENZ CAR PRICE PREDICTION')

with st.container():
    col1, col2 = st.columns(2)
    with col1:
        st.image(
            'photo-1595925889916-2a1d773a0613.jpeg')
    with col2:
        st.write("Mercedes-Benz is a luxury car brand that originated in Germany and has become one of the symbols of prestige and luxury in the automotive industry. Mercedes-Benz cars are known for their elegant design, high quality, and outstanding performance. The brand offers a wide range of models, from sedans, coupes, SUVs, to sports cars, all of which are designed with attention to detail and refinement. Mercedes-Benz is known for innovation and advanced technology, such as the 4MATIC drive system, powerful turbocharged engines, and cutting-edge safety features. Mercedes-Benz cars also offer great comfort and luxury inside the cabin, with high-quality materials and furniture. In addition, Mercedes-Benz has a long history in the automotive world and has won many championships in racing. With its combination of luxury, performance and prestige, Mercedes-Benz continues to be one of the most desired luxury car brands in the world.")

st.markdown("<h3 style='text-align: center; '>Want to get it? Predict the price of your dream car below!</h3>",
            unsafe_allow_html=True)

model = pickle.load(open('Mercedes Benz.sav', 'rb'))

year = st.number_input('Input Tahun Mobil')
mileage = st.number_input('Input KM Mobil')
engineSize = st.number_input('Input Engine Size')

predict = ''

if st.button('Estimasi Harga'):
    predict = model.predict([[year, mileage, engineSize]])
    st.write('Estimasi Harga Mobil Bekas dalam Pounds: ', predict)
    st.write('Estimasi Harga Mobil Bekas dalam Rupiah: ', predict*18642.79)
