"""Crypto: retornos reales del periodo, sin dejar que la media mienta.

Datos: data/crypto_yearly_performance - copia.csv (100 monedas con precio
inicial, final y retorno total). El histórico de 365 días del repo está vacío,
así que no se usa: la primera comprobación lo deja dicho.

Uso: python src/crypto_charts.py
"""
import pathlib
import sys

import pandas as pd

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from svg_chart import AZUL, ROJO, barras

ROOT = pathlib.Path(__file__).resolve().parents[1]
RAW = ROOT / "data" / "crypto_yearly_performance - copia.csv"
HIST = ROOT / "data" / "crypto_historical_365days.csv"
IMG, OUT = ROOT / "docs" / "img", ROOT / "outputs"
IMG.mkdir(parents=True, exist_ok=True)
OUT.mkdir(parents=True, exist_ok=True)

# 1) el archivo que el repo documenta como vacío
if HIST.exists():
    print(f"1. {HIST.name}: {HIST.stat().st_size} bytes "
          f"-> {'vacío, no se usa' if HIST.stat().st_size < 50 else 'con datos'}")
else:
    print(f"1. {HIST.name}: no está en el repositorio")

d = pd.read_csv(RAW)
r = d["total_return"]
print(f"2. {len(d)} monedas · mediana {r.median():,.1f}% · media {r.mean():,.1f}%")
print(f"   positivas {int((r > 0).sum())} ({(r > 0).mean():.1%}) · "
      f"negativas {int((r < 0).sum())} · planas {int((r == 0).sum())}")

top = d.nlargest(8, "total_return")[::-1]
print("\n3. mejores retornos:")
print(top[["coin_name", "total_return"]].to_string(index=False))
barras(
    [(n, v, ROJO if v > 300 else AZUL) for n, v in zip(top["coin_name"], top["total_return"])],
    "Una moneda multiplica por 22 y rompe la escala",
    IMG / "crypto-top.svg",
    subtitulo=f"retorno total del periodo (%) · {len(d)} monedas analizadas",
    formato="{:,.0f}", sufijo="%")

bins = [-100, 0, 50, 150, 300, 10000]
etiquetas = ["pérdida", "0-50 %", "50-150 %", "150-300 %", ">300 %"]
cuenta = pd.cut(r, bins, labels=etiquetas).value_counts().reindex(etiquetas)
print("\n4. distribución de retornos:")
print(cuenta.to_string())
barras(
    [(e, int(v), ROJO if e == "pérdida" else AZUL) for e, v in cuenta.items()],
    "Siete de cada diez monedas cerraron en pérdidas",
    IMG / "crypto-distribucion.svg",
    subtitulo="número de monedas por rango de retorno en el periodo",
    formato="{:,.0f}")

barras(
    [("mediana", r.median(), ROJO), ("media", r.mean(), AZUL)],
    "La media no representa a casi nadie",
    IMG / "crypto-media-mediana.svg",
    subtitulo="retorno típico frente al retorno medio (%) · la diferencia la causa el valor extremo",
    formato="{:+,.1f}", sufijo="%")

d.sort_values("total_return", ascending=False).to_csv(OUT / "crypto_returns_ranked.csv", index=False)
print(f"\n5. peor: {d.nsmallest(1, 'total_return').iloc[0]['coin_name']} "
      f"({r.min():,.1f}%) · mejor: {d.nlargest(1, 'total_return').iloc[0]['coin_name']} "
      f"({r.max():,.1f}%)")
