---
title: Soporte de Atomic Presence
layout: simple
summary: Soporte y contacto de Atomic Presence
app_slug: atomic-presence
showDate: false
showReadingTime: false
---


---

## Preguntas frecuentes

**P: El código QR sale borroso en el vídeo y no se puede escanear durante la verificación.**  
R: Asegúrate de que el brillo de la pantalla sea suficiente durante la grabación y mantén la cámara a 30–50 cm de la pantalla. El código QR se actualiza una vez por segundo — la cámara tiene que poder enfocar con nitidez. Si el problema persiste, prueba a reducir la resolución de grabación.

**P: La verificación de la marca de agua de audio falla.**  
R: La verificación de la marca de agua puede fallar si: el audio se comprimió mucho (por ejemplo, reenviado por WhatsApp), el audio se truncó, o había demasiado ruido de fondo. Graba en un entorno silencioso y usa el archivo de audio original para verificar.

**P: La firma digital es inválida en un dispositivo nuevo.**  
R: La clave de firma de cada dispositivo se guarda en el Llavero (Keychain) de iOS, y un dispositivo nuevo genera una clave distinta. NO necesitas exportar manualmente la clave pública: cada `.evidence.json` que escribe la app ya incluye la clave pública usada para firmar esa grabación, así que cualquier verificador que tenga el archivo de evidencia puede comprobarla, sea cual sea su dispositivo.

**P: La app se cerró durante la grabación: ¿el archivo sigue ahí?**  
R: Cuando la app se cierra inesperadamente, pueden quedar grabaciones parciales en el directorio Documents. Vuelve a abrir la app, toca el botón **VERIFICAR** en la parte superior de la pantalla principal y revisa las tres pestañas (Nivel 1 / Nivel 2 / Nivel 3) por si hay archivos recuperables.

**P: La verificación de la cadena de hash dice "integridad rota" pero no he editado la grabación.**  
R: Posibles causas: la app fue interrumpida por el sistema durante la grabación, batería baja, o un error de escritura por falta de espacio. Asegúrate de tener batería y almacenamiento suficientes antes de grabar.

---

## Resolución de problemas

1. **Asegúrate de tener almacenamiento suficiente** (recomendado al menos 2 GB libres)
2. **Mantén la pantalla encendida durante la grabación** para evitar interrupciones del sistema
3. **Forzar cierre y volver a abrir la app**
4. **Comprueba la versión de iOS** ≥ 17.0
5. Si un escenario concreto da problemas de forma constante, haz una captura del mensaje de error y escríbenos

---

## Contacto de soporte

📧 **qqder339@gmail.com**  
Asunto: `[Atomic Presence] Descripción del problema`

Por favor incluye: modelo del dispositivo, versión de iOS, versión de la app, modo de grabación (vídeo/audio), pasos para reproducir.

> Esta app no recoge datos de usuario. Todas las operaciones criptográficas se ejecutan íntegramente en el dispositivo. No tenemos acceso a tus grabaciones.
