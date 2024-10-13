# Phishing Email Detection
from os import read
import streamlit as st

# A comparison on Random Forest vs Supor Vector
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.pipeline import Pipeline
from sklearn import metrics


@st.cache_data
def modelar(uploaded_file):
    data = pd.read_csv(uploaded_file)

    data.isna().sum()  # List empty variables
    df = data.dropna()

    base_lines = df["Email Type"].value_counts().to_frame()  # Sample is IMBALANCED

    base_lines["weights"] = base_lines["count"] / base_lines["count"].max()
    undersample_obs = base_lines["count"].min()
    oversampled = df[df["Email Type"] == "Safe Email"].sample(undersample_obs)
    dfx = pd.concat(
        [oversampled, df[df["Email Type"] == "Phishing Email"]], ignore_index=True
    )

    X = dfx["Email Text"]  # Features
    y = dfx["Email Type"]
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=0
    )
    return X_train, X_test, y_train, y_test


@st.cache_resource
def train(X_train, X_test, y_train, y_test):
    classifier = Pipeline(
        [
            ("vectorizer", TfidfVectorizer()),
            ("classifier", RandomForestClassifier(n_estimators=10)),
        ]
    )
    classifier.fit(X_train, y_train)
    return classifier


st.title("Prueba de concepto")
st.header("Input para entrenar modelo")
uploaded_file = st.file_uploader("Escoja el csv", type="csv")


if uploaded_file is not None:
    # Title of the app

    X_train, X_test, y_train, y_test = modelar(uploaded_file)
    if X_train is not None and y_train is not None:
        classifier = train(X_train, X_test, y_train, y_test)
        y_hat = classifier.predict(X_test)
        st.write("Model:", "Accuracy:", metrics.accuracy_score(y_test, y_hat))

    if "model_cached" not in st.session_state:
        st.session_state.model_cached = True
        st.write("Modelo en cache.")
    else:
        st.write("Modelo en cache y cargado.")

    # List to store text inputs
    if "text_list" not in st.session_state:
        st.session_state.text_list = []

    st.header("API input para consumir modelo")
    if st.session_state.model_cached:
        with st.form(key="my_form"):
            text_input = st.text_input(
                "Ingrese el texto del correo (o presione 'Done' para terminar):"
            )
            submit_button = st.form_submit_button(label="Submit")

        if submit_button:
            st.write("\nResultados:")
            st.write(classifier.predict([text_input]))
