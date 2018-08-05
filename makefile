compile:
	gfortran -O2 -fbounds-check -shared -g -o LCSubStr.dll LCSubStr.f90
	gfortran -O2 -fbounds-check -shared -g -o LCSubSeq.dll LCSubSeq.f90
	gfortran -O2 -fbounds-check -shared -g -o HammingDistance.dll HammingDistance.f90
	gfortran -O2 -fbounds-check -shared -g -o Levenshtein.dll Levenshtein.f90
	gfortran -O2 -fbounds-check -shared -g -o GestaltPatternMatching.dll GestaltPatternMatching.f90
	gfortran -O2 -fbounds-check -shared -g -o Jaro_Winkler.dll Jaro_Winkler.f90
	gfortran -O2 -fbounds-check -shared -g -o Damerau_Levenshtein.dll Damerau_Levenshtein.f90
	python callF90lib.py

run:
	python callF90lib.py
