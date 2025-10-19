@echo off
REM Script de deploy para produção (Windows)
REM Arquivo: scripts/prod.bat

echo 🚀 Iniciando WADE COLETOR em modo produção...

REM Verificar se SECRET_KEY está configurada
if "%SECRET_KEY%"=="" (
    echo ❌ ERRO: SECRET_KEY não configurada!
    echo Configure com: set SECRET_KEY=sua_chave_secreta
    pause
    exit /b 1
)

REM Ativar ambiente virtual
call venv\Scripts\activate.bat

REM Instalar dependências
pip install -r requirements.txt

REM Configurar variáveis de ambiente para produção
set FLASK_ENV=production
set FLASK_DEBUG=false
set HOST=0.0.0.0
if "%PORT%"=="" set PORT=5000

echo ✅ Configuração verificada
echo 🔐 SECRET_KEY: Configurada
echo 📍 HOST: %HOST%
echo 🔌 PORT: %PORT%

REM Iniciar servidor com Gunicorn
gunicorn --config gunicorn.conf.py wsgi:app

pause