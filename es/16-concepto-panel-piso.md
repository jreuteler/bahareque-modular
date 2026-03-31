# Concepto de Panel de Piso — Viga Arco de Bambú

> **Estado: Concepto en desarrollo — no probado.** Este documento describe una propuesta de extensión del sistema BaharequeModular para luces horizontales de piso/techo. Todas las estimaciones estructurales son analíticas y requieren validación en laboratorio. Contribuciones, críticas y ofertas de ensayos son bienvenidas.

## El Objetivo

Extender BaharequeModular de un sistema de muros a un **sistema constructivo completo** — muros, pisos y techos desde la misma línea de producción, mismos materiales, mismas habilidades. Sin losa de concreto. Sin vigas de acero. Sin refuerzo de acero.

## El Problema

Un panel de muro estándar de 85 mm falla cuando se coloca horizontalmente para cubrir luces de 4–5 m como piso. El mortero se fisura en tracción en la cara inferior — el panel fue diseñado para compresión (muros), no para flexión (pisos).

## La Solución: Viga Arco de Bambú (Bowstring Beam)

Un solo marco de perfil T (la misma pieza usada en paneles de muro) con un mecanismo de **arco atirantado** interior:

- **Arco de bambú en compresión** — tiras forzadas en una curva parabólica por piezas transversales perpendiculares graduadas sobre el alma del perfil T
- **Tirante de bambú en tracción** — 26 tiras (30 × 35 mm) sujetadas con tornillos en una sola capa en el ala inferior del perfil T
- **Mortero** rellena y estabiliza todo
- **Cero acero en la luz** — acero solo en el marco perimetral del perfil T para conexiones

![Vista lateral del panel de piso](svg/floor-panel-side.svg)

Cada material hace lo que mejor sabe hacer:

| Material | Función | Resistencia utilizada |
|----------|---------|----------------------|
| Arco de bambú | Compresión | 45 MPa (solo 20–31% utilizado) |
| Tirante de bambú | Tracción | 25 MPa al 30% de utilización |
| Piezas transversales | Control geométrico | Fuerzan el arco en forma parabólica |
| Mortero | Relleno + estabilidad | Zona de compresión sobre el arco |
| Marco de perfil T | Conexión perimetral | Corte en apoyos, conexión a muros |

![Vista superior del panel de piso](svg/floor-panel-top.svg)

## Cómo Funciona

Una viga arco (arco atirantado) convierte la carga vertical del piso en empuje horizontal. El arco lleva este empuje en compresión. El tirante lo resiste en tracción. Los dos están en equilibrio — el mortero rellena entre ellos, proporcionando estabilidad y distribuyendo cargas locales.

## Especificaciones (panel de 180 mm, recomendado)

| Propiedad | Valor |
|-----------|-------|
| Dimensiones del panel | 1,0 m ancho × 4,0 o 5,0 m de luz |
| Profundidad total | 180 mm |
| Marco de perfil T | Estándar 30×30×3 mm, alma de 85 mm — un solo marco en la parte inferior |
| Arco de bambú | 27 tiras × 20×20 mm × 2 capas, forzado en parábola |
| Piezas transversales | Bambú de 30×30 mm, graduadas de 0→40 mm |
| Tirante de bambú | 26 tiras × 30×35 mm, una sola capa, sujetadas con tornillos |
| Flecha del arco | 127 mm (tirante a corona) |
| Peso | ~325 kg/m² |

## Rendimiento Estructural

| Luz | Empuje | Ratio arco | Ratio tirante | Deflexión | Estado |
|-----|--------|-----------|---------------|-----------|--------|
| 4,0 m | 121 kN | 0,31 (69% reserva) | 0,92 (8% reserva) | 2,2 mm / 13,3 límite | OK |
| 5,0 m | 189 kN | 0,49 (51% reserva) | 0,98 (2% reserva) | 5,0 mm / 16,7 límite | OK |

Carga de piso: 4,5 kN/m² (muerta 2,5 + viva 2,0, según NSR-10 residencial). Peso propio incluido.

## Lo Que es Nuevo

Búsqueda exhaustiva de literatura académica, patentes y proyectos construidos no encontró **ningún sistema existente** que combine:

1. Arco de bambú en compresión dentro de un elemento de piso
2. Tirante de bambú en tracción en la parte inferior
3. Mecanismo de arco atirantado (bowstring)
4. Encapsulamiento en mortero

Cada principio está bien establecido individualmente. La combinación es nueva. Coincidencias más cercanas:

| Trabajo existente | Qué falta |
|-------------------|-----------|
| Viga T de bambú laminado curvo-concreto (2023) | Sin tirante de tracción, bambú laminado no tiras |
| Concreto reforzado con bambú (Ghavami, 1979+) | Siempre refuerzo recto, nunca en arco |
| Cerchas bowstring (acero/madera) | Nunca en bambú, nunca encapsuladas en mortero |
| Paneles de ferrocemento con bambú (India) | Planos, luces cortas, sin arco |

## Lo Que Necesita Pruebas

1. **¿Se desarrolla la acción de arco atirantado?** — Cargar un panel de prueba, medir el empuje horizontal en los apoyos
2. **¿Se mantiene el arco forzado bajo carga?** — ¿Las piezas transversales mantienen la geometría del arco?
3. **Tracción del tirante de bambú** — ¿El paquete de 30×35 mm sujetado mantiene su capacidad bajo el empuje del arco?
4. **Acción compuesta** — ¿Se mantiene la adherencia mortero-bambú en el arco bajo compresión?
5. **Sonido de impacto** — Medir IIC con y sin fibra de pasto estrella
6. **Conexión** — Probar el sistema de pernos de longitud extra (unión muro-piso-muro con triple ala)

Un solo ensayo de flexión (simplemente apoyado, carga uniforme) responde las preguntas 1–4 en una tarde.

## Implicaciones

Si se valida, este panel de piso convierte a BaharequeModular en un **sistema constructivo completo**:

- **Muros** — panel estándar de 85 mm
- **Pisos/techos** — panel bowstring de 180 mm
- **Conexiones** — alas de perfil T empernadas en cada unión
- **Electricidad** — integrada en todos los paneles
- **Plomería** — integrada en paneles de piso y muro
- **Acabado de techo** — pañete de cal en la cara inferior del panel de piso

Un sistema de paneles. Una línea de producción. Un conjunto de habilidades. Cero acero en cualquier luz — bambú y mortero llevan todo. Acero solo en los bordes para conexiones.

**Una viga arco de bambú fundida en mortero. Aún no existe. Queremos construirla y probarla.**
