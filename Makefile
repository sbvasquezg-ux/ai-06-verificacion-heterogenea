.PHONY: test simulate figures lean

test:
	python3 -m unittest discover -s tests -v
simulate:
	python3 sim.py
figures: simulate
	python3 scripts/plot_example.py
lean:
	cd lean && lake env lean MainTheorems.lean
