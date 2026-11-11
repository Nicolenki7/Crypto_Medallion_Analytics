# Plan de ejecucion

## Estado actual
- Pipeline medallion en Fabric (PySpark) + Power BI.
- `LICENSE`, `requirements.txt` y `.gitignore` anadidos.

## Problema detectado
- `data/crypto_historical_365days.csv` esta **vacio** (2 bytes).
- `crypto_yearly_performance - copia.csv` y `crypto_monthly_summary - copia.csv` son duplicados con nombre no canonico.

## Proximos pasos
1. Regenerar el historico de 365 dias desde el pipeline y versionarlo con nombre definitivo.
2. Eliminar los sufijos `- copia` y el archivo vacio.
3. Script unico `src/run_pipeline.py` que reconstruya bronze -> silver -> gold.
4. CI de contrato de datos (mismo test que los otros repos).

## Criterio de aceptacion
- Ningun CSV vacio ni duplicado en el repo; el informe se regenera desde datos reales.

## Riesgos
- Los precios de cripto dependen de la fuente: fijar snapshot y fecha de corte.
