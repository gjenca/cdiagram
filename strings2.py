import sys
from cdiagram import MatrixDiagram
from jinja2 import Template,FileSystemLoader,Environment

env=Environment(loader=FileSystemLoader('.'),
    line_statement_prefix='%%',variable_start_string='<<',variable_end_string='>>')
t=env.get_template('stringdiags.tex')

d1=MatrixDiagram()
d1.skip()
d1.node('chi',ntype='effect',label=r'\chi')
d1.cr()
d1.cr()
d1.skip()
d1.node(r'nabla',label=r'\nabla')
d1.cr()
d1.cr()
d1.node('v1',ntype='state',label=r'v')
d1.skip()
d1.node('v2',ntype='state',label=r'v')
d1.add_arrow('nabla','chi',angleA=90,angleB=-90)
d1.add_arrow('v1','nabla',label='S',angleA=90,angleB=180)
d1.add_arrow('v2','nabla',angleA=90,angleB=0)
sys.stdout.write(t.render(diags=(d1,),baselength='3em'))



