# 🎉 Aniversário Lucas 5 Anos - Sistema de Convidados

Site de gerenciamento de convidados e fornecedores para o aniversário do Lucas.

## 🚀 Setup Inicial (faça uma vez)

### 1. Criar Google Sheets

1. Acesse https://sheets.google.com
2. Crie uma nova planilha chamada "Aniversário Lucas 5 Anos"
3. Crie 2 abas:
   - **Convidados** (Aba 1)
   - **Fornecedores** (Aba 2)

4. **Aba Convidados** - Cole estas colunas exatas:
   ```
   Tipo | Nome | Confirmado
   ```

5. **Aba Fornecedores** - Cole estas colunas exatas:
   ```
   Fornecedor | Serviço | Valor | Escopo | Confirmado
   ```

6. Importar dados iniciais:
   - Vá em **Arquivo → Importar**
   - Upload do arquivo `convidados.csv` (neste repo)
   - Escolha "Substituir planilha atual"
   - Repita para `fornecedores.csv` na aba Fornecedores

7. **Tornar pública:**
   - Clique em "Compartilhar" (botão verde, canto superior direito)
   - Em "Acesso geral", escolha **"Qualquer pessoa com o link pode visualizar"**
   - Copie o link da planilha

8. **Pegar os IDs:**
   - URL da planilha tem esse formato:
     ```
     https://docs.google.com/spreadsheets/d/SPREADSHEET_ID/edit#gid=SHEET_ID
     ```
   - Anote o `SPREADSHEET_ID` (parte grande do meio)
   - Anote o `SHEET_ID` de cada aba (número depois de `gid=`)
     - Convidados: geralmente `gid=0`
     - Fornecedores: `gid=` (algo diferente de 0)

### 2. Configurar Script de Atualização

Edite o arquivo `update.py` e substitua:

```python
SHEETS_BASE_URL = "https://docs.google.com/spreadsheets/d/SPREADSHEET_ID"
CONVIDADOS_GID = "0"  # Geralmente 0
FORNECEDORES_GID = "123456"  # ID da aba Fornecedores
```

### 3. Criar Repositório no GitHub

```bash
# No terminal, dentro da pasta aniversario-lucas-5anos:
git branch -M main
gh repo create aniversario-lucas-5anos --public --source=. --remote=origin --push
```

Se não tiver `gh` instalado, crie manualmente:
1. Vá em https://github.com/new
2. Nome: `aniversario-lucas-5anos`
3. Público
4. Não adicione README, .gitignore ou licença
5. Clique em "Create repository"
6. Depois rode:
   ```bash
   git remote add origin https://github.com/SEU_USUARIO/aniversario-lucas-5anos.git
   git branch -M main
   git push -u origin main
   ```

### 4. Ativar GitHub Pages

1. Vá no repo: `https://github.com/SEU_USUARIO/aniversario-lucas-5anos`
2. Settings → Pages
3. Source: **Deploy from a branch**
4. Branch: **main** / **/ (root)**
5. Save

Aguarde ~2 minutos. Site estará em:
```
https://SEU_USUARIO.github.io/aniversario-lucas-5anos/
```

### 5. Configurar Atualização Automática

Adicione ao cron do servidor (roda de hora em hora):

```bash
# Editar cron:
crontab -e

# Adicionar esta linha:
0 * * * * cd /root/.openclaw/workspace/aniversario-lucas-5anos && /root/.openclaw/workspace/venv-excel/bin/python update.py >> /tmp/aniversario-update.log 2>&1
```

Isso vai:
- Rodar a cada hora (:00)
- Ler Google Sheets
- Atualizar HTML
- Fazer commit e push automaticamente
- Site atualiza em ~1 minuto

## 📝 Como Usar

### Atualizar Convidados
1. Abra o Google Sheets
2. Edite diretamente na planilha:
   - Adicione/remova linhas
   - Mude status (S/N)
3. Salve (automático)
4. Aguarde até 1 hora (ou rode o script manualmente)

### Atualizar Fornecedores
1. Mesma coisa, mas na aba Fornecedores
2. Preencha: Fornecedor, Serviço, Valor, Escopo, Confirmado (Sim/Não)

### Atualização Manual (opcional)
```bash
cd /root/.openclaw/workspace/aniversario-lucas-5anos
/root/.openclaw/workspace/venv-excel/bin/python update.py
```

## 🎨 Personalizações

- **Cores**: Edite o `<style>` em `index.html`
- **Título/Data**: Linha 12-13 de `index.html`
- **Estatísticas**: JavaScript no final de `index.html`

## 📊 Recursos

- ✅ Busca em tempo real
- ✅ Contadores automáticos
- ✅ Design responsivo (mobile-friendly)
- ✅ Atualização automática (cron)
- ✅ Duas abas (Convidados + Fornecedores)
- ✅ Badges coloridos (confirmado/pendente)

## 🦞 Feito por Polvo

Projeto criado automaticamente pelo assistente Polvo.
Última atualização: 30/04/2026
