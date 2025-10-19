# Configuração do Gunicorn para WADE COLETOR
# Otimizado para Render e outros serviços de nuvem

import multiprocessing
import os

# Configurações do servidor
port = os.environ.get("PORT", "10000")
bind = f"0.0.0.0:{port}"

# Workers - otimizado para Render (plano gratuito tem limitações)
workers = int(os.environ.get("WORKERS", "1"))  # Render free tier - usar 1 worker
worker_class = "sync"
worker_connections = 1000
timeout = int(os.environ.get("TIMEOUT", "120"))  # Render tem timeout de 120s
keepalive = 2

# Configurações de segurança e performance
max_requests = int(os.environ.get("MAX_REQUESTS", "1000"))
max_requests_jitter = 50
preload_app = True

# Logs - importante para debug no Render
accesslog = "-"
errorlog = "-"
loglevel = os.environ.get("LOG_LEVEL", "info")
access_log_format = '%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s"'

# Configurações de processo
daemon = False
pidfile = None  # Render não permite PID files
user = None
group = None

# Configurações específicas para Render
reload = False
reload_engine = "auto"

# Bind to all interfaces for cloud deployment
forwarded_allow_ips = "*"
proxy_allow_ips = "*"