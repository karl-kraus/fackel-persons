#!/bin/bash
echo "Make sure you have set an env-variable GITLAB_TOKEN"

rm listperson_fackel.xml
echo "downloading fackel persons from ${DL_URL}"
wget -O listperson_fackel.xml --header "PRIVATE-TOKEN: ${GITLAB_TOKEN}" ${DL_URL}

echo "transforming fackel persons into TEI"
python transform.py