default: all

all: \
	examples/oldexamples/example5.pdf \
	examples/oldexamples/example4.pdf \
	examples/oldexamples/example2.pdf \
	examples/oldexamples/example1.pdf \
	examples/oldexamples/example3.pdf \
	examples/graphs/mc.pdf \
	examples/graphs/allgraphs1.pdf \
	examples/strings/frobenius1.pdf \
	examples/strings/strings2.pdf \
	examples/strings/strings1.py

.PRECIOUS: %.tex

%.pdf: %.eps
	epstopdf $<

%.eps: %.ps
	ps2eps $< -f -B

%.ps: %.dvi
	dvips -o $@ $<

%.dvi: %.tex
	cd $(@D) ; latex $(*F).tex
	cd $(@D) ; rm $(*F).aux ; rm $(*F).log

%.tex: %.py stringdiags.tex graph.tex graphs.tex stringdiags_labelled.tex
	python3 $< > $@

