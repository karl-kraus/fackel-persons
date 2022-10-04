# fackel-persons
repo to automatgically merge Persons from Fackel with PMB


Once upon a time (summer 2022) [csae8092](https://github.com/csae8092) trained a csv-dedupe model to match person entitites from the ["Fackel"](https://fackel.oeaw.ac.at/) with [PMB-Persons](https://pmb.acdh.oeaw.ac.at/). 

In order to make the process of merging those two datasets as reproducable as possible, the generated training data (`./dedupe_files/training.json`) as well as the ouput the dedupe workflow `output_link.csv` is checked into this repo.

`fetch_data.sh` is a simple shell script to fetch the latest version of the Fackel-Personen data from a non public gitlab-repo and convert it into XML/time

