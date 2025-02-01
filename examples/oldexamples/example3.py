import sys
from cdiagram import MatrixDiagram
from jinja2 import Template,FileSystemLoader,Environment

env=Environment(loader=FileSystemLoader('.'),
    line_statement_prefix='%%',variable_start_string='<<',variable_end_string='>>')
t=env.get_template('diag.tex')

d1=MatrixDiagram()
d1.node('TXl',label=r'T(X)')
d1.arr('r',label=r'T(\eta_X)')
d1.node('TTX',label=r'T^2(X)')
d1.node('TXr',label=r'T(X)')
d1.cr()
d1.skip()
d1.node('TXd','T(X)')
#d1.add_arrow('TXl','TTX',label=r'T(\eta_X)')
d1.add_arrow('TXr','TTX',label=r'\eta_{T(X)}',label_position='_')
d1.add_arrow('TTX','TXd',label=r'\mu_X')
d1.add_arrow('TXl','TXd',label=r'\mathrm{id}_{T(X)}',label_position='_')
d1.add_arrow('TXr','TXd',label=r'\mathrm{id}_{T(X)}')
sys.stdout.write(t.render(diag=d1,baselength='8.5em'))



