import streamlit as st
import plotly.express as px
import pandas as pd

st.set_page_config(layout="wide")

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

data_ano = pd.read_json("./ano.json")
data_tipo = pd.read_json("./tipo.json")

fig_ano = px.line(data_ano, x="ano", y="total", title="Teste")
fig_tipo = px.pie(data_tipo, values="total", names="tipo", title="Teste pie")
fig_ano_bar = px.bar(data_ano, x="ano", y="total")

col1.plotly_chart(fig_ano)
col2.plotly_chart(fig_tipo)
col3.plotly_chart(fig_ano_bar)
