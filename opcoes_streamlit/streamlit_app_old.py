# streamlit_app.py

import streamlit as st
from main_controller import MainController
class StreamlitView:
    def __init__(self, controller: MainController):
        self.controller = controller

    def display(self):
        st.title("Web Scraper com Streamlit")

      
        scr_type = st.radio("Tipo scrape", ["bs4", "json"])
        if scr_type == "bs4":
            url = st.text_input("Digite a URL do site:")
            tag = st.text_input("Digite a tag HTML para extrair (ex: 'h1', 'p', 'div'):")
            class_name = st.text_input("Digite o nome da classe (opcional):")
        if scr_type == "json":
            api=st.selectbox("API:",["Genérica","ADVFN"])
            if api == "Genérica":
                url = st.text_input("Digite a URL do site:")
            if api == "ADVFN":
                symbol = st.text_input("Código da Ação/Opção:")

        if st.button("Extrair Dados"):
            if (scr_type == "bs4") and url and tag:
                data = self.controller.scrape_and_display(url, tag, class_name)
                if isinstance(data, list):
                    st.subheader("Dados Extraídos:")
                    for item in data:
                        st.write(item)
                else:
                    st.error(data)

            elif (scr_type == "json") and (api == "Genérica") and url:
                data = self.controller.scrape_json(url)
                st.subheader("Dados Extraídos:")
                st.write(data)

            elif (scr_type == "json") and (api == "ADVFN") and symbol:
                data = self.controller.scrape_advfn_hist(symbol)
                st.subheader("Dados Extraídos:")
                st.write(data)

            else:
                #st.warning("Por favor, preencha a URL e a tag.")
                st.warning("Por favor, preencha os dados obrigatórios")

if __name__ == "__main__":
    controller = MainController()
    view = StreamlitView(controller)
    view.display()