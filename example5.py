import sys
from cdiagram import MatrixDiagram
from jinja2 import Template,FileSystemLoader,Environment

env=Environment(loader=FileSystemLoader('.'),
    line_statement_prefix='%%',variable_start_string='<<',variable_end_string='>>')
t=env.get_template('diag.tex')

d=MatrixDiagram()
d.skip()
d.node('M1',label=r'2^{[2]\times[2]}')
d.cr()
d.node('L1',label=r'2^{[3]\times[2]}')
d.skip()
d.node('A')
d.cr()
d.skip()
d.node('M2',label=r'2^{[2]\times[2]}')
d.cr()
d.skip()
d.node('M3',label=r'2^{[2]\times[2]}')
d.add_arrow('M1','L1',label=r'_f*\mathrm{id}')
sys.stdout.write(t.render(diag=d,baselength='8.5em'))



