@echo off
REM Script de deploy para desenvolvimento (Windows)
REM Arquivo: scripts/dev.bat

echo 🚀 Iniciando WADE COLETOR em modo desenvolvimento...

REM Ativar ambiente virtual
call venv\Scripts\activate.bat

REM Instalar dependências
pip install -r requirements.txt

REM Configurar variáveis de ambiente para desenvolvimento
set FLASK_ENV=development
set FLASK_DEBUG=true
set HOST=0.0.0.0
set PORT=5000

REM Iniciar servidor de desenvolvimento
python wsgi.py

pause