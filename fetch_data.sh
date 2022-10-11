#!/bin/bash
echo "Make sure you have set an env-variable GITLAB_TOKEN"

rm listperson_fackel.xml
rm -rf ./data
echo "downloading fackel persons from ${DL_URL}"
wget -O listperson_fackel.xml --header "PRIVATE-TOKEN: ${GITLAB_TOKEN}" ${DL_URL}

wget -O refined.xlsx --header "PRIVATE-TOKEN: ${GITLAB_TOKEN}" "https://gitlab.oeaw.ac.at/api/v4/projects/33/repository/files/openrefine%2FFackel-Personen_mit%20gnd.xlsx/raw?ref=master"

wget -O konkordanz.csv --header "PRIVATE-TOKEN: ${GITLAB_TOKEN}" "https://gitlab.oeaw.ac.at/api/v4/projects/33/repository/files/openrefine%2Fpersonen_id_fackel_id_konkordanz.csv/raw?ref=master"


echo "transforming fackel persons into TEI"
python transform.py

echo "adding PMB IDs"
python add_idno.py

echo "add GND and WikiData IDs"
python add_gnd_ids.py