BOOKS = books
CONDOR = condor*
DATA = *.out
ERROR = makeflow.failed* *.makeflowlog
MAKEFLOW = wordcount.mf
OUTFILE = top100.words
WORDS = *.words

all: $(OUTFILE)

$(BOOKS):
	unzip books.zip

$(MAKEFLOW): makeflowgen $(BOOKS)
	perl makeflowgen $(BOOKS) > $(MAKEFLOW)

$(OUTFILE): $(MAKEFLOW)
	work_queue_factory -T condor -M osgtest -w 20 -W 200 --workers-per-cycle 20 &
	makeflow -T wq -M osgtest -L wordcount.condor.log $(MAKEFLOW)
	perl cleanup

build: $(MAKEFLOW)

run: $(OUTFILE)

condor: $(MAKEFLOW)
	makeflow -T condor -L wordcount.condor.log $(MAKEFLOW)

clean:
	makeflow -c $(MAKEFLOW) || true
	rm -rf $(BOOKS) $(CONDOR) $(DATA) $(ERROR) $(MAKEFLOW) $(OUTFILE) || true

lean:
	makeflow -c $(MAKEFLOW) || true
	rm -rf $(CONDOR) $(ERROR)
