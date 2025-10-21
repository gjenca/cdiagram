import sys
from cdiagram import StringDiagram
from jinja2 import Template,FileSystemLoader,Environment

env=Environment(loader=FileSystemLoader('.'),
    line_statement_prefix='%%',variable_start_string='<<',variable_end_string='>>')
t=env.get_template('stringdiags.tex')

d1=StringDiagram() 
d1.add_bottom_node('B1',(0,0)) 
d1.add_bottom_node('B2',(3,0)) 
d1.add_circle_node('delta',(3,1))
d1.add_circle_node('nabla',(1,2))
d1.add_top_node('T1',(1,3))
d1.add_top_node('T2',(4,3))
d1.add_arrow('B1','nabla')
d1.add_arrow('B2','delta') 
d1.add_arrow('delta','nabla')
d1.add_arrow('delta','T2')
d1.add_arrow('nabla','T1')
d1.compute_angles()
sys.stdout.write(t.render(diags=(d1,)))



