# Guía de registro de sensor de suelo Wincontop (material para GitHub)

Este directorio contiene entregables corregidos y ampliados de la reunión de Zoom.

## Contenido

- `transcript.txt`  
  Transcripción completa en texto.
- `transcript.json`  
  Transcripción con segmentos y timestamps.
- `important_steps.json`  
  Pasos relevantes detectados automáticamente (versión breve).
- `important_steps_detailed.json`  
  Pasos ampliados y curados (versión recomendada).
- `GUIA_PASO_A_PASO_WINCONTOP.md`  
  SOP detallado para operación en terreno.
- `frames/`  
  Capturas de pantalla del video en momentos clave.
- `Guia_registro_sensor_suelo_Wincontop.pptx`  
  Presentación final breve.
- `Guia_registro_sensor_suelo_Wincontop_v2_detallada.pptx`  
  Presentación corregida y ampliada.

## Objetivo

Documentar un flujo operativo completo para configurar sensor de suelo Wincontop en plataforma: tipo de sensor, asociación de variables, unidad de CE (µS/cm), mapeo de link, duplicación de dispositivo y validación final.

## Estructura sugerida del repositorio

```text
/docs/wincontop-sensor-suelo/
  README.md
  GUIA_PASO_A_PASO_WINCONTOP.md
  transcript.txt
  transcript.json
  important_steps.json
  important_steps_detailed.json
  Guia_registro_sensor_suelo_Wincontop.pptx
  Guia_registro_sensor_suelo_Wincontop_v2_detallada.pptx
  /frames/
```

## Plataforma objetivo (web)

- URL: `https://sensores.cmasccp.cl/registrar`

### ¿Qué es esta página?

La URL pertenece a la plataforma de sensores del **Centro de investigación en tecnologías para la sociedad (C+)** y corresponde al módulo de **registro/gestión de dispositivos**.

Al revisar la web se observa:
- Menú con secciones: **Inicio, Dashboard, Dispositivos, Datos, Protocolos, Banco de datos**.
- Mensaje de **Acceso Restringido**: para ver contenido operativo se requiere iniciar sesión.

Esto confirma que el flujo documentado en esta guía (tipo de sensor, variables en sensores, mapeo y validación) se ejecuta dentro de un entorno autenticado de esa plataforma.

## Recomendaciones antes de publicar

- Corregir frases de ASR que puedan estar ambiguas (audio con ruido).
- Revisar y anonimizar nombres o datos sensibles.
- Confirmar que cada captura coincida con el paso descrito.

## Estado

- Whisper local: configurado en `C:\whisper`
- Transcripción: completada
- Capturas clave: completadas
- Documentación detallada (MD): completada
- PPT v2 ampliada: completada
