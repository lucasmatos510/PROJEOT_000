@echo off
REM Build script for Render (Windows compatible)
REM This script is executed during the build process

echo 🚀 Iniciando build do WADE COLETOR no Render...

REM Install Python dependencies
pip install -r requirements.txt
if errorlevel 1 (
    echo ❌ Erro ao instalar dependências
    exit /b 1
)

echo ✅ Dependências instaladas com sucesso!

REM Initialize database if it doesn't exist
python -c "import os; import sqlite3; from app import init_db; init_db() if not os.path.exists('data.db') else print('📄 Banco de dados já existe'); print('✅ Banco configurado!')"

echo ✅ Build concluído com sucesso!