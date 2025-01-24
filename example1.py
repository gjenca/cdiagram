import sys
from cdiagram import Diagram,Node
from jinja2 import Template,FileSystemLoader,Environment

env=Environment(loader=FileSystemLoader('.'),
    line_statement_prefix='%%',variable_start_string='<<',variable_end_string='>>')
t=env.get_template('diag.tex')

d=Diagram()
d.add_node('A',(0,0),label='AAAAAAAAAAA')
d.add_node('B',(1,0)).shift((0.5,0))
d.add_arrow('A','B',label='f')

sys.stdout.write(t.render(diag=d))



