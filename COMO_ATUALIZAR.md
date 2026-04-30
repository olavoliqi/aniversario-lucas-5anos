# 📝 Como Atualizar o Site

## Quando você quiser atualizar o site:

### Opção 1: Me manda a lista pelo WhatsApp

**Formato aceito:**
- Excel (.xlsx)
- CSV
- Google Sheets (link público)
- Ou só me fala os nomes/mudanças

**O que eu faço:**
1. Atualizo os arquivos CSV
2. Rodo o script de atualização
3. Faço push no GitHub
4. Te aviso quando o site estiver atualizado (leva ~2 minutos)

### Opção 2: Você mesmo atualiza

Se quiser fazer manualmente:

```bash
# 1. Editar os arquivos CSV
cd /root/.openclaw/workspace/aniversario-lucas-5anos
nano convidados.csv  # ou use vim, etc

# 2. Rodar o script de atualização
/root/.openclaw/workspace/venv-excel/bin/python update.py

# 3. Pronto! Site atualiza em ~1-2 minutos
```

## 🔗 Link do Site

https://olavoliqi.github.io/aniversario-lucas-5anos/

## 📊 Estrutura dos CSVs

### convidados.csv
```csv
Tipo,Nome,Confirmado
Adulto,João Silva,S
Criança,Maria Silva,N
```

### fornecedores.csv
```csv
Fornecedor,Serviço,Valor,Escopo,Confirmado
Buffet ABC,Comida,R$ 5000,Buffet completo,Sim
```

**Status aceitos:**
- Confirmado: `S`, `Sim`, `SIM`
- Não confirmado: `N`, `Não`, `NAO`, `NÃO`
- Pendente: qualquer outro valor (ou vazio)

## 🦞 Jeito Mais Fácil

Me manda a lista atualizada pelo WhatsApp e eu atualizo tudo! 😄
