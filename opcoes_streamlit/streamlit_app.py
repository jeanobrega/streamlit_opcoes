# streamlit_app.py

import streamlit as st
from main_controller import MainController
class StreamlitView:
    def __init__(self, controller: MainController):
        self.controller = controller

    def display(self):
        st.title("Opções Streamlit")

      
        symbol = st.text_input("Código da Ação/Opção:")

        if st.button("Extrair Dados"):
            
            if  symbol:
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