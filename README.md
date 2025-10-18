# Sistema de Coleta de Dados de Produtos – WADE Coleta

## Descrição
O **Jojo Coleta** é um sistema web desenvolvido em **Flask (Python)** com front-end em **HTML, CSS e JavaScript**, voltado para **supermercados e redes de lojas com grande volume de produtos**.  
O sistema tem como objetivo **automatizar a coleta de informações e códigos de barras de produtos**, reduzindo erros no cadastramento e agilizando a integração com sistemas fiscais, proporcionando uma gestão administrativa mais moderna e eficiente.

Um dos diferenciais do sistema é a implementação de **login por empresa**, garantindo que cada usuário visualize apenas os dados da sua própria empresa. Essa funcionalidade permite **comercializar o sistema para diversas redes** sem comprometer a segurança e a privacidade dos dados.

---

## Funcionalidades Principais
- Coleta automática de dados e códigos de barras de produtos  
- Cadastro e atualização de produtos com redução de erros manuais  
- Login individual para cada empresa, com visualização exclusiva de seus próprios dados  
- Interface intuitiva e dinâmica com HTML, CSS e JavaScript  
- Integração prática com sistemas fiscais  
- Base sólida para expansão e personalização para diferentes redes de supermercados

---

## Tecnologias Utilizadas
- **Backend:** Python / Flask  
- **Front-end:** HTML, CSS e JavaScript  
- **Banco de dados:** SQLite (ou outro banco utilizado)  
- **Gerenciamento de dependências:** `requirements.txt`  
- **Templates:** Jinja2  

---

## Como Rodar o Projeto
```bash
# Clonar o repositório
git clone https://github.com/seu_usuario/nome-do-repositorio.git
cd nome-do-repositorio

# Criar ambiente virtual e ativar
python -m venv venv
# Linux/Mac
source venv/bin/activate
# Windows
venv\Scripts\activate

# Instalar dependências
pip install -r requirements.txt

# Executar o sistema
python app.py
