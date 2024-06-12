import streamlit as st
import pandas as pd
# import plotly.express as px




# vendas_por_ano = dados.loc[(dados["DATA"].dt.year == 2024)]


# dados = pd.read_excel("20232024f.xlsx")
# vendas = dados.groupby(dados["DATA"].dt.year)["VLTOTAL"].sum()
# vendas2024 = dados.groupby(dados["DATA"].dt.year == '2024')["VLTOTAL"].sum()
# vendas2023 = dados.groupby(dados["DATA"].dt.year == '2023')["VLTOTAL"].sum()





# Vendas_por_mes_g = vendas_por_ano.groupby(dados["DATA"].dt.month)["VLTOTAL"].sum()
# valores = dados.head(200)
# vendas_por_mes = dados.loc[(dados["DATA"].dt.year == 2024) & (dados["DATA"].dt.month == 1)]


with st.sidebar:
    st.image("logo_almeida.png")
    st.title('Análise de Vendas')

    Filial_vendas = st.selectbox("Setor de vendas ",["Site","Força de venda 1"])

    Ano_vendas = st.selectbox("Anos ",["2023/2024","2024","2023"])



    # dados_agrupado = dados.groupby(["estado","cidade", "loja", "forma_pagamento"])["preco"].sum().to_frame()


 
          
    # st.header("My dashbord")

    # st.text('Meu texto')

    # st.caption('Balloons. Hundreds of them...')

    # st.write("# Ola", ['Caio', 'Sampaio'])
# dados.groupby("DATA")["CODUSUR"].sum()

# grafico = px.histogram(vendas_por_ano, x="DATA", 
#              y="VLTOTAL", 
#              text_auto=True,
#              title="Total por Mês",
#              color="CODUSUR")

# Vendas_por_mes_g = vendas_por_ano.groupby(dados["DATA"].dt.month)["VLTOTAL"].sum().plot.bar(x="DATA")






# grafico = px.histogram(dados, x="DATA", y="VLTOTAL")

# dados = px.data.tips()
# fig = px.ecdf(dados, x="total_bill", color="sex")
# fig.show()


# aa = px.histogram(dados, x='continent', y='lifeExp')



st.text('Power bi, Almeida - Análise de Vendas')










# if Ano_vendas == "2024":
#     # st.bar_chart(vendas2024)
# elif Ano_vendas == "2023":
#     # st.bar_chart(vendas2023)
# else:
#     # st.bar_chart(vendas)
#     # st.write(fig)



