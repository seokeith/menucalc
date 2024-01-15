import streamlit as st
import requests

def get_exchange_rate():
    api_url = "https://api.exchangerate-api.com/v4/latest/EUR"
    response = requests.get(api_url)
    if response.status_code == 200:
        data = response.json()
        return data['rates']['USD']
    else:
        st.error(f"Failed to fetch exchange rate: {response.status_code}")
        return None

def calculate_final_price(original_price, additional_fees, exchange_rate):
    tip = original_price * 0.15  # 15% tip
    final_price_eur = original_price + tip + additional_fees
    final_price_usd = final_price_eur * exchange_rate
    return final_price_usd, tip

st.title('Restaurant Menu Price Converter with Exchange Rate')

exchange_rate = get_exchange_rate()
if exchange_rate:
    st.write(f"Current Exchange Rate (EUR to USD): {exchange_rate:.2f}")

    original_price = st.number_input('Enter original price of the menu item (€)', min_value=0.0, format='%f')
    additional_fees = st.number_input('Enter any additional fees (€)', min_value=0.0, format='%f')

    if st.button('Calculate Final Price in USD'):
        final_price_usd, suggested_tip = calculate_final_price(original_price, additional_fees, exchange_rate)
        st.write(f'The final price of the menu item in USD is: ${final_price_usd:.2f}')
        st.write(f'The suggested tip is: €{suggested_tip:.2f} (15% of the meal cost)')
else:
    st.error("Unable to fetch the current exchange rate.")
