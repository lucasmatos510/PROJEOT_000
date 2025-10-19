# 🚀 Guia de Deploy - WADE COLETOR

## 📋 Visão Geral

Este guia explica como fazer deploy do WADE COLETOR em diferentes ambientes usando Flask 2.3.2 e Gunicorn 20.1.0.

## 🔧 Dependências Atualizadas

```txt
Flask==2.3.2          # Framework web estável
gunicorn==20.1.0       # Servidor WSGI para produção
python-dotenv==1.0.1   # Gestão de variáveis de ambiente
```

## 🏗️ Estrutura de Deploy

### Arquivos de Configuração:
- `wsgi.py` - Ponto de entrada da aplicação
- `gunicorn.conf.py` - Configuração do Gunicorn
- `Procfile` - Deploy no Heroku
- `.env` - Variáveis de ambiente

### Scripts de Deploy:
- `scripts/dev.sh` / `scripts/dev.bat` - Desenvolvimento
- `scripts/prod.sh` / `scripts/prod.bat` - Produção

## 🖥️ Deploy Local

### Desenvolvimento (Windows):
```bash
# Executar script de desenvolvimento
scripts\dev.bat

# Ou manualmente:
call venv\Scripts\activate.bat
set FLASK_DEBUG=true
python wsgi.py
```

### Desenvolvimento (Linux/Mac):
```bash
# Executar script de desenvolvimento
chmod +x scripts/dev.sh
./scripts/dev.sh

# Ou manualmente:
source venv/bin/activate
export FLASK_DEBUG=true
python wsgi.py
```

### Produção:
```bash
# Configurar SECRET_KEY primeiro
export SECRET_KEY=sua_chave_super_secreta

# Executar script de produção
./scripts/prod.sh

# Ou com Gunicorn diretamente:
gunicorn --config gunicorn.conf.py wsgi:app
```

## ☁️ Deploy em Nuvem

### Heroku:
```bash
# Fazer login no Heroku
heroku login

# Criar aplicação
heroku create seu-app-wade

# Configurar SECRET_KEY
heroku config:set SECRET_KEY=sua_chave_super_secreta

# Deploy
git push heroku main
```

### Railway:
```bash
# Conectar repositório no Railway
# Configurar variáveis de ambiente:
SECRET_KEY=sua_chave_super_secreta
PORT=5000
```

### DigitalOcean App Platform:
```yaml
# app.yaml
name: wade-coletor
services:
- name: web
  source_dir: /
  github:
    repo: seu-usuario/seu-repo
    branch: main
  run_command: gunicorn --config gunicorn.conf.py wsgi:app
  environment_slug: python
  instance_count: 1
  instance_size_slug: basic-xxs
  envs:
  - key: SECRET_KEY
    value: sua_chave_super_secreta
    scope: RUN_TIME
```

### Docker:
```dockerfile
# Dockerfile
FROM python:3.11-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

ENV FLASK_ENV=production
ENV FLASK_DEBUG=false

EXPOSE 5000

CMD ["gunicorn", "--config", "gunicorn.conf.py", "wsgi:app"]
```

## 🔐 Configuração de Segurança

### Variáveis de Ambiente Obrigatórias:
```bash
SECRET_KEY=sua_chave_super_secreta_e_unica  # OBRIGATÓRIO
FLASK_ENV=production                         # Recomendado
```

### Variáveis Opcionais:
```bash
HOST=0.0.0.0        # Host do servidor
PORT=5000           # Porta do servidor
WORKERS=4           # Número de workers do Gunicorn
TIMEOUT=30          # Timeout das requisições
MAX_REQUESTS=1000   # Máximo de requisições por worker
```

## 📊 Configuração do Gunicorn

### Configuração Automática:
- **Workers:** 2 × CPUs + 1
- **Timeout:** 30 segundos
- **Max Requests:** 1000 (restart automático)
- **Logs:** stdout/stderr
- **Bind:** 0.0.0.0:5000

### Personalizar:
Edite `gunicorn.conf.py` conforme necessário.

## 🔍 Monitoramento

### Verificar Status:
```bash
# Verificar se o servidor está rodando
curl http://localhost:5000

# Verificar logs
tail -f /var/log/gunicorn/access.log
```

### Health Check:
```bash
# Endpoint de saúde (adicionar no futuro)
curl http://localhost:5000/health
```

## 🐛 Troubleshooting

### Problemas Comuns:

1. **SECRET_KEY não configurada:**
   ```bash
   export SECRET_KEY=sua_chave_secreta
   ```

2. **Porta em uso:**
   ```bash
   export PORT=8000  # Usar porta diferente
   ```

3. **Gunicorn não funciona no Windows:**
   ```bash
   # Usar o servidor Flask de desenvolvimento
   python wsgi.py
   ```

4. **Banco de dados não encontrado:**
   ```bash
   # Verificar se data.db existe
   python -c "from app import init_db; init_db()"
   ```

## 📈 Performance

### Recomendações:
- **Produção:** Use Gunicorn + Nginx
- **Load Balancer:** Para alta disponibilidade
- **CDN:** Para arquivos estáticos
- **Database:** PostgreSQL para produção

### Configuração Nginx:
```nginx
server {
    listen 80;
    server_name seu-dominio.com;
    
    location / {
        proxy_pass http://127.0.0.1:5000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
    
    location /static {
        alias /path/to/app/static;
        expires 1y;
    }
}
```

## 📞 Suporte

Para problemas de deploy:
1. Verificar logs do servidor
2. Confirmar variáveis de ambiente
3. Testar localmente primeiro
4. Verificar conectividade de rede

---

**Última atualização:** 18/10/2025  
**Versão:** 2.0 com Flask 2.3.2 + Gunicorn  
**Projeto:** WADE COLETOR