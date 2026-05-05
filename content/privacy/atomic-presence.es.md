---
title: Atomic Presence — Política de privacidad
layout: simple
showDate: false
showReadingTime: false
---

**Última actualización: 15-04-2026**

---

## 1. Resumen

Atomic Presence, desarrollada por QQder339, es una herramienta anti-deepfake que utiliza cadenas de hash criptográficas, firmas digitales y marcas de agua de audio para que las personas usuarias puedan auto-verificar la integridad de sus grabaciones.

**En resumen: NO recopilamos, almacenamos ni transmitimos ninguno de tus datos personales a servidores externos. Todas las operaciones criptográficas y la verificación se realizan en el dispositivo.**

## 2. Datos que NO recopilamos

Esta app no recopila:

- Información de identificación personal (nombre, correo, teléfono)
- Datos de ubicación
- Identificadores de dispositivo
- Datos analíticos o de seguimiento de uso

## 3. Datos almacenados localmente

Los siguientes datos se almacenan estrictamente en tu dispositivo y nunca se transmiten al exterior:

- **Archivos de audio/vídeo**: Todo el contenido grabado se guarda en el almacenamiento local del dispositivo
- **Registros de cadena de hash**: Secuencias de hash SHA-256 y los datos de verificación correspondientes
- **Firmas digitales**: Datos de firma generados por el algoritmo Curve25519 en el propio dispositivo
- **Informes de verificación**: Informes de integridad y registros de metadatos
- **Identificador anonimizado del dispositivo**: Cada `.evidence.json` incluye un prefijo hexadecimal de 16 caracteres de `SHA-256(identifierForVendor)`, usado únicamente para correlacionar grabaciones del mismo dispositivo durante la verificación. Este identificador vive solo dentro de los archivos de evidencia en tu dispositivo, nunca se envía a ningún servidor, y no se puede revertir a la información original del dispositivo

## 4. Funciones criptográficas (completamente offline)

Todas las funciones principales se completan en el dispositivo sin conexión de red:

- **Generación de cadena de hash**: Secuencias de hash SHA-256 en tiempo real; todo el cálculo se ejecuta localmente
- **Firma digital**: Usa el algoritmo Curve25519 para firmar grabaciones en el dispositivo
- **Marca de agua de audio**: Incrusta señales FSK en las grabaciones; todo el procesamiento de señal se ejecuta en el dispositivo
- **Verificación**: La comprobación de integridad se calcula localmente

## 5. Aviso importante

El contenido procesado por esta app (audio, vídeo) puede contener información sensible. Todo el procesamiento ocurre en tu dispositivo, y **no podemos ni accederemos jamás a ninguno de tus contenidos grabados**.

## 6. Servicios de terceros

Esta app **NO** utiliza ningún framework de análisis ni de publicidad de terceros (sin Google Analytics, sin Facebook SDK, sin anuncios).

## 7. Acceso a la red

Esta app **no requiere conexión de red** para usar ninguna de sus funciones. El único acceso a la red es:

- **Enlaces externos**: Abre el navegador al tocar los enlaces correspondientes

## 8. Contáctanos

📧 **qqder339@gmail.com**  
Asunto: Consulta sobre la Política de privacidad de Atomic Presence
