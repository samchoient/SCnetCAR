import pickle
import streamlit as st

st.set_page_config(
    page_title='VAUXHALL'
)

st.title('VAUXHALL CAR PRICE PREDICTION')

with st.container():
    col1, col2 = st.columns(2)
    with col1:
        st.write("Vauxhall is a British car manufacturer with a long history in the automotive industry. Although Vauxhall is now part of the PSA Group, the brand has its own identity in the UK car market. Vauxhall cars offer a range of models, including hatchbacks, sedans, MPVs, and SUVs. The brand is known for its stylish design, practicality, and good performance. Vauxhall cars often offer good comfort and modern")
    with col2:
        st.image('Vauxhall_Astra_registered_July_2016_999cc.jpg')
with st.container():
    col1, col2 = st.columns(2)
    with col1:
        st.image('1 Vauxhall Astra.jpeg')
    with col2:
        st.write('features expected in the segments they target. The brand also boasts good fuel efficiency with economical and eco-friendly engines. Vauxhall has a strong history in racing and has won numerous championships. In addition, the brand also focuses on safety by providing comprehensive safety features in most of its models.')

st.markdown("<h3 style='text-align: center; '>Want to get it? Predict the price of your dream car below!</h3>",
            unsafe_allow_html=True)

model = pickle.load(open('vauxhall.sav', 'rb'))

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
