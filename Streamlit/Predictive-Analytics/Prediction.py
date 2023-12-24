import streamlit as st
import requests
import pandas as pd

# Set the background colors
st.markdown(
    """
    <style>
    body {
        background-color: #f0f0f0; /* Light gray background */
        margin: 0; /* Remove default margin for body */
        padding: 0; /* Remove default padding for body */
    }
    .st-bw {
        background-color: #eeeeee; /* White background for widgets */
    }
    .st-cq {
        background-color: #cccccc; /* Gray background for chat input */
        border-radius: 10px; /* Add rounded corners */
        padding: 8px 12px; /* Add padding for input text */
        color: black; /* Set text color */
    }

    .st-cx {
        background-color: white; /* White background for chat messages */
    }
    .sidebar .block-container {
        background-color: #f0f0f0; /* Light gray background for sidebar */
        border-radius: 10px; /* Add rounded corners */
        padding: 10px; /* Add some padding for spacing */
    }
    .top-right-image-container {
        position: fixed;
        top: 30px;
        right: 0;
        padding: 20px;
        background-color: white; /* White background for image container */
        border-radius: 0 0 0 10px; /* Add rounded corners to bottom left */
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown("""
    <div style='display: flex; align-items: center; gap: 15px;'>
        <img src='https://cdn-icons-png.flaticon.com/512/3815/3815321.png' width='50'>
        <h1 style='margin: 0;'>Aplikasi Predictive Analytics</h1>
    </div>
""", unsafe_allow_html=True)


# Create functions to open each social media app
def open_app(app_name):
    st.experimental_set_query_params(page=app_name)

##################################################################################################
# Fungsi untuk melakukan POST request ke endpoint
def run_prediction(customer_id):
    url = 'https://asia-southeast2-trial-genai.cloudfunctions.net/predictive-analytics'
    payload = {"customer": customer_id}
    headers = {'Content-Type': 'application/json'}

    try:
        response = requests.post(url, json=payload, headers=headers)
        if response.status_code == 200:
            return response.json()
        else:
            return {"error": f"Request failed with status code {response.status_code}"}
    except requests.RequestException as e:
        return {"error": f"Request error: {str(e)}"}

# Tampilan Streamlit
st.title("Product Prediction from Customer")

# Kolom input teks untuk customer
customer_id = st.text_input("Masukkan ID Customer:", "")

# Tombol untuk menjalankan proses
if st.button("Prediksi"):
    if customer_id:
        # Menjalankan prediksi jika ID customer diisi
        st.info("Sedang melakukan prediksi...")
        result = run_prediction(int(customer_id))
        
        # Menampilkan hasil prediksi
        st.success("Prediksi selesai!")
        # Mengonversi JSON ke DataFrame Pandas
        if result != {}:
            df = pd.read_json(result)
            st.write(df)
        else:
            st.write("Customer sudah melihat semua produk, silahkan cari Customer lain.")
    else:
        st.warning("Mohon isi ID Customer terlebih dahulu.")