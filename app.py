import streamlit as st
import plotly.express as px
import pandas as pd

st.set_page_config(layout="wide")

hide_st_style = """
            <style>
            ##MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
"""
st.markdown(hide_st_style, unsafe_allow_html=True)

col1, col2 = st.columns(2)
(col3,) = st.columns(1)

# data = pd.read_csv(r"", sep=";")
# data_ano = data.groupby("ano_acidente")
# data_tipo = data.groupby("tp_acidente")

# df_ano = []
# df_tipo = []
# for ano, d in data_ano:
#     df_ano.append({"ano": ano, "total": d["ano_acidente"].count()})


# for tipo, t in data_tipo:
#     df_tipo.append({"tipo": tipo, "total": t["tp_acidente"].count()})
@st.cache_data
def load_ano():
    data = pd.read_json("./ano.json")
    return data


@st.cache_data
def load_tipo():
    data = pd.read_json("./tipo.json")
    return data


data_ano = pd.read_json("./ano.json")
data_tipo = pd.read_json("./tipo.json")

fig_ano = px.line(data_ano, x="ano", y="total", title="Teste")
fig_tipo = px.pie(data_tipo, values="total", names="tipo", title="Teste pie")
fig_ano_bar = px.bar(data_ano, x="ano", y="total")

col1.plotly_chart(fig_ano)
col2.plotly_chart(fig_tipo)
col3.plotly_chart(fig_ano_bar)
