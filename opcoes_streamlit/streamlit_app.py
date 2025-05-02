# streamlit_app.py

import streamlit as st
from main_controller import MainController
class StreamlitView:
    def __init__(self, controller: MainController):
        self.controller = controller

    def display(self):
        st.title("Web Scraper com Streamlit")

        url = st.text_input("Digite a URL do site:")
        scr_type = st.radio("Tipo scrape", ["bs4", "json"])
        if scr_type == "bs4":
            tag = st.text_input("Digite a tag HTML para extrair (ex: 'h1', 'p', 'div'):")
            class_name = st.text_input("Digite o nome da classe (opcional):")
        
        if st.button("Extrair Dados"):
            if (scr_type == "bs4") and url and tag:
                data = self.controller.scrape_and_display(url, tag, class_name)
                if isinstance(data, list):
                    st.subheader("Dados Extraídos:")
                    for item in data:
                        st.write(item)
                else:
                    st.error(data)

            elif (scr_type == "json") and url:
                data = self.controller.scrape_json(url)
                st.subheader("Dados Extraídos:")
                st.write(data)          
            else:
                #st.warning("Por favor, preencha a URL e a tag.")
                st.warning("Por favor, preencha os dados obrigatórios")

if __name__ == "__main__":
    controller = MainController()
    view = StreamlitView(controller)
    view.display()