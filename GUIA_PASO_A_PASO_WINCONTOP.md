# SOP - Registro de sensor de suelo Wincontop

Documento corregido y ampliado a partir de la reunión de Zoom.

## Alcance

Configuración de sensor de suelo Wincontop con variables de humedad, temperatura y conductividad, incluyendo asociación en plataforma, mapeo de enlace y validación final.

## Pre-requisitos

- Acceso al administrador de la plataforma
- Proyecto de monitoreo de suelos creado
- Dispositivo base existente (recomendado para duplicar)
- Datasheet de Wincontop para confirmar unidades

## Checklist detallado

### 1. Inicio del flujo (00:21)

- **Acción:** Entrar al administrador para registrar sensor de suelo y revisar estado actual.

- **Evidencia (transcripción):** "y quiero registrar o hacer mejor un menos encerno"

### 2. Sensor tipo vs sensor (00:46)

- **Acción:** Aclarar que primero se valida/crea el tipo de sensor y luego el sensor/dispositivo.

- **Evidencia (transcripción):** "Por lo que estés, porque tenemos el sensor de tipo y el sensor."

### 3. Reutilizar entidades existentes (01:12)

- **Acción:** Si el sensor ya existe, no recrearlo; completar asociaciones faltantes.

- **Evidencia (transcripción):** "El sensor es probablemente tal no lo usas"

### 4. Diagnóstico principal (03:13)

- **Acción:** La conductividad no aparecía por asociación incompleta de variables.

- **Evidencia (transcripción):** "Pero..."

### 5. Unidad de medida (03:52)

- **Acción:** Conductividad en µS/cm según datasheet.

- **Evidencia (transcripción):** "¿En qué unidad de medida mía es la conductida?"

### 6. Variable existente (04:24)

- **Acción:** Revisar variable existente de conductividad y ajustar etiqueta 'ambiental' si aplica.

- **Evidencia (transcripción):** "No, ambiental."

### 7. Relación variable-sensor (05:24)

- **Acción:** Ir a 'Variables en sensores' y crear relación nueva para sensor de suelo Wincontop.

- **Evidencia (transcripción):** "Hay que agregar unas. Hay que crear una relación nueva."

### 8. Dispositivo objetivo (06:44)

- **Acción:** Usar/duplicar dispositivo base y agregar segundo sensor (caso Soil 9).

- **Evidencia (transcripción):** "Y ese soil 9 le vamos a agregar el segundo sensor."

### 9. Duplicación práctica (08:17)

- **Acción:** Duplicar acelera, luego limpiar variables no usadas (p. ej. módem/GPS).

- **Evidencia (transcripción):** "¿Pauro...?"

### 10. Composición final (09:39)

- **Acción:** Confirmar sensores: DHT22 + suelo + batería + módem + segundo sensor.

- **Evidencia (transcripción):** "Ya, tú se va a agregar sensor o digital."

### 11. Mapeo en enlace (10:48)

- **Acción:** Validar orden de variables en el link: temperatura aire, CE suelo, temperatura suelo, humedad suelo, etc.

- **Evidencia (transcripción):** "El 2?"

### 12. Cierre operativo (11:43)

- **Acción:** Guardar, duplicar estaciones necesarias y validar telemetría/pop-up de creación.

- **Evidencia (transcripción):** "Por lo tanto, primero es temperatura de la aire."

## Reglas clave levantadas de la reunión

- Si el sensor ya existe, no recrearlo: completar asociaciones pendientes.

- La falta de conductividad suele ser problema de asociación/mapeo, no necesariamente del hardware.

- Unidad de conductividad: **µS/cm**.

- En duplicación de dispositivos, revisar variables heredadas y limpiar las no usadas.

- El orden del link debe coincidir con el orden de la tabla/variables en el sistema.

## Validación final

1. Confirmar recepción de temperatura de aire (DHT22).
2. Confirmar CE, temperatura y humedad de suelo.
3. Confirmar variables auxiliares (batería/módem) según necesidad.
4. Verificar que la estación duplicada tenga ID/link actualizado.
