import sys
from cdiagram import MatrixDiagram
from jinja2 import Template,FileSystemLoader,Environment

env=Environment(loader=FileSystemLoader('.'),
    line_statement_prefix='%%',variable_start_string='<<',variable_end_string='>>')
t=env.get_template('diag.tex')

d1=MatrixDiagram()
d1.node('A')
d1.skip()
d1.node('B')
d1.cr()
d1.skip()
d1.node('C')
d1.add_arrow('A','B',label=r'\mathrm{id}_{T(X)}',type='arc',arcangle=-45)
sys.stdout.write(t.render(diag=d1,baselength='8.5em'))



