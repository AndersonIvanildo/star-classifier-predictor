import streamlit as st

def main():
    """
    This project is the main file when the streamlit will run
    """
    # Configuração da página
    st.set_page_config(page_title="Texto em Tempo Real", layout="wide")
    st.title("Conversor de Texto em Tempo Real 🚀")

    # Criar colunas
    col1, col2 = st.columns(2)

    # Coluna de entrada
    with col1:
        st.header("Entrada")
        input_text = st.text_area(
            "Digite seu texto aqui:",
            height=300,
            placeholder="Comece a digitar...",
            key="input"
        )

    # Coluna de saída
    with col2:
        st.header("Saída em Tempo Real")
        if input_text:
            st.markdown(f"**Texto digitado:**\n\n{input_text}")
        else:
            st.info("Seu texto aparecerá aqui automaticamente enquanto você digita...")

    # Estilo adicional
    st.markdown("""
    <style>
        [data-testid=stVerticalBlock] {
            gap: 0.5rem;
        }
        textarea {
            font-size: 18px !important;
        }
    </style>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()