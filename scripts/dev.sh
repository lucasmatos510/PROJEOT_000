#!/bin/bash
# Script de deploy para desenvolvimento
# Arquivo: scripts/dev.sh

echo "🚀 Iniciando WADE COLETOR em modo desenvolvimento..."

# Ativar ambiente virtual
source venv/bin/activate || source venv/Scripts/activate

# Instalar dependências
pip install -r requirements.txt

# Configurar variáveis de ambiente para desenvolvimento
export FLASK_ENV=development
export FLASK_DEBUG=true
export HOST=0.0.0.0
export PORT=5000

# Iniciar servidor de desenvolvimento
python wsgi.py