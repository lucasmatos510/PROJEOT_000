# 🔐 Configuração de Variáveis de Ambiente

## 📋 Visão Geral

O WADE COLETOR agora usa variáveis de ambiente para configurações sensíveis, seguindo as melhores práticas de segurança.

## 🚀 Como Configurar

### 1. Arquivo .env
O projeto inclui um arquivo `.env` com configurações padrão. Para personalizar:

```bash
# Copie o arquivo .env para .env.local (opcional)
cp .env .env.local

# Edite as configurações conforme necessário
```

### 2. Variáveis Principais

#### SECRET_KEY (Obrigatória em Produção)
```bash
SECRET_KEY=sua_chave_super_secreta_aqui
```

**⚠️ IMPORTANTE:**
- Use uma chave forte e única em produção
- Nunca compartilhe esta chave
- Gere uma nova chave para cada ambiente

### 3. Gerando uma SECRET_KEY Segura

#### Método 1 - Python:
```python
import secrets
print(secrets.token_urlsafe(32))
```

#### Método 2 - Online:
Use um gerador de chaves online confiável

#### Método 3 - OpenSSL:
```bash
openssl rand -base64 32
```

## 🔧 Configuração por Ambiente

### Desenvolvimento
```bash
SECRET_KEY=dev_key_apenas_para_desenvolvimento
FLASK_DEBUG=true
FLASK_ENV=development
```

### Produção
```bash
SECRET_KEY=chave_super_forte_e_unica_para_producao
FLASK_ENV=production
FLASK_DEBUG=false
```

## 📂 Estrutura de Arquivos

```
projeto/
├── .env                 # Configurações padrão (versionado)
├── .env.local          # Configurações locais (não versionado)
├── .env.production     # Configurações de produção (não versionado)
└── .gitignore          # Ignora arquivos .env.local e similares
```

## 🛡️ Segurança

### ✅ Boas Práticas:
- Use SECRET_KEY única para cada ambiente
- Mantenha .env.local fora do controle de versão
- Use chaves longas e aleatórias (mínimo 32 caracteres)
- Rotacione chaves regularmente em produção

### ❌ Evite:
- Compartilhar chaves secretas
- Usar chaves fracas como "123456"
- Versionar arquivos .env.local
- Reutilizar chaves entre ambientes

## 📋 Exemplo de Deploy

### Heroku:
```bash
heroku config:set SECRET_KEY=sua_chave_secreta
```

### Docker:
```bash
docker run -e SECRET_KEY=sua_chave_secreta seu_app
```

### Servidor Linux:
```bash
export SECRET_KEY=sua_chave_secreta
python app.py
```

## 🔍 Verificação

Para verificar se as variáveis estão carregadas:

```python
import os
print("SECRET_KEY configurada:", bool(os.environ.get("SECRET_KEY")))
```

## 📞 Suporte

Se encontrar problemas com as configurações de ambiente:
1. Verifique se o arquivo .env existe
2. Confirme que python-dotenv está instalado
3. Teste com `python -c "import os; print(os.environ.get('SECRET_KEY'))"`

---

**Última atualização:** 18/10/2025  
**Versão:** 2.0  
**Projeto:** WADE COLETOR