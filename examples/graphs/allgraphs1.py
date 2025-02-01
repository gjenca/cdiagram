import sys
from cdiagram import Diagram,Node
from jinja2 import Template,FileSystemLoader,Environment

from cdiagram.cdutils import triangle_over

env=Environment(loader=FileSystemLoader('.'),
    line_statement_prefix='%%',variable_start_string='<<',variable_end_string='>>')
t=env.get_template('graphs.tex')

d1=Diagram()
d1.add_node('u',(0,0))
d1.add_node('v',(1,0))
d1.add_arrow('u','v')
d1.label='G'
d1.label_at=(0.5,-1.5)

d2=Diagram()
d2.add_node('u',(0,0),label=r'\{u\}')
d2.add_node('v',(1,0),label=r'\{v\}')
d2.add_node('uv',triangle_over(d2['u'],d2['v']),label_angle=90,label=r'\{u,v\}')
d2.add_arrow('u','v')
d2.add_arrow('u','uv')
d2.add_arrow('v','uv')
d2.label='S(G)'
d2.cluster_all().shift((2,0))
d2.label_at=(2.5,-1.5)

d3=Diagram()
d3.add_node('u',(0,0),label=r'\{\{u\}\}',label_angle=-120)
d3.add_node('v',(1,0),label=r'\{\{v\}\}',label_angle=-30)
d3.add_node('uv',triangle_over(d3['u'],d3['v']),label_angle=90,label=r'\{\{u,v\}\}')
d3.add_node('ucv',triangle_over(d3['v'],d3['u']),label_angle=-90,label=r'\{\{u\},\{v\}\}')
d3.add_node('ucuv',triangle_over(d3['u'],d3['uv']),label_angle=90,label=r'\{\{u\},\{u,v\}\}')
d3.add_node('vcuv',triangle_over(d3['uv'],d3['v']),label_angle=90,label=r'\{\{v\},\{u,v\}\}')
d3.add_arrow('u','v')
d3.add_arrow('u','uv')
d3.add_arrow('v','uv')
d3.add_arrow('u','ucv')
d3.add_arrow('v','ucv')
d3.add_arrow('u','ucuv')
d3.add_arrow('uv','ucuv')
d3.add_arrow('uv','vcuv')
d3.add_arrow('v','vcuv')
d3.label='S^2(G)'
d3.label_at=(4.5,-1.5)
d3.cluster_all().shift((4,0))

sys.stdout.write(t.render(diags=(d1,d2,d3)))



