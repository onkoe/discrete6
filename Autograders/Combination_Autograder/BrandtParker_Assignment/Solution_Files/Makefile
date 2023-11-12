all: python

java: combination.java

python: combination.py
	python3 combination.py ../../../test_data/Combinations/input-1.csv test0_output.csv

c: combinations.c
	gcc -w -g -Wall -o combinations combinations.c -lm -std=c99

run: python

clean: 
	rm *.o *.exe