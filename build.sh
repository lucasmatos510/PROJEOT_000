# Build script for Render
# This script is executed during the build process

#!/bin/bash

echo "🚀 Iniciando build do WADE COLETOR no Render..."

# Install Python dependencies
pip install -r requirements.txt

echo "✅ Dependências instaladas com sucesso!"

# Initialize database if it doesn't exist
python -c "
import os
import sqlite3
from app import init_db

if not os.path.exists('data.db'):
    print('📄 Criando banco de dados...')
    init_db()
    print('✅ Banco de dados criado!')
else:
    print('📄 Banco de dados já existe')
"

echo "✅ Build concluído com sucesso!"