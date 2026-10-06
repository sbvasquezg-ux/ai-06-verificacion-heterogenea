# Verificación formal parcial

`MainTheorems.lean` comprueba cinco consecuencias algebraicas sobre números reales: oferta con renta cero, expansión del costo lineal, pendiente a renta cero, efecto de un costo no negativo y equivalencia entre brecha positiva y beneficio de entrada positivo.

No contiene `sorry` ni axiomas económicos nuevos. Usa Mathlib y los axiomas fundacionales que Lean informa en `BUILD_OUTPUT.txt`. La FOC es una hipótesis en el lema de pendiente: Lean no demuestra aquí la diferenciación, existencia de un máximo, beneficio cero, cómputo ocioso ni equilibrio general.

## Reproducir

Con elan y acceso a Internet, desde esta carpeta:

```sh
lake update
lake exe cache get
lake env lean MainTheorems.lean
```

La comprobación local utilizó Lean 4.30.0-rc2 y Mathlib en la revisión fijada en `lakefile.toml`, mediante un entorno local con dependencias ya descargadas. `BUILD_OUTPUT.txt` registra el resultado real de comprobar este archivo. No se afirma haber probado una instalación limpia desde cero.
