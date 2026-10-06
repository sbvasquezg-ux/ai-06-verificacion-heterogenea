![Verificación heterogénea](assets/header.svg)

# Verificación heterogénea y acceso a la IA

**Extensión formal en desarrollo de Ide y Talamàs (2025), _Artificial Intelligence in the Knowledge Economy_.** Autora: Belén Vásquez. Primer avance: pregunta, mecanismo, problema de la firma y condiciones de primer orden.

¿Puede un costo de verificación decreciente con el conocimiento cambiar qué trabajadores usan una IA no autónoma? La hipótesis es que la ventaja de validar respuestas puede desplazar la oportunidad de entrada hacia tipos intermedios. El equilibrio y sus consecuencias distributivas siguen abiertos.

## Entregables

| Material | Archivo |
|---|---|
| Avance de dos páginas | [PDF](paper/avance.pdf) · [Word editable](paper/avance.docx) |
| Exposición de 20 minutos | [PDF](presentation.pdf) · [PowerPoint editable](presentation.pptx) |
| Explicación paso a paso | [Guía de estudio](extra/guia_estudio.pdf) |
| Guion y tiempos | [Notas](extra/notes.md) |
| Desarrollo formal | [Modelo y FOC](extensions.md) |
| Simulación ilustrativa | [Código](sim.py) · [Resultados](extra/results/example.json) |
| Verificación algebraica | [Lean y alcance](lean/README.md) |

La presentación tiene 12 diapositivas centrales (20 minutos) y tres de apoyo. Word y PowerPoint son las fuentes editables de los PDF entregados. `presentation.tex` es una versión alternativa de contenido en Beamer; no fue la fuente de ese PDF.

## Modificación del modelo

La firma paga un costo real obligatorio $c(z)\geq0$ por trabajador y período, medido en unidades del bien final. La especificación inicial es $c(z)=\kappa(1-z)$. Este costo no añade tiempo de consulta ni introduce errores de la IA: se conserva $n(z)=1/[h(1-z)]$.

```math
\max_{0\leq z\leq a}\;\Pi^V(z)=n(z)[a-w^V(z)-c(z)]-r.
```

Para un óptimo interior diferenciable, la FOC es

```math
n'(z)[a-w^V(z)-c(z)]-n(z)[w^{V\prime}(z)+c'(z)]=0.
```

Con beneficio cero se obtiene $w^{V\prime}(z)+c'(z)=hr$. Si el cómputo es abundante y $r=0$, las firmas activas con IA pagan $w^V(z)=a-c(z)$; para el costo lineal, la pendiente de ese tramo es $\kappa$. **Estas identidades locales no determinan por sí solas quién utiliza IA en equilibrio.**

## Reproducción

Python 3.10 o superior; el cálculo y las pruebas usan la biblioteca estándar:

```sh
python3 -m unittest discover -s tests -v
python3 sim.py
```

Para regenerar las figuras (PDF y SVG):

```sh
python3 -m pip install -r requirements.txt
python3 scripts/plot_example.py
```

El ejemplo usa distribución uniforme, $h=0.5$, $a=0.88$ y $\kappa=0.53$. Compara la oferta neta de IA con salarios **anteriores a IA**. Es una oportunidad de entrada a precios dados, no una solución del nuevo equilibrio ni una estimación empírica.

## Estructura y estado

- `paper/`: avance y referencia bibliográfica.
- `presentation.*`, `assets/`: exposición y estilo.
- `extra/`: guía, guion, figuras y resultados reproducibles.
- `sim.py`, `tests/`, `scripts/`: ejemplo, verificaciones y gráficos.
- `hand/`: hoja para desarrollar la FOC a mano; evidencia manuscrita pendiente.
- `lean/`: consecuencias algebraicas comprobadas; formalización económica parcial.
- `extensions.md`, `prompts.md`: desarrollo y trazabilidad.

Se conserva la organización del [repositorio de referencia](https://github.com/sbvasquezg-ux/ai-05-ide), adaptando el contenido al nuevo tema. No se presentan fotografías, auditorías o demostraciones del trabajo anterior como evidencia de esta extensión.

El siguiente paso es resolver conjuntamente asignación, salarios y vaciado de mercados; comparar costo cero, constante y heterogéneo; y comprobar si la selección intermedia sobrevive al ajuste de salarios.

## Referencias

Ide, E. y Talamàs, E. (2025). _Artificial Intelligence in the Knowledge Economy_. Journal of Political Economy, 133(12), 3762–3800. [DOI](https://doi.org/10.1086/737233). Versión utilizada: [arXiv:2312.05481v11](https://arxiv.org/html/2312.05481v11), §§3 y 6, Proposición 6.

La estructura y el ejemplo uniforme se apoyan en `ai-05-ide`, revisión `6604860bd611b7fc9c95bc13492fe16cded6fe56`. Las propuestas y las limitaciones de esta extensión se distinguen en [extensions.md](extensions.md). Licencia MIT para el material propio; el artículo citado conserva sus derechos.
