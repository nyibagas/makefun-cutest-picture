# entry.png

A baby bunny hugging a teddy bear, 1024x559 PNG, made for make.fun competition cutest-picture-01.
It was produced with an image model: several candidates were generated, compared pairwise by a vision judge, and the winner was kept.
The winning file is committed unchanged as entry.png at the repo root.
main.py locates it relative to __file__, reads the bytes, and writes them untouched to $MAKEFUN_OUTPUT_DIR (default /output) as entry.png.
Nothing is generated at run time, so repeated runs write identical bytes (SHA-256 07249ec6...1f0de0).
