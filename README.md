# ⚖️ IA do Advogado Júnior — Versão Estética Aprimorada 🤖

Um aplicativo jurídico interativo em **Streamlit**, criado para auxiliar estudantes e profissionais do Direito com tarefas cotidianas como:
- Resumo e aperfeiçoamento de textos jurídicos;  
- Geração de petições automáticas;  
- Consulta de termos e conceitos jurídicos.

---

## 🏛️ Design e Identidade Visual

O novo layout segue o estilo **clássico jurídico**, combinando elegância e clareza:

🎨 **Cores:** Azul-marinho e branco  
🧭 **Layout:** Menu lateral fixo  
🪶 **Fonte:** Georgia (tradicional e formal)  
💼 **Detalhes:** Cards com sombra, ícones, gradiente sutil e sidebar institucional  

---

## 🚀 Funcionalidades

### 📝 Assistente Jurídico
Cole um texto (ementa, decisão, parecer ou petição) e escolha:
- **🔍 Resumir** – Gera um resumo automático.  
- **✍️ Melhorar Texto** – Reformula com linguagem mais formal e clara.  
- **📑 Transformar em Petição** – Gera uma minuta completa com estrutura jurídica.  

Os resultados podem ser baixados em **.docx** e **.pdf**.

---

### 📄 Gerador de Petições
Formulário que gera petições completas com base em informações básicas:
- Tipo de ação  
- Dados das partes  
- Fatos e pedidos  

Produz o texto final formatado e disponível para download.

---

### 📚 Dicionário Jurídico
Busca termos e conceitos jurídicos comuns.  
Se o termo não estiver na base local, o app oferece uma explicação genérica e orientações para pesquisa em doutrina.

---

## 🧠 Futuras Melhorias
- Integração com **OpenAI API** (para resumos e textos de alta qualidade).  
- Acesso a **bases reais de jurisprudência (STF/STJ)**.  
- Geração de petições com fundamentação automática.  
- Tema escuro alternável e salvamento de histórico de textos.  

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
📚 Fontes dos Dados Jurídicos
O aplicativo utiliza definições extraídas de bases oficiais do Direito brasileiro.
As fontes utilizadas são:
Glossário Jurídico do Conselho Nacional de Justiça (CNJ)
Glossário Jurídico do Superior Tribunal de Justiça (STJ)
Glossário Jurídico da Câmara dos Deputados
Código de Processo Civil (Lei 13.105/2015)
Constituição Federal de 1988
O arquivo dicionario_juridico.csv, presente no repositório, contém todas as definições e respectivas fontes, conforme exigido no trabalho.
📚 Fontes dos Dados
As definições de termos jurídicos utilizadas no aplicativo foram extraídas integralmente do:
Tribunal de Justiça de São Paulo (TJSP)
Vocabulário Jurídico dos Juizados Especiais
https://www.tjsp.jus.br/JuizadosEspeciais/JuizadosEspeciais/VocabularioJuridico
O arquivo glossario_consolidado.csv contém os termos originais e está incluído no repositório, conforme exigido para uso de dados reais no projeto.
