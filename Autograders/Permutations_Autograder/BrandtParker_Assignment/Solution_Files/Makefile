all: 
	@echo "Python does not need to compile"

java: combination.java

python: permutation.py
	python3 permutation.py ../../../test_data/Permutations/input-1.csv test0_output.csv

c: combinations.c
	gcc -w -g -Wall -o combinations combinations.c -lm -std=c99

run: python

clean: 
	rm *.o *.exe