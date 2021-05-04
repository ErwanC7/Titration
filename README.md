# Titration

My program read titrant volume (in ml) and pH couples from a csv file, and output:
* the derivative values for each given volume,
* the closest point from the equivalence point amongst those given points,
* the second derivative values for each given volume,
* an estimate of the second derivative values every 0.1 ml around the above closest point from theequivalence point, using linear interpolation,
* the proper equivalence point, estimated from the second derivative.

>## Langages & compilation

* using Python
* I don't compile but I used a Makefile
