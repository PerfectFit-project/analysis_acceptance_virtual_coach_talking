# analysis_acceptance_virtual_coach_talking
This repository contains all software written and used, along with the outcomes across all stages of the thematic analysis conducted on the reasons to find it easy or difficult to talk to the virtual coach. Throughout this project, use was made of the originally provided data set, which was also made public [1].


# Cohen's Kappa 
In the python folder, you will find the first and second coders' encodings (first_coders_hot_one_encoding.csv & second_coders_hot_one_encoding.csv) as well as the pyhon script (cohens_kappa_calculator.py). This folder also contains the output of running the script (cohens_kappa_calculator_output.txt). To run the code yourself, simply run the python file with the two csv files in the same folder. If using the script on other hot one encoded csv files, be sure to adjust the filenames and the text columns and rows to remove according to the comments in the python file.


# Peason's correlation
In the python folder, you will find the python script used to calculate the Pearson's correlations between columns from the pre-screening data, the pre-questionnaire and the post-questionnaire. All columns to be used should be located in the same file. Set the variable "filename" to this files name and simply enter the names of the columns to calculate the correlation for in the variables "col1" and "col2". Running this file will give output the correlation and the p-value of this calculation. In the file pearsons_correlation_calculator_ouput.txt you will find the ouput of the files calculated throughout the research. 


# Coding & Themes
The final themes and coding scheme can be found in "final_coding_scheme.png" & "themes_and_codes_scheme.png". The final coded free-text responses can be found in "final_coded_responses_with_themes_final.xlsx".


# References
[1] N. Albers, M. A. Neerincx, and W.-P. Brinkman, “Acceptance of a Virtual Coach for Quitting Smoking and Becoming Physically Active: Dataset,” May 2022. DOI: 10.4121/19934783.v1.


# License
Copyright (C) 2022 Delft University of Technology.

Licensed under the Apache License, version 2.0. See LICENSE for details.

[![DOI](https://zenodo.org/badge/500115034.svg)](https://zenodo.org/badge/latestdoi/500115034)
