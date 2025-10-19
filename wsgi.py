#!/usr/bin/env python3
"""
Arquivo de entrada para o WADE COLETOR
Otimizado para deploy em produção (Render, Heroku, etc.)
"""

import os
from dotenv import load_dotenv

# Carregar variáveis de ambiente
load_dotenv()

# Importar a aplicação Flask
from app import app

# Configuração específica para produção
if __name__ == "__main__":
    # Configurações para diferentes ambientes
    debug_mode = os.environ.get('FLASK_DEBUG', 'false').lower() == 'true'
    port = int(os.environ.get('PORT', 10000))  # Render usa porta 10000 por padrão
    host = os.environ.get('HOST', '0.0.0.0')
    
    print(f"🚀 Iniciando WADE COLETOR...")
    print(f"📍 Host: {host}")
    print(f"🔌 Porta: {port}")
    print(f"🐛 Debug: {debug_mode}")
    print(f"🔐 SECRET_KEY configurada: {bool(os.environ.get('SECRET_KEY'))}")
    print(f"🌍 Ambiente: {os.environ.get('FLASK_ENV', 'development')}")
    
    # Iniciar servidor
    app.run(
        host=host,
        port=port,
        debug=debug_mode,
        threaded=True
    )
else:
    # Para uso com Gunicorn
    print("🚀 WADE COLETOR carregado para produção")
    print(f"🔐 SECRET_KEY configurada: {bool(os.environ.get('SECRET_KEY'))}")
    print(f"🌍 Ambiente: {os.environ.get('FLASK_ENV', 'production')}")