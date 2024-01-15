import streamlit as st
import requests

# Function to get the current exchange rate from EUR to USD
def get_exchange_rate():
    api_url = "https://api.exchangerate-api.com/v4/latest/EUR"
    response = requests.get(api_url)
    data = response.json()
    return data['rates']['USD']

def calculate_final_price(original_price, service_charge, additional_fees, exchange_rate):
    total_service_charge = original_price * (service_charge / 100)
    final_price_eur = original_price + total_service_charge + additional_fees
    final_price_usd = final_price_eur * exchange_rate
    return final_price_usd

st.title('Restaurant Menu Price Converter with Exchange Rate')

exchange_rate = get_exchange_rate()
st.write(f"Current Exchange Rate (EUR to USD): {exchange_rate:.2f}")

original_price = st.number_input('Enter original price of the menu item (€)', min_value=0.0, format='%f')
service_charge = st.number_input('Enter service charge (%)', min_value=0.0, max_value=100.0, format='%f')
additional_fees = st.number_input('Enter any additional fees (€)', min_value=0.0, format='%f')

if st.button('Calculate Final Price in USD'):
    final_price_usd = calculate_final_price
