import sys
from cdiagram import Diagram,Node
from jinja2 import Template,FileSystemLoader,Environment

from cdutils import triangle_over

env=Environment(loader=FileSystemLoader('.'),
    line_statement_prefix='%%',variable_start_string='<<',variable_end_string='>>')
t=env.get_template('graphs.tex')

d1=Diagram()
d1.add_node('1',(1,0),label_angle=90)
d1.add_node('a',(0,1))
d1.add_node('b',(2,1))
d1.add_node('0',(1,2))
d1.add_arrow('0','a')
d1.add_arrow('0','b')
d1.add_arrow('1','b')
d1.add_arrow('1','a')
d1.label='2^2'
d1.label_at=(1,3)

d2=Diagram()
d2.add_node('P',(0,0),label='2^2',label_angle=90)
d2.add_node('0ab',(0,1),label='\{0,a,b\}',label_angle=0)
d2.add_node('0',(0,2),label='\{0\}',label_angle=-90)
d2.add_arrow('P','0ab')
d2.add_arrow('0','0ab')
d2.label='\overline{2^2}'
d2.cluster_all().shift((4,0))
d2.label_at=(4,3)

sys.stdout.write(t.render(diags=(d1,d2,)))



