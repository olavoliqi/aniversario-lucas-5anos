#!/usr/bin/env python3
"""
Script de atualização automática
Lê Google Sheets público e atualiza o HTML
"""

import csv
import urllib.request
import os
from datetime import datetime

# URLs do Google Sheets (formato: /export?format=csv&gid=SHEET_ID)
SHEETS_BASE_URL = "COLE_AQUI_A_URL_DA_PLANILHA"  # Será substituído depois
CONVIDADOS_GID = "0"  # ID da aba Convidados
FORNECEDORES_GID = "COLE_AQUI"  # ID da aba Fornecedores

def download_csv(url):
    """Baixa CSV do Google Sheets"""
    try:
        with urllib.request.urlopen(url, timeout=30) as response:
            content = response.read().decode('utf-8')
            return content
    except Exception as e:
        print(f"❌ Erro ao baixar CSV: {e}")
        return None

def parse_csv(content):
    """Converte CSV em lista de dicts"""
    if not content:
        return []
    
    lines = content.strip().split('\n')
    reader = csv.DictReader(lines)
    return list(reader)

def generate_convidados_html(convidados):
    """Gera HTML da tabela de convidados"""
    html = ""
    for i, c in enumerate(convidados, 1):
        tipo = c.get('Tipo', '')
        nome = c.get('Nome', '')
        confirmado = c.get('Confirmado', '').upper()
        
        # Badge de tipo
        tipo_badge = f'<span class="badge {tipo.lower()}">{tipo}</span>'
        
        # Badge de status
        if confirmado == 'S' or confirmado == 'SIM':
            status_badge = '<span class="badge sim">✓ Confirmado</span>'
        elif confirmado == 'N' or confirmado == 'NÃO' or confirmado == 'NAO':
            status_badge = '<span class="badge nao">✗ Não confirmado</span>'
        else:
            status_badge = '<span class="badge pendente">⏳ Pendente</span>'
        
        html += f"""
                    <tr>
                        <td>{i}</td>
                        <td>{nome}</td>
                        <td>{tipo_badge}</td>
                        <td>{status_badge}</td>
                    </tr>"""
    
    return html

def generate_fornecedores_html(fornecedores):
    """Gera HTML da tabela de fornecedores"""
    html = ""
    for i, f in enumerate(fornecedores, 1):
        fornecedor = f.get('Fornecedor', '')
        servico = f.get('Serviço', '')
        valor = f.get('Valor', 'R$ 0')
        escopo = f.get('Escopo', '')
        confirmado = f.get('Confirmado', '').upper()
        
        # Badge de status
        if confirmado == 'S' or confirmado == 'SIM':
            status_badge = '<span class="badge sim">✓ Confirmado</span>'
        else:
            status_badge = '<span class="badge nao">✗ Pendente</span>'
        
        html += f"""
                    <tr>
                        <td>{i}</td>
                        <td>{fornecedor}</td>
                        <td>{servico}</td>
                        <td>{valor}</td>
                        <td>{escopo}</td>
                        <td>{status_badge}</td>
                    </tr>"""
    
    return html

def update_html():
    """Atualiza o index.html com dados do Google Sheets"""
    print("🔄 Iniciando atualização...")
    
    # Baixar CSVs
    print("📥 Baixando dados do Google Sheets...")
    
    # Por enquanto, ler dos arquivos locais (depois substitui pelas URLs)
    if os.path.exists('convidados.csv'):
        with open('convidados.csv', 'r', encoding='utf-8') as f:
            convidados_content = f.read()
    else:
        convidados_content = None
    
    if os.path.exists('fornecedores.csv'):
        with open('fornecedores.csv', 'r', encoding='utf-8') as f:
            fornecedores_content = f.read()
    else:
        fornecedores_content = None
    
    # Parse CSVs
    convidados = parse_csv(convidados_content)
    fornecedores = parse_csv(fornecedores_content)
    
    print(f"✅ {len(convidados)} convidados carregados")
    print(f"✅ {len(fornecedores)} fornecedores carregados")
    
    # Gerar HTML
    convidados_html = generate_convidados_html(convidados)
    fornecedores_html = generate_fornecedores_html(fornecedores)
    
    # Ler template
    with open('index.html', 'r', encoding='utf-8') as f:
        html = f.read()
    
    # Substituir placeholders
    html = html.replace('<!-- PLACEHOLDER_CONVIDADOS -->', convidados_html)
    html = html.replace('<!-- PLACEHOLDER_FORNECEDORES -->', fornecedores_html)
    
    # Atualizar timestamp
    now = datetime.now().strftime('%d/%m/%Y às %H:%M')
    html = html.replace('--</span>', f'{now}</span>')
    
    # Salvar
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    
    print("✅ index.html atualizado!")
    
    # Git commit e push
    print("📤 Enviando para GitHub...")
    os.system('git add index.html')
    os.system(f'git commit -m "🤖 Atualização automática - {now}" --allow-empty')
    os.system('git push origin main')
    
    print("✨ Atualização concluída!")

if __name__ == '__main__':
    update_html()
