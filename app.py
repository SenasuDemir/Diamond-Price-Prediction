from sklearn.pipeline import Pipeline 
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
import streamlit as st
import pandas as pd
import joblib
import sklearn
print(sklearn.__version__)
# Load the data
df = pd.read_csv("diamonds.csv")
df["size"] = df["x"] * df["y"] * df["z"]

# Load the trained model
model = joblib.load('best_model.pkl')

# Define the preprocessor and pipeline
preprocessor = ColumnTransformer(
    transformers=[
        ("num", StandardScaler(), ["size", "carat"]),
        ("cat", OneHotEncoder(), ["color", "clarity", "cut"])
    ]
)
pipeline = Pipeline(steps=[("preprocessor", preprocessor), ("regressor", model)])

# Fit the pipeline on the data (optional, if you want to refit with the data)
pipeline.fit(df[["size", "carat", "cut", "color", "clarity"]], df["price"])

def price_prediction(size, carat, cut, color, clarity):
    input_data = pd.DataFrame({
        "size": [size],
        "carat": [carat],
        "cut": [cut],
        "color": [color],
        "clarity": [clarity]
    })
    prediction = pipeline.predict(input_data)[0]
    return prediction

# Main function to render the Streamlit app
def main():
    st.set_page_config(page_title="Diamond Price Prediction", layout="centered")
    
    # App title and description
    st.title("💎 Diamond Price Prediction 💎")
    st.write("""
    Enter the diamond features to predict its price. 
    Adjust the inputs to see how different characteristics affect the price.
    """)

    # Layout with columns for better organization
    col1, col2 = st.columns([1, 1])
    
    with col1:
        size = st.number_input("Size (volume in mm³)", int(df["size"].min()), int(df["size"].max()))
        carat = st.number_input("Carat Weight", float(df["carat"].min()), float(df["carat"].max()), step=0.01)
    
    with col2:
        cut = st.selectbox("Cut", df["cut"].unique())
        color = st.selectbox("Color", df["color"].unique())
    
    clarity = st.selectbox("Clarity", df["clarity"].unique(), key="clarity", index=0)
    
    # Prediction button
    if st.button("Predict Price"):
        price = price_prediction(size, carat, cut, color, clarity)
        price = float(price)
        
        # Display the result with enhanced visualization
        st.markdown(f"### Predicted Price: 💲 **${price:,.2f}**")
        st.write("""
        This is the estimated price based on the characteristics you provided. 
        Please note that the actual market price may vary.
        """)

if __name__ == "__main__":
    main()
