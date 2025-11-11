# ⚖️ IA do Advogado Júnior 🤖

**Protótipo interativo** desenvolvido em **Streamlit**, criado para auxiliar estudantes e profissionais do Direito em tarefas como:
- Resumo de decisões e textos jurídicos;  
- Melhoria e formalização de petições;  
- Geração de minutas completas;  
- Consulta rápida de termos jurídicos.

---

## 🚀 Funcionalidades Principais

### 📝 Assistente Jurídico
Cole um texto (ementa, decisão, parecer, petição etc.) e escolha uma das opções:
- **Gerar resumo**: cria um resumo automático.  
- **Melhorar texto**: reformula com linguagem mais formal.  
- **Transformar em petição**: gera minuta padrão com endereçamento, fatos, fundamentos e pedidos.  

Os resultados podem ser baixados em **.docx** e **.pdf**.

---

### 📄 Gerador de Petições
Formulário que gera uma **petição completa** a partir de informações simples:
- Tipo de ação (dano moral, cobrança, mandado de segurança etc.);
- Dados das partes;
- Fatos e pedidos.

Gera o texto final formatado e pronto para download.

---

### 📚 Dicionário Jurídico
Busca inteligente que fornece definições e exemplos de termos jurídicos comuns.  
Se o termo não estiver no dicionário local, o app fornece uma explicação genérica com contexto jurídico.

---

## 🧠 Futuras Melhorias
- Integração com **OpenAI API** (para resumos e textos de alta precisão).  
- Acesso a **bases reais de jurisprudência** (STF/STJ).  
- Geração automática de petições baseadas em casos similares.  
- Interface com **modo escuro** e design mais moderno.

---

## 💻 Instalação e Execução

### 1️⃣ Clone o repositório
```bash
git clone https://github.com/SEU_USUARIO/ia-advogado-junior.git
cd ia-advogado-junior
python -m venv venv
source venv/bin/activate   # Linux/macOS
venv\Scripts\activate      # Windows
pip install -r requirements.txt
streamlit run app.py
streamlit
pandas
python-docx
reportlab
