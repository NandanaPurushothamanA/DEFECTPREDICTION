import streamlit as st
import pandas as pd


df = pd.read_csv("module_data.csv")

# Features
features = ['module_complexity', 'code_churn', 'past_bugs', 'test_failures']

st.title("🔍 Software Defect Risk Predictor")
st.markdown("Select either a **file** or a **module** to view defect risk analysis.")

# View selector
view_option = st.radio("View by:", ["By File", "By Module"])

# View by File
if view_option == "By File":
    selected_file = st.selectbox("Choose a file:", sorted(df["file_path"].unique()))
    selected_row = df[df["file_path"] == selected_file].iloc[0]

    st.subheader("File Info")
    st.write(f"**File Path:** {selected_row['file_path']}")
    st.write(f"**Module:** {selected_row['module']}")

    # Show feature values and prediction
    st.subheader("Feature Metrics")
    st.dataframe(selected_row[features].to_frame(name="Value"))

    st.subheader(" Prediction")
    label = " Low Risk" if selected_row["predicted_risk"] == 0 else " High Risk"
    st.markdown(f"**Defect Risk:** {label}")

# View by Module
elif view_option == "By Module":
    selected_module = st.selectbox("Choose a module:", sorted(df["module"].unique()))

    module_df = df[df["module"] == selected_module]

    avg_metrics = module_df[features].mean().to_frame(name="Average Value")
    risk_score = int(round(module_df["predicted_risk"].mean()))

    st.subheader(" Module Info")
    st.write(f"**Module Name:** `{selected_module}`")
    st.subheader(" Average Feature Metrics")
    st.dataframe(avg_metrics)

    st.subheader(" Prediction")
    label = " Low Risk" if risk_score == 0 else " High Risk"
    st.markdown(f"**Average Defect Risk:** {label}")

