import pickle
import streamlit as st

st.set_page_config(
    page_title='BMW'
)

st.title('BMW CAR PRICE PREDICTION')

with st.container():
    col1, col2 = st.columns(2)
    with col1:
        st.write("BMW is a German luxury car manufacturer known for its combination of elegant design, powerful performance and advanced technology. BMW cars have a solid reputation for superior handling and driving dynamics. They offer a wide range of models, from sedans, coupes, SUVs, to sports cars. BMW is also known for their innovations in the use of lightweight materials and efficient engines, such as TwinPower Turbo technology. BMW's exterior design often incorporates bold lines with a distinctive front grille that gives the brand a strong identity. Inside, BMW cars offer luxurious interiors with a blend of modern design and cutting-edge features such as the latest infotainment systems and optimal comfort. With a rich heritage and dedication to performance, BMW has gained global recognition as one of the world's top luxury car brands.")
    with col2:
        st.image('photo-1580273916550-e323be2ae537.png')

st.markdown("<h3 style='text-align: center; '>Want to get it? Predict the price of your dream car below!</h3>",
            unsafe_allow_html=True)

model = pickle.load(open('BMW.sav', 'rb'))

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
