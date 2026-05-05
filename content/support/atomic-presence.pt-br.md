---
title: Suporte do Atomic Presence
layout: simple
summary: Suporte e contato do Atomic Presence
app_slug: atomic-presence
showDate: false
showReadingTime: false
---


---

## Perguntas frequentes

**P: O QR code aparece borrado no vídeo e não consegue ser lido na verificação.**  
R: Garanta brilho suficiente na tela durante a gravação e mantenha a câmera a 30–50 cm da tela. O QR code atualiza uma vez por segundo — a câmera precisa conseguir focar com nitidez. Se o problema continuar, tente reduzir a resolução de gravação.

**P: A verificação da marca d'água de áudio falha.**  
R: A verificação da marca d'água pode falhar se: o áudio foi muito comprimido (por exemplo, encaminhado pelo WhatsApp), o áudio foi cortado, ou havia muito ruído de fundo. Grave em um ambiente silencioso e use o arquivo de áudio original para verificar.

**P: A assinatura digital fica inválida em um dispositivo novo.**  
R: A chave de assinatura de cada dispositivo fica armazenada no Keychain do iOS, e um dispositivo novo gera uma chave diferente. Você NÃO precisa exportar manualmente a chave pública — cada `.evidence.json` gravado pelo app já embute a chave pública usada para assinar aquela gravação, então qualquer verificador que tenha o arquivo de evidência consegue verificar, independente do dispositivo.

**P: O app travou durante a gravação — o arquivo ainda está lá?**  
R: Quando o app trava inesperadamente, gravações parciais podem permanecer no diretório Documents. Reabra o app, toque no botão **VERIFICAR** no topo da tela principal e confira as três abas (Nível 1 / Nível 2 / Nível 3) em busca de arquivos recuperáveis.

**P: A verificação da cadeia de hash mostra "integridade quebrada", mas eu não editei a gravação.**  
R: Causas possíveis: o app foi interrompido pelo sistema durante a gravação, bateria baixa, ou erro de escrita por falta de armazenamento. Garanta bateria e armazenamento suficientes antes de gravar.

---

## Solução de problemas

1. **Garanta armazenamento suficiente no dispositivo** (recomendado pelo menos 2 GB livres)
2. **Mantenha a tela ligada durante a gravação** para evitar interrupções do sistema
3. **Force o fechamento e reabra o app**
4. **Verifique a versão do iOS** ≥ 17.0
5. Se um cenário específico causar problemas de forma consistente, tire um print da mensagem de erro e nos envie por e-mail

---

## Contato de suporte

📧 **qqder339@gmail.com**  
Assunto: `[Atomic Presence] Descrição do problema`

Por favor inclua: modelo do dispositivo, versão do iOS, versão do app, modo de gravação (vídeo/áudio), passos para reproduzir.

> Este app não coleta dados de usuário. Todas as operações criptográficas rodam inteiramente no dispositivo. Não temos acesso às suas gravações.
