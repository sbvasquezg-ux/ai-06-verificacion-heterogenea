# Extensión: costos de verificación heterogéneos

## 1. Pregunta y contribución

La Proposición 6 de Ide y Talamàs caracteriza la IA no autónoma bajo los supuestos del artículo. La extensión pregunta por la robustez de la selección de usuarios cuando la validación exige recursos y esos recursos dependen del conocimiento. La contribución prevista es identificar condiciones para conservar o alterar el patrón de adopción. La selección intermedia es una hipótesis de equilibrio, no un teorema demostrado en este avance.

## 2. Entorno y unidad del costo

Hay masa uno de humanos con conocimiento observable y fijo $z\in[0,1]$ y distribución $G$. La capacidad de IA es $a\in(0,1)$; se considera como asesora de trabajadores $z\leq a$. Se mantienen los supuestos de la referencia, incluido $h<h_0(G)$. Para la ilustración uniforme se usa $h=0.5<0.75$.

El costo $c(z)\geq0$, $c'(z)\leq0$, es un gasto real por trabajador y período, en unidades del bien final, que paga la firma. Representa validación y documentación obligatorias. No consume tiempo adicional del trabajador o asesor y no modifica la probabilidad de éxito. Modelar verificación como tiempo, errores o esfuerzo endógeno requeriría otra tecnología.

Con $c(z)=\kappa(1-z)$, $\kappa\geq0$, el conocimiento ahorra recursos de validación. Comparar con costo constante permite separar nivel y heterogeneidad. El producto bruto por trabajador es $a$; el neto es $a-c(z)$.

## 3. Firma y FOC

El asesor atiende a $n(z)$ trabajadores y su restricción de tiempo implica

$$hn(z)(1-z)=1,\qquad n(z)=\frac1{h(1-z)},\qquad n'(z)=\frac1{h(1-z)^2}.$$

La firma elige el tipo contratado, no la educación de una persona, tomando como dados el salario por tipo y la renta del cómputo:

$$\max_{z\in[0,a]}\Pi^V(z)=n(z)[a-w^V(z)-c(z)]-r.$$

Bajo diferenciabilidad y para un óptimo interior,

$$\Pi^{V\prime}(z)=n'(z)[a-w^V(z)-c(z)]-n(z)[w^{V\prime}(z)+c'(z)]=0.$$

Como $n'/n=1/(1-z)$,

$$w^{V\prime}(z)+c'(z)=\frac{a-w^V(z)-c(z)}{1-z}.$$

Beneficio cero en una firma activa implica $a-w^V-c=r/n=rh(1-z)$. Sustituyendo:

$$\boxed{w^{V\prime}(z)+c'(z)=hr.}$$

Con masa humana uno, cada usuario requiere a lo sumo $h$ unidades de asesoría; $\mu>h$ es una condición suficiente de cómputo ocioso en este régimen. Por complementariedad $r=0$. Así, para firmas activas con IA:

$$w^V(z)=a-c(z),\qquad w^{V\prime}(z)=-c'(z)=\kappa.$$

No es una ecuación para identificar un tipo único: el salario competitivo se ajusta. Tampoco describe salarios de quienes no usan IA.

## 4. Bordes y segunda derivada

En $z=0$ se requiere $\Pi'(0)\leq0$; en $z=a$, $\Pi'(a)\geq0$, con derivadas unilaterales. En un punto interior estacionario, usando la FOC y la forma de $n$, se obtiene $\Pi''=-n(w''+c'')$. La condición necesaria es $w''+c''\geq0$. No asegura suficiencia global; en tramos de beneficio cero puede haber indiferencia. En quiebres salariales se deben usar variaciones unilaterales.

## 5. Diagnóstico de entrada a salarios anteriores a IA

Sea $w^0(z)$ el salario de equilibrio anterior a IA. Para $r=0$:

$$\Delta^0(z)=a-c(z)-w^0(z),\qquad \Delta^{0\prime}(z)=-c'(z)-w^{0\prime}(z).$$

Con costo lineal, $\Delta^{0\prime}=\kappa-w^{0\prime}$. Un costo que disminuye con rapidez puede hacer crecer inicialmente la rentabilidad de entrada. El ejemplo uniforme usa $h=.5$, $a=.88$, $\kappa=.53$:

| $z$ | $w^0$ | $a-c$ | $\Delta^0$ |
|---|---:|---:|---:|
| 0 | .357044 | .350000 | −.007044 |
| .25 | .474391 | .482500 | .008109 |
| .60 | .691177 | .668000 | −.023177 |

El intervalo de entrada rentable en este ejemplo es aproximadamente $(.066081,.426366)$. Se calcula con salarios fijos de referencia. No es el conjunto de usuarios del equilibrio con IA y no demuestra pérdidas salariales en la base. Parámetros ilustrativos, sin calibración empírica.

## 6. Cierre de equilibrio pendiente

Para cómputo abundante, las restricciones de ausencia de beneficios incluyen

$$w(z)\geq z,$$
$$w(z)\geq a-c(z)\quad(z\leq a),$$
$$w(z)+h(1-z)w(s)\geq s\quad(z\leq s).$$

Debe haber igualdad en actividades utilizadas, vaciado de mercados humanos por tipo y factibilidad y complementariedad del cómputo. Las desigualdades solas no bastan. El plan es discretizar tipos, resolver la asignación con recursos humanos y cómputo, recuperar salarios duales, verificar residuos y robustez al tamaño de malla.

Comparaciones: (i) $c=0$; (ii) $c=\bar c$; (iii) $c=\kappa(1-z)$ con nivel comparable. Medir usuarios directos, salarios de todos los tipos y producto neto. La posible no monotonía debe verificarse tras el ajuste general de salarios.

## 7. Qué está demostrado y qué no

La FOC se deriva analíticamente bajo sus condiciones; las consecuencias algebraicas básicas se verifican en Lean. El código reproduce el diagnóstico de entrada y verifica la derivada numéricamente. No se ha demostrado existencia, unicidad, selección intermedia en equilibrio ni efecto distributivo. El [artículo original](https://arxiv.org/html/2312.05481v11) fundamenta el entorno; la fricción y sus preguntas son propias de esta propuesta.
