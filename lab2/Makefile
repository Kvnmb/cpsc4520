CONDOR = condor*
DATA = *.out splits
GENOME = agambiae.small.fasta
MAKEFLOW = swcompare.mf
OUTFILE = top10.txt
ERROR = makeflow.failed*

all: $(OUTFILE)

splits:
	mkdir splits

$(MAKEFLOW): makeflowgen splits
	perl makeflowgen $(GENOME) > $(MAKEFLOW)

$(OUTFILE): $(MAKEFLOW)
	makeflow -T condor -J 250 $(MAKEFLOW)
	perl scoring > $(OUTFILE)

build: $(MAKEFLOW)

run: $(OUTFILE)

clean:
	makeflow -c $(MAKEFLOW) || true
	rm -rf $(CONDOR) $(DATA) $(ERROR) $(MAKEFLOW) $(OUTFILE) || true

lean:
	makeflow -c $(MAKEFLOW) || true
	rm -rf $(CONDOR) $(ERROR)
