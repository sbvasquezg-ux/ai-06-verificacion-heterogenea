"""Generate standalone scientific figure from the numerical CSV."""
from pathlib import Path
import csv
from reportlab.graphics.shapes import Drawing, String, Line
from reportlab.graphics.charts.lineplots import LinePlot
from reportlab.graphics import renderPDF, renderSVG
from reportlab.lib import colors
ROOT=Path(__file__).resolve().parents[1]
rows=list(csv.DictReader((ROOT/'extra/results/entry_grid.csv').open()))
d=Drawing(720,440)
d.add(String(55,409,'Entrada a salarios anteriores a IA',fontSize=20,fillColor=colors.HexColor('#102d3c')))
d.add(String(55,387,'h = 0.50 | a = 0.88 | kappa = 0.53 | ejemplo ilustrativo',fontSize=11))
p=LinePlot();p.x=65;p.y=80;p.width=595;p.height=280
keys=['baseline_wage','zero_cost_offer','constant_cost_offer','heterogeneous_offer']
p.data=[[(float(r['z']),float(r[k])) for r in rows] for k in keys]
p.xValueAxis.valueMin=0;p.xValueAxis.valueMax=.88;p.yValueAxis.valueMin=.3;p.yValueAxis.valueMax=1.15
palette=['#102d3c','#7e8b95','#d48b36','#008777']
for i,col in enumerate(palette):p.lines[i].strokeColor=colors.HexColor(col);p.lines[i].strokeWidth=1.8
p.lines[1].strokeDashArray=[4,3];p.lines[2].strokeDashArray=[2,3]
d.add(p)
for i,label in enumerate(['Salario base','IA sin costo','Costo constante','Costo heterogeneo']):
 x=55+i*165;d.add(Line(x,38,x+20,38,strokeColor=colors.HexColor(palette[i]),strokeWidth=2));d.add(String(x+25,34,label,fontSize=9))
d.add(String(310,55,'Conocimiento z',fontSize=10))
d.add(String(55,13,'Entrada rentable cuando la oferta supera al salario base. No es el nuevo equilibrio.',fontSize=10))
folder=ROOT/'extra/figures';folder.mkdir(exist_ok=True)
renderPDF.drawToFile(d,str(folder/'entry.pdf'));renderSVG.drawToFile(d,str(folder/'entry.svg'))
