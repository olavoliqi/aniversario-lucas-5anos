# 🎉 Aniversário Lucas 5 Anos

Site de gerenciamento de convidados para o aniversário do Lucas.

## 🔗 Link do Site

**https://olavoliqi.github.io/aniversario-lucas-5anos/**

## ✨ Características

- ✅ **HTML estático completo** (todos os dados embutidos)
- ✅ **182 convidados** já carregados
- ✅ **Zero dependências** externas (não precisa CSV, Google Sheets, scripts)
- ✅ **Design responsivo** (funciona perfeitamente em celular)
- ✅ **Busca em tempo real** por nome
- ✅ **Contadores automáticos** (total, confirmados, pendentes, %)
- ✅ **Tema festa infantil** (cores vibrantes e modernas)
- ✅ **Duas abas:** Convidados e Fornecedores

## 📱 Recursos

### Aba Convidados
- Lista completa de convidados (adultos e crianças)
- Status de confirmação visual (badges coloridos)
- Busca instantânea
- Estatísticas em tempo real

### Aba Fornecedores
- Lista de fornecedores (a ser preenchida)
- Informações: serviço, valor, escopo, status
- (Atualmente vazia - adicione conforme necessário)

## 🔄 Como Atualizar o Site

### Método Simples (Recomendado)
**Envie a lista atualizada para o Polvo pelo WhatsApp:**
- Excel (.xlsx) ✅
- CSV ✅
- Google Sheets (link) ✅
- Ou apenas descreva as mudanças ✅

O Polvo atualiza o HTML e faz o deploy em ~2 minutos.

### Método Manual (se preferir)
1. Edite o `index.html` (dados estão na variável JavaScript `convidados`)
2. Faça commit: `git add index.html && git commit -m "Atualização"`
3. Push: `git push`
4. Site atualiza automaticamente em ~1-2 minutos

## 📊 Estrutura dos Dados

Os dados estão embutidos no JavaScript do `index.html`:

```javascript
const convidados = [
  {
    "tipo": "Adulto",
    "nome": "João Silva",
    "confirmado": "S"  // S, N, ou vazio
  },
  ...
];
```

**Status aceitos:**
- `"S"` ou `"SIM"` → Badge verde "✓ Confirmado"
- `"N"` ou `"NÃO"` ou `"NAO"` → Badge vermelho "✗ Não confirmado"
- Qualquer outro valor ou vazio → Badge laranja "⏳ Pendente"

## 🎨 Design

- Gradiente roxo/rosa (tema festa infantil)
- Badges coloridos por tipo (Adulto = azul, Criança = rosa)
- Badges de status (Verde = confirmado, Vermelho = não, Laranja = pendente)
- Responsivo para mobile
- Busca em tempo real

## 🦞 Feito por Polvo

Site criado automaticamente pelo assistente Polvo.

**Última atualização:** 30/04/2026
