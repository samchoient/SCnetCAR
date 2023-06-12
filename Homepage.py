import streamlit as st
from streamlit_option_menu import option_menu

st.set_page_config(
    page_title='Car Price Prediction'
)

st.title('SCNetCAR')

with st.container():
    col1, col2 = st.columns(2)
    with col1:
        st.image('0124_042656_fa8e_inilah.com_.jpg')
        st.markdown("<h5 style='text-align: justify; '>Introducing SCNetCAR, a revolutionary website that specializes in predicting car prices with unparalleled accuracy. Whether you're a car enthusiast, a buyer looking for the best deals, or a seller looking to maximize profits, SCNetCAR is the right resource for you.:</h5>",
                    unsafe_allow_html=True)
    with col2:
        st.write("Are you tired of the uncertainty and confusion when it comes to buying or selling a car? Do you wish there was a way to accurately predict future car prices in the market? Look no further, because we have the solution for you!")
        st.image('261cbb_7d006a45987c485986b62df660063b87~mv2.webp')

st.markdown("<h3 style='text-align: center; '>Here are the reasons why you should choose SCNetCAR:</h3>",
            unsafe_allow_html=True)

with st.container():
    col1, col2 = st.columns(2)
    with col1:
        st.image('202302241341-main.cropped_1677220870.jpg')
        st.write("2. Easy-to-Use Interface")
        st.write("SCNetCAR's user-friendly website makes it easy for you to navigate our vast database of car models, years, and trims. Simply enter the necessary details, and within seconds, you will receive a comprehensive prediction of the car's future value.")
    with col2:
        st.write("1. Precise predictions")
        st.write("Our advanced algorithms analyze extensive historical data, market trends, and various influential factors to provide accurate car price predictions. Say goodbye to guesswork and make the right decision with confidence.")
        st.write("3. Comprehensive Data Analysis")
        st.write("We leave no stone unturned in predicting car prices. SCNetCAR considers factors such as mileage, condition, geographic location, model popularity, and even economic indicators to ensure the most reliable predictions.")

with st.container():
    col1, col2 = st.columns(2)
    with col1:
        st.write("4. Personalized recommendations")
        st.write("Whether you're buying or selling a car, SCNetCAR offers personalized recommendations based on your unique needs. Our intelligent system considers your preferences, budget, and market trends to guide you towards the most suitable option.")
    with col2:
        st.write("5. Save Time and Money")
        st.write("By using SCNetCAR's predictions, you can save hours of time searching for the right car or trying to determine its value. Our streamlined platform simplifies the process, so you can make the right decision quickly and confidently.")

st.markdown("<h3 style='text-align: center;'>CLICK YOUR DREAM CAR BRAND ON THE SIDEBAR</h3>",
            unsafe_allow_html=True)
st.image('Honda-Brio-sidoarjo-a.jpg')
st.markdown("<h5 style='text-align: center; color: grey;'>Don't let uncertainty hold you back. Gain insights, make smarter decisions, and unlock the potential of the car market like never before. Visit our website now and take the guesswork out of buying and selling cars. Trust the experts; trust SCNetCAR!</h5>", unsafe_allow_html=True)
