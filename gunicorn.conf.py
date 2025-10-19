# Configuração do Gunicorn para WADE COLETOR
# Simplificada para Render

import os

# Configurações básicas do servidor
port = os.environ.get("PORT", "10000")
bind = f"0.0.0.0:{port}"

# Workers - otimizado para Render free tier
workers = 1  # Render free tier funciona melhor com 1 worker
worker_class = "sync"
timeout = 120  # Render timeout máximo
keepalive = 2

# Logs para debug
accesslog = "-"
errorlog = "-"
loglevel = "info"

# Configurações essenciais
preload_app = True
max_requests = 1000
max_requests_jitter = 50

# Bind para cloud
forwarded_allow_ips = "*"
proxy_allow_ips = "*"

# Não usar PID files no Render
daemon = False
pidfile = None