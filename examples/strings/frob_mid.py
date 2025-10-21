import sys
from cdiagram import StringDiagram
from jinja2 import Template,FileSystemLoader,Environment

env=Environment(loader=FileSystemLoader('.'),
    line_statement_prefix='%%',variable_start_string='<<',variable_end_string='>>')
t=env.get_template('stringdiags.tex')

d1=StringDiagram() 
d1.add_bottom_node('B1',(0,0)) 
d1.add_bottom_node('B2',(2,0)) 
d1.add_circle_node('nabla',(1,1))
d1.add_circle_node('delta',(1,2))
d1.add_top_node('T1',(0,3))
d1.add_top_node('T2',(2,3))
d1.add_arrow('B1','nabla',angleA=90,angleB=180)
d1.add_arrow('B2','nabla',angleA=90,angleB=0) 
d1.add_arrow('nabla','delta',angleA=90,angleB=270)
d1.add_arrow('delta','T1',angleA=180,angleB=270)
d1.add_arrow('delta','T2',angleA=0,angleB=270)
sys.stdout.write(t.render(diags=(d1,)))



