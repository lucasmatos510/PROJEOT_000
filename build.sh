# Build script for Render
# This script is executed during the build process

#!/bin/bash

# Build script for Render - WADE COLETOR
# This script is executed during the build process

set -e  # Exit on any error

echo "🚀 Iniciando build do WADE COLETOR no Render..."

# Update pip first
pip install --upgrade pip

echo "📦 Instalando dependências Python..."
pip install -r requirements.txt

echo "✅ Dependências instaladas com sucesso!"

# Create data directory if it doesn't exist
mkdir -p data

# Initialize database if it doesn't exist
echo "📄 Configurando banco de dados..."
python3 -c "
import os
import sys
sys.path.insert(0, '.')

try:
    from app import init_db
    
    if not os.path.exists('data.db'):
        print('📄 Criando banco de dados...')
        init_db()
        print('✅ Banco de dados criado!')
    else:
        print('📄 Banco de dados já existe')
except Exception as e:
    print(f'⚠️ Aviso: {e}')
    print('Banco será criado durante a primeira execução')
"

# Test if the app can be imported
echo "🧪 Testando importação da aplicação..."
python3 -c "
try:
    from app import app
    print('✅ Aplicação importada com sucesso!')
except Exception as e:
    print(f'❌ Erro na importação: {e}')
    exit(1)
"

echo "✅ Build concluído com sucesso!"
echo "🚀 Pronto para iniciar com Gunicorn!"