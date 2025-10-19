# 🚀 Deploy no Render - WADE COLETOR

## 📋 Instruções Completas para Deploy

### 🔗 **Passo 1: Preparar Repositório**

1. **Commit todos os arquivos:**
   ```bash
   git add .
   git commit -m "Preparação para deploy no Render"
   git push origin main
   ```

### 🌐 **Passo 2: Criar Conta no Render**

1. Acesse: https://render.com
2. Faça login com GitHub
3. Autorize o Render a acessar seus repositórios

### 🚀 **Passo 3: Deploy da Aplicação**

#### **Método 1 - Blueprint (Recomendado):**
1. No dashboard do Render, clique em "New +"
2. Selecione "Blueprint"
3. Conecte seu repositório
4. O arquivo `render.yaml` configurará tudo automaticamente

#### **Método 2 - Manual:**
1. No dashboard do Render, clique em "New +"
2. Selecione "Web Service"
3. Conecte seu repositório GitHub
4. Configure:
   - **Name:** wade-coletor
   - **Environment:** Python 3
   - **Build Command:** `./build.sh`
   - **Start Command:** `gunicorn --config gunicorn.conf.py wsgi:app`
   - **Plan:** Free

### 🔐 **Passo 4: Configurar Variáveis de Ambiente**

No dashboard do Render, vá em "Environment" e adicione:

```bash
SECRET_KEY=sua_chave_super_secreta_aqui
FLASK_ENV=production
FLASK_DEBUG=false
PORT=10000
HOST=0.0.0.0
```

**⚠️ IMPORTANTE:** 
- Gere uma SECRET_KEY forte e única
- Use um gerador online ou Python: `import secrets; print(secrets.token_urlsafe(32))`

### 📁 **Arquivos Necessários (Todos Incluídos):**

✅ **Arquivos Principais:**
- `app.py` - Aplicação Flask principal
- `wsgi.py` - Ponto de entrada otimizado para Render
- `requirements.txt` - Dependências Python
- `runtime.txt` - Versão específica do Python
- `gunicorn.conf.py` - Configuração do servidor

✅ **Arquivos de Deploy:**
- `render.yaml` - Configuração automática (Blueprint)
- `build.sh` - Script de build
- `Procfile` - Compatibilidade com outros serviços

✅ **Arquivos de Configuração:**
- `.env` - Variáveis de ambiente padrão
- `.gitignore` - Arquivos ignorados pelo Git

✅ **Templates e Estáticos:**
- `templates/` - Todos os templates HTML
- `static/` - CSS, JS e imagens
- Scanner de código de barras incluído

### 🔧 **Comandos de Build:**

**Build Command:**
```bash
./build.sh
```

**Start Command:**
```bash
gunicorn --config gunicorn.conf.py wsgi:app
```

### 🌍 **URLs de Acesso:**

Após o deploy, sua aplicação estará disponível em:
```
https://seu-app-name.onrender.com
```

### 📊 **Funcionalidades Disponíveis:**

✅ **Scanner de Código de Barras** - ZXing-js moderno
✅ **Sistema de Login de Empresas** - Autenticação segura
✅ **Dashboard por Empresa** - Dados isolados
✅ **Coleta de Produtos** - Interface responsiva
✅ **Administração** - Gestão completa
✅ **Suporte Técnico** - Página de contato com WhatsApp
✅ **Design Responsivo** - Mobile-first

### 🔍 **Verificação Pós-Deploy:**

1. **Testar Homepage:**
   ```
   https://seu-app.onrender.com/
   ```

2. **Testar Login de Empresa:**
   ```
   https://seu-app.onrender.com/empresa-login
   ```

3. **Testar Scanner:**
   ```
   https://seu-app.onrender.com/coleta
   ```

4. **Testar Admin:**
   ```
   https://seu-app.onrender.com/admin-login
   ```

### 🛠️ **Troubleshooting:**

#### **Erro de Build:**
- Verificar se todos os arquivos estão no repositório
- Confirmar que `build.sh` tem permissões de execução
- Verificar logs na aba "Events" do Render

#### **Erro de Inicialização:**
- Verificar se SECRET_KEY está configurada
- Confirmar Start Command
- Verificar logs da aplicação

#### **Erro 503:**
- Aguardar alguns minutos (cold start)
- Verificar se a aplicação está respondendo na porta correta
- Render free tier pode hibernar após inatividade

### 💡 **Dicas de Otimização:**

1. **Performance:**
   - Render free tier hiberna após 15 min de inatividade
   - Primeira requisição pode ser lenta (cold start)
   - Use plano pago para produção

2. **Monitoramento:**
   - Acompanhe logs na aba "Logs"
   - Configure alertas se necessário
   - Verifique métricas de uso

3. **Segurança:**
   - Mantenha SECRET_KEY privada
   - Use HTTPS sempre (Render fornece automaticamente)
   - Monitore tentativas de acesso

### 📞 **Suporte:**

- **Documentação Render:** https://render.com/docs
- **Status Page:** https://status.render.com
- **Logs da Aplicação:** Dashboard > Logs
- **Support:** help@render.com

### 🎉 **Deploy Completo!**

Sua aplicação WADE COLETOR está agora rodando em produção no Render com:
- ✅ Scanner de código de barras funcional
- ✅ Sistema de autenticação seguro
- ✅ Design responsivo
- ✅ Configuração de produção otimizada
- ✅ SSL/HTTPS automático
- ✅ Monitoramento e logs

---

**Criado em:** 18/10/2025  
**Versão:** 2.0 - Otimizado para Render  
**Projeto:** WADE COLETOR