import gzip
import shutil

with open('demo.pdf', 'rb') as f_input:
    with gzip.open('demo.pdf.gz', 'wb') as f_output:
        shutil.copyfileobj(f_input,f_output)