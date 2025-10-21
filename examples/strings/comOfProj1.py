import sys
from cdiagram import StringDiagram
from jinja2 import Template,FileSystemLoader,Environment

env=Environment(loader=FileSystemLoader('.'),
    line_statement_prefix='%%',variable_start_string='<<',variable_end_string='>>')
t=env.get_template('stringdiags_labelled.tex')

d1=StringDiagram()
d1.add_state('v',(1,-0.5),label=r'\mathbf{v}')
d1.add_node('pi',(1,1),label=r'\pi')
d1.add_circle_node('delta',(1,2))
d1.add_circle_node('nabla',(1,4))
d1.add_top_node('T',(1,5))
d1.add_arrow('v','pi',angleA=90,angleB=-90)
d1.add_arrow('pi','delta',angleA=90,angleB=-90)
d1.add_arrow('delta','nabla',angleA=180,angleB=180)
d1.add_arrow('delta','nabla',angleA=0,angleB=0)
d1.add_arrow('nabla','T',angleA=90,angleB=-90)
sys.stdout.write(t.render(diags=(d1,)))



