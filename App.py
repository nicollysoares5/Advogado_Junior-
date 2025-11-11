# app.py -- IA do Advogado Júnior (protótipo)
import streamlit as st
import pandas as pd
from io import BytesIO
from docx import Document
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
import textwrap
import re

st.set_page_config("IA do Advogado Júnior", layout="wide")

# ---------- Helpers simples (substituíveis por IA real) ----------
def split_sentences(text, max_sentences=3):
    # quebra por pontos, exclui vazios
    sents = re.split(r'(?<=[.!?])\s+', text.strip())
    sents = [s.strip() for s in sents if s.strip()]
    return " ".join(sents[:max_sentences])

def summarize_text(text, n_sentences=3):
    text = text.strip()
    if not text:
        return "Nenhum texto fornecido para resumo."
    return split_sentences(text, n_sentences)

def improve_text(text):
    if not text.strip():
        return "Nenhum texto fornecido para melhoria."
    # heurística: limpar espaços, transformar em tom formal:
    t = re.sub(r'\s+', ' ', text).strip()
    # substituir informalidades comuns (exemplos)
    substitutions = {
        r"\bvc\b": "você",
        r"\bV\.c\b": "Você",
        r"\bpq\b": "porque",
        r"\bporq\b": "porque",
    }
    for pat, rep in substitutions.items():
        t = re.sub(pat, rep, t, flags=re.IGNORECASE)
    # adicionar pequenas frases formais
    if len(t.split()) < 10:
        t = "Considerando o exposto, " + t
    # melhorar pontuação simples
    t = re.sub(r'\s+,', ',', t)
    return t

def transform_to_petition_from_text(text, petitioner_name="Autor (nome)", respondent_name="Réu (nome)", city="Cidade/UF"):
    if not text.strip():
        return "Nenhum texto fornecido para transformar em petição."
    facts = split_sentences(text, max_sentences=8)
    petition = f"""EXCELENTÍSSIMO(A) SENHOR(A) DOUTOR(A) JUIZ(A) DE DIREITO DA COMARCA DE {city.upper()}

{petitioner_name}, já qualificado(a), por seu advogado (procuração anexa), vem, respeitosamente, propor a presente

AÇÃO DE RESPONSABILIDADE CIVIL

em face de {respondent_name}, pelos fatos e fundamentos a seguir expostos:

DOS FATOS
{facts}

DO DIREITO
1) Fundamenta-se a presente ação no dever geral de reparar danos, na legislação aplicável e na jurisprudência consolidada.
2) Requer-se a aplicação do disposto nos arts. ... (indicar dispositivos aplicáveis).

DOS PEDIDOS
Diante do exposto, requer:
a) A citação do requerido;
b) A condenação ao pagamento de indenização por danos morais e materiais, em valor a ser arbitrado por Vossa Excelência;
c) A produção de provas em direito admitidas;
d) Condenação em custas e honorários advocatícios.

Termos em que,
Pede deferimento.

{city}, ____ de __________ de 20__.

__________________________________
Advogado / OAB
"""
    return petition

def create_docx_from_text(title, body_text):
    doc = Document()
    doc.add_heading(title, level=1)
    for para in body_text.split("\n\n"):
        doc.add_paragraph(para)
    bio = BytesIO()
    doc.save(bio)
    bio.seek(0)
    return bio

def create_pdf_from_text(title, body_text):
    buffer = BytesIO()
    c = canvas.Canvas(buffer, pagesize=A4)
    width, height = A4
    margin = 50
    y = height - margin
    c.setFont("Helvetica-Bold", 14)
    c.drawString(margin, y, title)
    y -= 24
    c.setFont("Helvetica", 10)
    for paragraph in body_text.split("\n\n"):
        lines = textwrap.wrap(paragraph, 100)
        for line in lines:
            if y < margin + 40:
                c.showPage()
                y = height - margin
            c.drawString(margin, y, line)
            y -= 12
        y -= 8
    c.save()
    buffer.seek(0)
    return buffer

# ---------- UI ----------
st.title("🤖 IA do Advogado Júnior — Protótipo")
st.markdown("Ferramenta de apoio: resumos, revisão e geração de petições (protótipo sem API).")

tabs = st.tabs(["📝 Assistente Jurídico", "📄 Gerador de Petições", "📚 Dicionário Jurídico"])

# ---------------- Assistente Jurídico ----------------
with tabs[0]:
    st.header("Assistente Jurídico")
    st.markdown("Cole abaixo a ementa, decisão ou texto jurídico. Use os botões para gerar resumo, melhorar o texto ou transformar em minuta de petição.")
    user_text = st.text_area("Cole o texto aqui", height=280, placeholder="Cole ementa, acórdão, petição ou trecho jurídico...")
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("🔎 Gerar resumo"):
            summary = summarize_text(user_text, n_sentences=3)
            st.subheader("Resumo (automático)")
            st.write(summary)
            st.download_button("Baixar resumo (.txt)", data=summary, file_name="resumo.txt", mime="text/plain")
    with col2:
        if st.button("✍️ Melhorar texto"):
            improved = improve_text(user_text)
            st.subheader("Versão melhorada (heurística)")
            st.write(improved)
            # oferecer download .docx e .pdf
            docx_b = create_docx_from_text("Versão melhorada", improved)
            pdf_b = create_pdf_from_text("Versão melhorada", improved)
            st.download_button("Baixar .docx", data=docx_b, file_name="texto_melhorado.docx")
            st.download_button("Baixar .pdf", data=pdf_b, file_name="texto_melhorado.pdf")
    with col3:
        if st.button("📑 Transformar em petição"):
            petitioner = st.text_input("Nome do(a) autor(a)", value="Autor (nome)")
            respondent = st.text_input("Nome do(a) réu/ré", value="Réu (nome)")
            city = st.text_input("Cidade/UF", value="Cidade/UF")
            # note: we read values but peticao generated from prefilled defaults - show result
            petition = transform_to_petition_from_text(user_text, petitioner, respondent, city)
            st.subheader("Minuta de Petição (gerada)")
            st.write(petition)
            docx_b = create_docx_from_text("Petição - Minuta", petition)
            pdf_b = create_pdf_from_text("Petição - Minuta", petition)
            st.download_button("Baixar Petição (.docx)", data=docx_b, file_name="peticao_minuta.docx")
            st.download_button("Baixar Petição (.pdf)", data=pdf_b, file_name="peticao_minuta.pdf")

# ---------------- Gerador de Petições ----------------
with tabs[1]:
    st.header("Gerador de Petições (formulário)")
    with st.form("pet_form"):
        tipo_acao = st.selectbox("Tipo de ação", ["Ação de Indenização (dano moral)", "Ação de Cobrança", "Mandado de Segurança", "Habeas Corpus", "Outro"])
        autor = st.text_input("Autor / parte autora", value="Fulano de Tal")
        advogado = st.text_input("Advogado (nome / OAB)", value="Dr. Exemplo - OAB/UF 00000")
        reu = st.text_input("Réu / parte ré", value="Empresa X")
        valor = st.text_input("Valor da causa (R$)", value="0,00")
        cidade = st.text_input("Cidade / Comarca", value="Cidade/UF")
        fatos = st.text_area("Exponha os fatos (resumo)", height=140, placeholder="Descreva os fatos de forma objetiva...")
        pedidos = st.text_area("Pedidos (o que se pleiteia)", height=100, placeholder="Ex.: condenação em R$ X; produção de provas; etc.")
        enviar = st.form_submit_button("Gerar petição")

    if enviar:
        # gerar petição simples
        pet_text = f"""EXCELENTÍSSIMO(A) SENHOR(A) DOUTOR(A) JUIZ(A) DE DIREITO DA COMARCA DE {cidade.upper()}

{autor}, por seu advogado {advogado}, vem, respeitosamente, propor a presente

{tipo_acao.upper()}

em face de {reu}, pelos fatos a seguir:

DOS FATOS
{fatos}

DO DIREITO
(Enquadre jurídico sucinto — indicar dispositivos legais aplicáveis)

DO VALOR DA CAUSA
Dá-se à causa o valor de R$ {valor}.

DOS PEDIDOS
{pedidos}

Termos em que,
Pede deferimento.

{cidade}, ____ de __________ de 20__.

__________________________________
{advogado}
"""
        st.subheader("Petição gerada")
        st.write(pet_text)
        docx_b = create_docx_from_text("Petição Gerada", pet_text)
        pdf_b = create_pdf_from_text("Petição Gerada", pet_text)
        st.download_button("Baixar petição (.docx)", data=docx_b, file_name="peticao_gerada.docx")
        st.download_button("Baixar petição (.pdf)", data=pdf_b, file_name="peticao_gerada.pdf")

# ---------------- Dicionário Jurídico ----------------
with tabs[2]:
    st.header("Dicionário Jurídico Inteligente (protótipo)")
    term = st.text_input("Digite o termo para buscar", placeholder="Ex.: litisconsórcio, repercussão geral, coisa julgada")
    sample_dict = {
        "litisconsórcio": ("Litisconsórcio é a situação em que duas ou mais pessoas figuram no mesmo polo da relação processual, "
                          "podendo ser ativo ou passivo. Ex.: art. 113 do CPC."),
        "repercussão geral": ("No STF, repercussão geral é o filtro de admissibilidade de recursos extraordinários, "
                             "que seleciona questões relevantes do ponto de vista constitucional."),
        "coisa julgada": ("Coisa julgada é a qualidade da decisão judicial que a torna imutável e indiscutível entre as partes, "
                         "após o esgotamento dos recursos previstos em lei.")
    }
    if st.button("Buscar definição"):
        key = term.strip().lower()
        if not key:
            st.info("Digite um termo para buscar.")
        elif key in sample_dict:
            st.subheader(f"Definição: {term}")
            st.write(sample_dict[key])
        else:
            # fallback: gerar explicação simples heurística
            st.subheader(f"Definição aproximada: {term}")
            st.write(f"O termo **{term}** não está no dicionário de amostra. Em geral, pesquise em doutrinas e códigos. "
                     "Aqui vai uma explicação genérica: trata-se de um instituto jurídico relacionado ao contexto processual — "
                     "consulte legislação e jurisprudência específica para definição precisa.")
            st.markdown("**Exemplo prático (genérico):**")
            st.write(f"Imagine um caso em que '{term}' apareça na ementa — a análise dependerá do contexto fático e normativo.")

st.markdown("---")
st.caption("Protótipo sem integração com API. Para respostas avançadas (resumos aprofundados, geração automática baseada em jurisprudência), integramos uma API de linguagem (OpenAI, etc.).")
