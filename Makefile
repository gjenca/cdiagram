default: strings1.pdf \
	strings2.pdf
#	example1.pdf \
#	example2.pdf \
#	example3.pdf \
#	example4.pdf \
#	example5.pdf \
#	allgraphs1.pdf

.PRECIOUS: %.eps %.tex

%.pdf: %.eps
	epstopdf $(*F).eps

%.eps: %.ps
	ps2eps $(*F).ps -f -l

%.ps: %.dvi
	dvips -o $@ $(*F).dvi

%.dvi: %.tex
	latex $(*F)

%.tex: %.py diag.tex cdiagram.py cdutils.py stringdiags.tex
	python3 $(*F).py > $@

