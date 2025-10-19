#!/bin/bash
# Script de deploy para produção
# Arquivo: scripts/prod.sh

echo "🚀 Iniciando WADE COLETOR em modo produção..."

# Verificar se SECRET_KEY está configurada
if [ -z "$SECRET_KEY" ]; then
    echo "❌ ERRO: SECRET_KEY não configurada!"
    echo "Configure com: export SECRET_KEY=sua_chave_secreta"
    exit 1
fi

# Ativar ambiente virtual
source venv/bin/activate || source venv/Scripts/activate

# Instalar dependências
pip install -r requirements.txt

# Configurar variáveis de ambiente para produção
export FLASK_ENV=production
export FLASK_DEBUG=false
export HOST=0.0.0.0
export PORT=${PORT:-5000}

echo "✅ Configuração verificada"
echo "🔐 SECRET_KEY: Configurada"
echo "📍 HOST: $HOST"
echo "🔌 PORT: $PORT"

# Iniciar servidor com Gunicorn
gunicorn --config gunicorn.conf.py wsgi:app