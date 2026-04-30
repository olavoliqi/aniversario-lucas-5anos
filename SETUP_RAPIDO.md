# ⚡ Setup Rápido (5 minutos)

## Passo 1: Google Sheets (2 min)

1. Criar planilha: https://sheets.google.com
2. Nomear: "Aniversário Lucas 5 Anos"
3. Importar `convidados.csv` (Arquivo → Importar)
4. Criar aba "Fornecedores" e importar `fornecedores.csv`
5. **Compartilhar → "Qualquer pessoa com o link" → Copiar link**

## Passo 2: Editar update.py (1 min)

Abrir `update.py` e colar a URL da planilha:

```python
# Linha 11-12:
SHEETS_BASE_URL = "https://docs.google.com/spreadsheets/d/SEU_ID_AQUI"
FORNECEDORES_GID = "1234"  # Pegar do link (depois de gid=)
```

**Como pegar os IDs:**
- URL da planilha: `https://docs.google.com/spreadsheets/d/1ABC.../edit#gid=0`
- `SHEETS_BASE_URL` = tudo até `/edit`
- Para aba Fornecedores, clique nela e veja o `gid=` na URL

## Passo 3: GitHub (1 min)

```bash
cd /root/.openclaw/workspace/aniversario-lucas-5anos
git branch -M main
git remote add origin https://github.com/olavomeyer/aniversario-lucas-5anos.git
git push -u origin main
```

**OU** crie manual:
1. https://github.com/new
2. Nome: `aniversario-lucas-5anos`, público
3. **NÃO** adicione README
4. Copie os comandos que o GitHub mostrar

## Passo 4: Ativar GitHub Pages (1 min)

1. Repo → Settings → Pages
2. Branch: **main**, pasta: **/ (root)**
3. Save

Site vai ficar em: `https://olavomeyer.github.io/aniversario-lucas-5anos/`

## Passo 5: Cron (30 seg)

Me avise que terminei os passos acima e eu configuro o cron automaticamente! 🦞

---

**Dúvidas?** Me chame no WhatsApp!
