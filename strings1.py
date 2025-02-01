import sys
from cdiagram import StringDiagram
from jinja2 import Template,FileSystemLoader,Environment

env=Environment(loader=FileSystemLoader('.'),
    line_statement_prefix='%%',variable_start_string='<<',variable_end_string='>>')
t=env.get_template('stringdiags.tex')

d1=StringDiagram()
d1.add_bottom_node('B1',(0,0))
d1.add_bottom_node('B2',(2,0))
d1.add_bottom_node('B3',(3,0))
d1.add_circle_node('nabla1',(1,1))
d1.add_node('nabla2',(2,2),label=r'\nabla')
d1.add_top_node('T',(2,3),ntype=r'pnode')
d1.add_arrow('B1','nabla1',angleA=90,angleB=180,label='S')
d1.add_arrow('B2','nabla1',angleA=90,angleB=0)
d1.add_arrow('nabla1','nabla2',angleA=90,angleB=180)
d1.add_arrow('B3','nabla2',angleA=90,angleB=0)
d1.add_arrow('nabla2','T',angleA=90,angleB=-90)
sys.stdout.write(t.render(diags=(d1,),baselength='3em'))



