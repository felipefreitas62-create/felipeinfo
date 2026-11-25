
import streamlit as st

# Configuração da página
st.set_page_config(
    page_title="Calculadora de Média",
    page_icon="📚",
    layout="centered"
)

# Título
st.title("📚 Calculadora de Média")
st.write("Digite suas notas para calcular sua média escolar.")

st.divider()

# Entrada das notas
st.subheader("📝 Insira suas notas")

nota1 = st.number_input(
    "Primeira nota",
    min_value=0.0,
    max_value=10.0,
    value=0.0,
    step=0.5
)

nota2 = st.number_input(
    "Segunda nota",
    min_value=0.0,
    max_value=10.0,
    value=0.0,
    step=0.5
)

nota3 = st.number_input(
    "Terceira nota",
    min_value=0.0,
    max_value=10.0,
    value=0.0,
    step=0.5
)

nota4 = st.number_input(
    "Quarta nota",
    min_value=0.0,
    max_value=10.0,
    value=0.0,
    step=0.5
)

st.divider()

# Botão de calcular
if st.button("Calcular média", use_container_width=True):

    media = (nota1 + nota2 + nota3 + nota4) / 4

    st.subheader("📊 Resultado")

    st.metric("Sua média", f"{media:.2f}")

    if media >= 7:
        st.success("🎉 Parabéns! Você foi aprovado!")
    elif media >= 5:
        st.warning("⚠️ Você está de recuperação!")
    else:
        st.error("❌ Você foi reprovado!")

st.caption("Calculadora de Média Escolar | Desenvolvido em Python")
