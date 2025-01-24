import sys
from cdiagram import MatrixDiagram
from jinja2 import Template,FileSystemLoader,Environment

env=Environment(loader=FileSystemLoader('.'),
    line_statement_prefix='%%',variable_start_string='<<',variable_end_string='>>')
t=env.get_template('diag.tex')

d1=MatrixDiagram()
d1.node('A',label='AA')
d1.node('B')
d1.cr()
d1.skip()
d1.node('C','CC')
d1.node('D')
d1.add_arrow('A','B','f',label_position='^')
d1.add_arrow('A','C',r'_\alpha',shape='->>')
d1.add_arrow('C','B')
d1.cluster_by_names('A','B').shift((0.5,0.5)).shift((0.2,0))

sys.stdout.write(t.render(diag=d1))



