# Prevención de Corrosión

## Filosofía de Diseño

El sistema de paneles usa múltiples materiales en contacto íntimo. Cada interfaz de materiales es un riesgo potencial de corrosión. Este capítulo documenta el análisis galvánico de cada interfaz y la estrategia de prevención.

**Meta de diseño: 80–100 años sin falla estructural por corrosión.**

## Serie Galvánica (metales relevantes)

De anódico (se corroe primero) a catódico (protegido):

1. Zinc (recubrimiento de galvanizado)
2. Aluminio (malla contra insectos)
3. Acero dulce (marco, tiras de sujeción)
4. Acero inoxidable (tornillos)

Cuando dos metales están en contacto eléctrico en presencia de un electrolito (humedad), el metal más anódico se corroe preferencialmente. Esta es la base de la corrosión galvánica.

## Análisis de Interfaces

### 1. Marco de Acero ↔ Mortero

- **Contacto:** Directo — el mortero se vierte sobre y alrededor del marco de acero galvanizado
- **Nivel de riesgo:** BAJO
- **Análisis:** El ambiente alcalino del mortero de cemento (pH 12–13) pasiva el recubrimiento de zinc, formando una capa estable de óxido de zinc. Esta es de hecho una combinación *beneficiosa* — el mortero protege el zinc, y el zinc protege el acero. Mismo principio que la varilla corrugada en concreto reforzado.
- **La adición puzolánica** reduce gradualmente el pH del mortero a 10–11 con las décadas. Esto permanece bien dentro del rango de pasivación para el zinc.
- **Prevención:** Galvanizado en caliente según ISO 1461 (mínimo 85 μm). No se necesitan medidas adicionales.

### 2. Tornillos de Acero Inoxidable ↔ Marco Galvanizado

- **Contacto:** Directo — los tornillos pasan a través del alma galvanizada
- **Nivel de riesgo:** BAJO-MEDIO
- **Análisis:** El acero inoxidable es catódico respecto al zinc. En teoría, esto genera corrosión acelerada del zinc en el punto de contacto. En la práctica, el encapsulamiento en mortero elimina la humedad continua (el electrolito), y el recubrimiento de zinc en el agujero del tornillo es un área sacrificial — el zinc circundante lo protege catódicamente.
- **Prevención:** Usar tornillos de acero inoxidable A2 (304). La cabeza del tornillo queda cubierta por la tira de sujeción y el mortero. Sin vía de humedad.

### 3. Malla de Gallinero ↔ Marco de Acero

- **Contacto:** Indirecto — la malla de gallinero se grapa sobre la cara de mortero, separada del marco por 30+ mm de mortero
- **Nivel de riesgo:** NINGUNO
- **Análisis:** Ambos son acero galvanizado. No hay diferencia de potencial galvánico. Separados por capa de mortero. Sin problema.

### 4. Malla de Aluminio ↔ Marco de Acero

- **Contacto:** Indirecto — la malla de aluminio se ubica entre la malla de gallinero y el mortero, separada del marco por 30+ mm
- **Nivel de riesgo:** NINGUNO
- **Análisis:** El aluminio es anódico respecto al acero (se correría primero en contacto directo). Pero no hay contacto directo metal-metal — la capa de mortero proporciona aislamiento eléctrico completo.
- **Prevención:** Asegurar que la malla de aluminio no toque directamente el marco de acero durante la instalación. La capa de mortero maneja esto naturalmente.

### 5. Malla de Aluminio ↔ Malla de Gallinero (Acero Galvanizado)

- **Contacto:** Directo — las capas de malla se tocan durante la instalación
- **Nivel de riesgo:** BAJO
- **Análisis:** Existe algo de potencial galvánico. Pero ambas quedan embebidas en mortero después de la instalación, eliminando la vía de humedad. La malla de aluminio es una capa delgada sacrificial — incluso si ocurre algo de corrosión en los puntos de contacto, la malla de gallinero estructural permanece intacta.
- **Prevención:** No se requiere acción. El encapsulamiento en mortero es suficiente.

### 6. Tira de Sujeción ↔ Alma del Marco

- **Contacto:** Directo — la tira de sujeción se emperna contra el alma a través de las tiras de bambú
- **Nivel de riesgo:** NINGUNO
- **Análisis:** Ambos son acero dulce galvanizado en caliente. Mismo material, mismo recubrimiento. Sin potencial galvánico.

### 7. Marco de Acero ↔ Tiras de Bambú

- **Contacto:** Directo — las tiras de bambú descansan contra el alma galvanizada
- **Nivel de riesgo:** BAJO
- **Análisis:** El bambú no es un metal — no es posible la corrosión galvánica. La preocupación es que la humedad que absorbe el bambú cree una zona húmeda persistente sobre el acero. El encapsulamiento en mortero elimina esto sellando la interfaz. El tratamiento con borato también reduce la absorción de humedad.

## Factores Ambientales

### Ambientes Costeros (< 1 km del mar)

El aire cargado de sal acelera dramáticamente el consumo de zinc. En ambientes costeros:
- Aumentar el espesor de galvanizado a 120+ μm
- Usar tornillos de acero inoxidable 316L (en vez de 304)
- Considerar recubrimiento adicional de epóxico sobre el marco antes del galvanizado
- Vida útil esperada del marco en zona costera: 40–60 años (vs 80–100 tierra adentro)

### Alta Pluviosidad (> 2.000 mm/año)

- Asegurar alero de techo adecuado (mínimo 1,5 m) para mantener la lluvia fuera de las superficies del muro
- El pañete de cal actúa como capa sacrificial — renovar cada 10–15 años en zonas de alta pluviosidad
- El interior del muro (encapsulado en mortero) no se ve afectado por la lluvia

### Humedad Tropical

- La transpirabilidad del pañete de cal es crítica — permite que la humedad pase a través en vez de atraparla
- NO selle el muro con pintura o recubrimiento impermeable — esto atrapa la humedad y acelera la degradación
- El muro debe respirar: solo lechada de cal

## Resumen

| Interfaz | Riesgo | Prevención | Mantenimiento |
|----------|--------|------------|---------------|
| Marco de acero en mortero | Bajo | Galvanizado en caliente | Ninguno (inspeccionar a los 40 años) |
| Tornillos inox. en marco galv. | Bajo-Medio | Inoxidable A2, encapsulamiento en mortero | Ninguno |
| Malla de gallinero a marco | Ninguno | Mismo material, separación por mortero | Ninguno |
| Malla de aluminio a marco | Ninguno | Aislamiento por mortero | Ninguno |
| Malla de aluminio a malla de gallinero | Bajo | Encapsulamiento en mortero | Ninguno |
| Tira de sujeción a marco | Ninguno | Mismo material | Ninguno |
| Acero a bambú | Bajo | Tratamiento con borato, encapsulamiento en mortero | Ninguno |

**La protección contra la corrosión del sistema se basa en tres capas: galvanizado (primaria), encapsulamiento en mortero (secundaria) y pañete de cal (terciaria/sacrificial). La falla de cualquier capa individual no compromete el sistema.**
