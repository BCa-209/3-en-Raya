# Trabajo 01: Evolución de una Arquitectura de Videojuegos -- Tres en Raya Pro+

## 1. Introducción 

Durante las sesiones anteriores se construyó una arquitectura básica de videojuegos basada en los siguientes conceptos:

- Entidades gráficas
- Entidades lógicas
- Estado del juego
- Escenas
- Input
- Update
- Render
- Game Loop 

El objetivo de este trabajo no es crear un nuevo videojuego desde cero. 

El  objetivo  consiste  en  evolucionar  y  mejorar  la  arquitectura desarrollada en clase, agregando nuevas características visuales y funcionales que permitan transformar el Tres en Raya original en una versión más completa denominada **Tres en Raya Pro+**. 
Durante el desarrollo deberán respetar la arquitectura presentada en clase, manteniendo la separación entre lógica, representación gráfica y control del juego

## 2. Mejora de Entidades Gráficas

Deben mejorar Las entidades gráficas desarrolladas en clase:

- X
- O
- Tablero
- Cursor

El objetivo es lograr una apariencia visual más atractiva y profesional.

### Ejemplos de lo que pueden hacer

Los siguientes ejemplos son únicamente sugerencias. Se espera que cada grupo proponga nuevas ideas y mejoras propias.

#### Ficha X
- Cambiar el diseño de las líneas.
- Utilizar varios colores.
- Agregar bordes.
- Crear una X más estilizada.

#### Ficha O
- Agregar doble circunferencia.
- Utilizar colores degradados simulados.
- Agregar detalles decorativos.

#### Tablero
- Cambiar colores.
- Agregar marcos.
- Agregar efectos visuales.
- Personalizar el diseño.

#### Cursor
- Cambiar el color según el jugador.
- Crear un borde más atractivo.
- Agregar efectos visuales.

#### Conceptos que reforzarán
- Primitivas gráficas.
- Transformaciones geométricas.
- Render.
- Diseño visual.
- Creatividad aplicada al desarrollo de videojuegos.

## 3. Mejora de Entidades Lógicas

### Deben mejorar
La lógica implementada en la clase: **TresEnRaya** El objetivo es agregar nuevas funcionalidades y reglas que permitan convertir el juego original en una versión más interesante.

### Ejemplos de lo que pueden hacer
Los siguientes ejemplos son únicamente referencias.

#### Nuevos tamaños de tablero
- 4 × 4
- 5 × 5
- Tamaños configurables

#### Nuevas reglas
- Número variable de fichas para ganar.
- Restricciones especiales.
- Modos de juego personalizados.

#### Estadísticas
- Contador de partidas.
- Contador de victorias.
- Historial de resultados.

#### Configuración
- Selección de colores.
- Selección del tamaño del tablero.

#### Conceptos que reforzarán
- Estado del juego.
- Matrices.
- Algoritmos.
- Programación orientada a objetos.
- Lógica de videojuegos.

## 4. Animaciones
### Deben mejorar
Las animaciones existentes e incorporar nuevas animaciones que hagan más agradable la experiencia del usuario.

### Ejemplos de lo que pueden hacer
Los siguientes ejemplos son únicamente sugerencias.

#### Cursor
- Efecto pulsante.
- Cambio gradual de tamaño.
- Cambio gradual de color.

#### Fichas 
- Aparición progresiva. 
- Crecimiento desde tamaño cero. 
- Rotación.
- Movimiento suave. 

#### Tablero 
- Aparición inicial animada. 
- Efectos de entrada. 

#### Indicadores de turno 
- Rotación continua. 
- Cambio de escala. 
- Efectos visuales dinámicos.

#### Conceptos que reforzarán 
- Update. 
- Tiempo. 
- Animación. 
- Transformaciones geométricas. 
- Estados dinámicos.

## 5. Efectos de Fin de Juego 
Deben mejorar La experiencia visual y funcional cuando ocurre una victoria o empate.

### Ejemplos de lo que pueden hacer
Los siguientes ejemplos son únicamente referencias. 

#### Victoria 
- Resaltar la línea ganadora. 
- Parpadeo de fichas ganadoras. 
- Cambio de color. 
- Animación de celebración. 

#### Empate 
- Mensaje especial. 
- Animación de empate. 
- Efectos visuales. 

#### Mensajes 
- Mostrar ganador. 
- Mostrar puntaje. 
- Mostrar estadísticas.

#### Conceptos que reforzarán 
- Estados del juego. 
- Eventos. 
- Render. 
- Comunicación visual con el usuario.

## 6. Sonidos 
### Deben mejorar 
La experiencia de usuario incorporando retroalimentación auditiva.

### Ejemplos de lo que pueden hacer 
Los siguientes ejemplos son únicamente referencias.

#### Durante el juego 
- Sonido al mover el cursor. 
- Sonido al colocar una ficha. 

#### Final de partida 
- Sonido de victoria. 
- Sonido de derrota. 
- Sonido de empate. 

#### Interacciones 
- Sonidos de selección. 
- Sonidos de confirmación.

#### Conceptos que reforzarán 
- Multimedia. 
- Eventos. 
- Retroalimentación. 
- Experiencia de usuario.

## 7. Recomendaciones Generales 
Durante el desarrollo del proyecto deberán respetar la arquitectura trabajada en clase. 
Eviten mezclar responsabilidades. 

### Por ejemplo: 
- La lógica no debe dibujar. 
- El render no debe contener reglas del juego. 
- Las entidades gráficas no deben administrar el estado. 
- El Game Loop debe continuar organizando Input, Update y Render.

### Entregable 
Cada grupo deberá presentar: 
- Código fuente completo. 
- Explicación de las mejoras implementadas. 
- Demostración funcional del videojuego. 
- Justificación de las decisiones tomadas.

## 8. Reflexión Final
El objetivo de este trabajo no es únicamente mejorar un **Tres en Raya**. El verdadero objetivo consiste en comprender cómo evoluciona una arquitectura de videojuegos.

En la industria del software rara vez se comienza desde cero. Lo más común es recibir un sistema existente, comprender su arquitectura y extenderla agregando nuevas funcionalidades. Por ello, este proyecto representa una experiencia cercana a una situación real de desarrollo.

Lo más valioso de todo el proceso realizado en clase es que se construyó una arquitectura completa a partir de conceptos simples como líneas, círculos y rectángulos.

A partir de esas primitivas surgieron entidades, estados, lógica, escenas, animaciones y finalmente un videojuego funcional. El siguiente desafío consistirá en reutilizar esta arquitectura para construir un nuevo videojuego: Conecta 4 

En ese momento descubrirán que el verdadero aprendizaje no estaba en
el Tres en Raya, sino en la arquitectura que construyeron para hacerlo
posible.
