import sys
from cdiagram import MatrixDiagram
from jinja2 import Template,FileSystemLoader,Environment

env=Environment(loader=FileSystemLoader('.'),
    line_statement_prefix='%%',variable_start_string='<<',variable_end_string='>>')
t=env.get_template('stringdiags.tex')

d1=MatrixDiagram()
d1.skip()
d1.skip()
d1.node('A',ntype='pnode').shift((0,-0.5))
# or shift afterwards: d1['A'].shift((0,-0.5))
d1.cr()
d1.skip()
d1.skip()
d1.node(r'nabla2',label=r'\nabla')
d1.cr()
d1.skip()
d1.node(r'nabla',label=r'\nabla')
d1.cr()
d1.node('B1',ntype='pnode')
d1.skip()
d1.node('B2',ntype='pnode')
d1.node('B3',ntype='pnode')
d1.cr()
d1.node('B1.',ntype='pnode')
d1.add_arrow('B1','nabla',angleA=90,angleB=180)
d1.add_arrow('B2','nabla',angleA=90,angleB=0)
d1.add_arrow('nabla','nabla2',angleA=90,angleB=180)
d1.add_arrow('B3','nabla2',angleA=90,angleB=0)
d1.add_arrow('nabla2','A',angleA=90,angleB=-90)
d1.add_arrow('B2','B3',atype='cup',arcangle=90)
d1.add_arrow('B1.','B1',angleA=90,angleB=-90)
sys.stdout.write(t.render(diags=(d1,),baselength='3em'))



