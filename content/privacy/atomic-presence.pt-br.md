---
title: Atomic Presence — Política de Privacidade
layout: simple
showDate: false
showReadingTime: false
---

**Última atualização: 15/04/2026**

---

## 1. Visão geral

O Atomic Presence, desenvolvido pela QQder339, é uma ferramenta anti-deepfake que utiliza cadeias de hash criptográficas, assinaturas digitais e marcas d'água de áudio para que as pessoas usuárias possam auto-verificar a integridade das suas gravações.

**Resumindo: NÃO coletamos, armazenamos nem transmitimos nenhum dado pessoal seu para servidores externos. Todas as operações criptográficas e a verificação são feitas no dispositivo.**

## 2. Dados que NÃO coletamos

Este app não coleta:

- Informações de identificação pessoal (nome, e-mail, telefone)
- Dados de localização
- Identificadores de dispositivo
- Dados de análise de uso ou rastreamento

## 3. Dados armazenados localmente

Os seguintes dados ficam armazenados estritamente no seu dispositivo e nunca são transmitidos para fora:

- **Arquivos de áudio/vídeo**: Todo o conteúdo gravado é guardado no armazenamento local do dispositivo
- **Registros da cadeia de hash**: Sequências de hash SHA-256 e os dados de verificação correspondentes
- **Assinaturas digitais**: Dados de assinatura gerados pelo algoritmo Curve25519 no próprio dispositivo
- **Relatórios de verificação**: Relatórios de integridade e registros de metadados
- **Identificador anonimizado do dispositivo**: Cada `.evidence.json` embute um prefixo hexadecimal de 16 caracteres de `SHA-256(identifierForVendor)`, usado apenas para correlacionar gravações do mesmo dispositivo durante a verificação. Esse identificador vive apenas dentro dos arquivos de evidência no seu dispositivo, nunca é transmitido a nenhum servidor, e não pode ser revertido para a informação original do dispositivo

## 4. Funções criptográficas (totalmente offline)

Todas as funções principais são concluídas no dispositivo sem conexão com a internet:

- **Geração da cadeia de hash**: Sequências de hash SHA-256 em tempo real; todo o cálculo roda localmente
- **Assinatura digital**: Usa o algoritmo Curve25519 para assinar gravações no dispositivo
- **Marca d'água de áudio**: Embute sinais FSK nas gravações; todo o processamento de sinal roda no dispositivo
- **Verificação**: A checagem de integridade é calculada localmente

## 5. Observação importante

O conteúdo processado por este app (áudio, vídeo) pode conter informações sensíveis. Todo o processamento acontece no seu dispositivo, e **não podemos e nunca acessaremos nenhum dos seus conteúdos gravados**.

## 6. Serviços de terceiros

Este app **NÃO** usa nenhum framework de análise ou publicidade de terceiros (sem Google Analytics, sem Facebook SDK, sem anúncios).

## 7. Acesso à rede

Este app **não requer conexão de rede** para usar nenhuma das suas funções. O único acesso à rede é:

- **Links externos**: Abre o navegador ao tocar nos links relacionados

## 8. Fale conosco

📧 **qqder339@gmail.com**  
Assunto: Consulta sobre a Política de Privacidade do Atomic Presence
