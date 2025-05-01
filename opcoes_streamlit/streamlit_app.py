# streamlit_app.py

import streamlit as st
from main_controller import MainController
print(__name__)
class StreamlitView:
    def __init__(self, controller: MainController):
        self.controller = controller

    def display(self):
        st.title("Web Scraper com Streamlit")

        url = st.text_input("Digite a URL do site:")
        tag = st.text_input("Digite a tag HTML para extrair (ex: 'h1', 'p', 'div'):")
        class_name = st.text_input("Digite o nome da classe (opcional):")

        if st.button("Extrair Dados"):
            if url and tag:
                data = self.controller.scrape_and_display(url, tag, class_name)
                if isinstance(data, list):
                    st.subheader("Dados Extraídos:")
                    for item in data:
                        st.write(item)
                else:
                    st.error(data)
            else:
                st.warning("Por favor, preencha a URL e a tag.")

if __name__ == "__main__":
    controller = MainController()
    view = StreamlitView(controller)
    view.display()