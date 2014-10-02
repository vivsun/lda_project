lda_project
===========

LDA scripts for edu data analysis

Basic workflow:

we get html / xml data dump from edu dept. The following script extract plain texts from these data dump:
    
    note_extract.py  note_to_plain_text.py

Tokenize the plain text doc with a simple tokenizer:

    tokenize.py

Turn tokenized text into word frequency matrix:

    word_document_freq.py
    
Take word document freq matrix to LDA input data format (we used lda-c implementation http://www.cs.princeton.edu/~blei/lda-c/)

    lda_C_data_gen.py
    
Some post processing scripts:
    
    phi_compute.py   Calculate phi value from LDA output
    html_alpha_print.py, html_alpha_print.py: output topics and token topic assignemnt in html format
    
Utility scripts:

    MyStemmer.py: a very simple regex stemmer
    
