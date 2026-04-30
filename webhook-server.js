#!/usr/bin/env node
/**
 * Webhook server para processar atualizações do site
 * Recebe mudanças, atualiza JSON, faz push no GitHub
 */

const express = require('express');
const fs = require('fs');
const { execSync } = require('child_process');
const app = express();
const PORT = process.env.PORT || 3050;

// Middleware
app.use(express.json({ limit: '10mb' }));
app.use(express.urlencoded({ extended: true }));

// CORS para permitir requisições do GitHub Pages
app.use((req, res, next) => {
  res.header('Access-Control-Allow-Origin', '*');
  res.header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS');
  res.header('Access-Control-Allow-Headers', 'Content-Type');
  
  if (req.method === 'OPTIONS') {
    return res.sendStatus(200);
  }
  
  next();
});

// Endpoint de atualização
app.post('/update', (req, res) => {
  try {
    const { convidados, tipo, usuario } = req.body;
    
    if (!convidados || !Array.isArray(convidados)) {
      return res.status(400).json({ 
        success: false, 
        error: 'Dados inválidos' 
      });
    }
    
    console.log(`[${new Date().toISOString()}] Recebida atualização (${tipo || 'edição'})`);
    console.log(`Total de convidados: ${convidados.length}`);
    
    // Salvar JSON
    const jsonPath = '/root/.openclaw/workspace/aniversario-lucas-5anos/convidados.json';
    fs.writeFileSync(jsonPath, JSON.stringify(convidados, null, 2), 'utf-8');
    
    // Git commit e push
    try {
      execSync('cd /root/.openclaw/workspace/aniversario-lucas-5anos && git add convidados.json', { encoding: 'utf-8' });
      
      const commitMsg = tipo 
        ? `🔄 Atualização: ${tipo} (${new Date().toLocaleString('pt-BR', { timeZone: 'America/Sao_Paulo' })})`
        : `🔄 Atualização manual (${new Date().toLocaleString('pt-BR', { timeZone: 'America/Sao_Paulo' })})`;
      
      execSync(`cd /root/.openclaw/workspace/aniversario-lucas-5anos && git commit -m "${commitMsg}"`, { encoding: 'utf-8' });
      
      // Configurar credenciais temporárias (token deve vir de variável de ambiente)
      const token = process.env.GITHUB_TOKEN;
      if (!token) {
        throw new Error('GITHUB_TOKEN não configurado');
      }
      
      execSync(`echo "https://olavoliqi:${token}@github.com" > ~/.git-credentials`, { encoding: 'utf-8' });
      execSync('git config --global credential.helper store', { encoding: 'utf-8' });
      
      execSync('cd /root/.openclaw/workspace/aniversario-lucas-5anos && git push', { encoding: 'utf-8' });
      
      // Limpar credenciais
      execSync('rm -f ~/.git-credentials', { encoding: 'utf-8' });
      execSync('git config --global --unset credential.helper', { encoding: 'utf-8' });
      
      console.log('✅ Push realizado com sucesso!');
    } catch (gitError) {
      console.error('Erro no git:', gitError.message);
      // Continua mesmo com erro de git (pode não ter mudanças)
    }
    
    res.json({ 
      success: true, 
      message: 'Atualização processada com sucesso!',
      timestamp: new Date().toISOString()
    });
    
  } catch (error) {
    console.error('Erro ao processar atualização:', error);
    res.status(500).json({ 
      success: false, 
      error: error.message 
    });
  }
});

// Health check
app.get('/health', (req, res) => {
  res.json({ 
    status: 'ok', 
    timestamp: new Date().toISOString() 
  });
});

// Iniciar servidor
app.listen(PORT, '0.0.0.0', () => {
  console.log(`🦞 Webhook server rodando na porta ${PORT}`);
  console.log(`Endpoint: http://localhost:${PORT}/update`);
  console.log(`Health: http://localhost:${PORT}/health`);
});
