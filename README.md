# Tres en Raya Pro+ - README

## Descripción del Proyecto

**Tres en Raya Pro+** es una evolución del clásico juego de tres en raya, desarrollado como parte de un trabajo académico sobre arquitectura de videojuegos.  
El proyecto demuestra cómo extender una base existente añadiendo mejoras visuales, lógica avanzada, animaciones, efectos de fin de partida y sonidos, respetando una arquitectura limpia y modular.

La arquitectura está separada en tres grandes bloques:
- **Motor genérico (`core/`)** – Reutilizable para otros juegos.
- **Componentes específicos del juego (`game/`)** – Lógica, entidades gráficas y escenas.
- **Punto de entrada y configuración** – `main.py` y `config.py`.

---

## Estructura del Proyecto

``` text
3_en_raya/
│
├── core/
│   ├── __init__.py
│   ├── entidad_base.py
│   └── escena.py
│
├── game/
│   ├── __init__.py
│   ├── entities/
│   │   ├── __init__.py
│   │   ├── tablero.py
│   │   ├── cursor.py
│   │   └── fichas.py
│   ├── logic/
│   │   ├── __init__.py
│   │   └── tres_en_raya.py
│   └── scenes/
│       ├── __init__.py
│       └── escena_juego.py
│
├── config.py
└── main.py
```


---

## Documentación de Archivos

### `core/entidad_base.py`
Define la clase `Base`, que sirve como base para todas las entidades gráficas.  
Almacena posición (`x`, `y`), escala (`e`), color y ángulo de rotación (`alfa`).  
Proporciona métodos para modificar estos atributos.  
**Permite aplicar transformaciones geométricas (rotación, escalado, traslación) esenciales para animaciones.**

### `core/escena.py`
Clase abstracta `Escena` que declara los métodos `input()`, `update()`, `render()` y `reiniciar()`.  
Toda pantalla o estado del juego debe implementar esta interfaz.  
**Garantiza un ciclo de vida uniforme (Input → Update → Render) y facilita la adición de nuevas escenas (menú, configuración, etc.).**

### `game/entities/tablero.py`
Clase `Tablero` que dibuja la cuadrícula 3×3 mediante líneas. Hereda de `Base`.  
**Mejoras visuales posibles:** marcos decorativos, bordes redondeados, colores personalizados.  
**Animaciones:** escalado progresivo para simular aparición.

### `game/entities/cursor.py`
Clase `Cursor` que gestiona la posición (fila, columna) y dibuja un rectángulo alrededor de la celda seleccionada.  
**Mejoras:** cambio de color según turno, borde doble, efecto pulsante (cambiando escala o alfa).  
**Sonidos:** se pueden agregar llamadas a sonido en los métodos de movimiento.

### `game/entities/fichas.py`
Clases `X` y `O` que dibujan sus formas (dos líneas cruzadas o un círculo) sobre un `Surface` transparente y aplican rotación.  
**Mejoras visuales:** líneas más gruesas, degradados, doble circunferencia para O.  
**Animaciones:** gracias a `self.alfa` y `self.e` se puede lograr rotación continua, crecimiento desde cero, aparición progresiva.

### `game/logic/tres_en_raya.py`
Contiene la lógica pura del juego:
- Matriz de estado (3×3 con valores VACIO, FICHA_X, FICHA_O)
- Control de turnos
- Verificación de ganador (filas, columnas, diagonales)
- Detección de empate
- Reinicio del juego

**Extensibilidad:** se puede modificar fácilmente para soportar tableros de 4×4, 5×5 o número variable de fichas para ganar. También se pueden añadir estadísticas (contadores de victorias, partidas jugadas).

### `game/scenes/escena_juego.py`
Orquesta la escena principal:
- Crea instancias del tablero, cursor, fichas de turno y la lógica.
- En `input()` procesa teclas (movimiento del cursor, colocación de ficha con ENTER).
- En `update()` maneja la animación del indicador de turno (cambio de escala).
- En `render()` dibuja todos los elementos en orden: tablero, cursor, fichas del tablero, indicadores de turno.

**Puntos de extensión:**  
- Agregar animaciones del cursor, aparición de fichas, línea ganadora parpadeante.  
- Mostrar mensajes de victoria/empate y reproducir sonidos según el resultado.  
- Cambiar colores o comportamiento mediante constantes de `config.py`.

### `config.py`
Almacena constantes globales:
- Dimensiones de pantalla (`ANCHO`, `ALTO`)
- FPS (`FPS`)
- Título de la ventana (`CAPTION`)
- Colores predefinidos (`COLOR_BLANCO`, `COLOR_ROJO`, etc.)
- Escala base (`ESCALA_BASE`)

**Permite centralizar parámetros y facilita la configuración del juego.**

### `main.py`
Punto de entrada del programa:
- Inicializa Pygame y la ventana.
- Crea una instancia de `EscenaJuego`.
- Ejecuta el **game loop** infinito:
  - Procesa eventos (cierre de ventana, teclas).
  - Llama a `input()`, `update()` y `render()` de la escena actual.
  - Controla la tasa de fotogramas.

**Sigue fielmente el patrón Input-Update-Render y no contiene lógica de negocio ni dibujo.**

---

## Relación con los Requisitos del Trabajo

| Requisito | Cómo se soporta |
|-----------|----------------|
| **Mejora de entidades gráficas** | Las clases `X`, `O`, `Tablero`, `Cursor` están aisladas y pueden rediseñarse libremente (colores, bordes, formas). |
| **Nuevas reglas / tamaños de tablero** | La lógica en `tres_en_raya.py` es independiente de Pygame; se puede extender para soportar matrices más grandes o reglas personalizadas. |
| **Animaciones** | La clase `Base` permite rotación y escala; el método `update()` de la escena puede modificar estos atributos gradualmente para lograr efectos (cursor pulsante, fichas que crecen). |
| **Efectos de fin de juego** | La escena puede consultar `hayGanador()` o `hayEmpate()` y renderizar la línea ganadora, cambiar colores, mostrar mensajes. |
| **Sonidos** | Se integran fácilmente en `input()` (por ejemplo, al mover cursor o colocar ficha) o en `update()` (al detectar fin de partida) usando `pygame.mixer`. |
| **Separación de responsabilidades** | La arquitectura impone que la lógica no dibuja, el render no contiene reglas, las entidades gráficas no administran el estado, y el game loop solo orquesta. |

---

## Instalación y Ejecución

### Requisitos
- Python 3.7 o superior
- Pygame

### Instalación de dependencias
```bash
pip install pygame
```

### Instalación de dependencias
```bash
python main.py
```

## Controles
- **Flechas (↑ ↓ ← →)** : Mover el cursor

- **ENTER** : Colocar ficha en la celda seleccionada

- **Cerrar ventana** : Salir del juego

## Próximas Mejoras (Ejemplos de Extensión)
- **Tablero dinámico**: Permitir elegir tamaño (3x3, 4x4, 5x5) y número de fichas para ganar.

- **Estadísticas**: Llevar contador de victorias de X y O, partidas jugadas.

- **Pantalla de configuración**: Seleccionar colores, volumen de sonido.

- **Más animaciones**: Rotación continua del indicador de turno, línea ganadora que parpadea.

- **Efectos de sonido**: Sonido al mover cursor, colocar ficha, ganar/empatar.