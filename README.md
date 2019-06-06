# AI Frameworks
A study of the spread and prevalence of AI frameworks used in jupyter notebooks


The research questions is what is the uptake of AI frameworks in publi jupyter notebooks

We utilize WoC infrastructure ad follow following steps:

1. Identify files that are jupyter notebooks
(how)

2. Obtain all the blobs associated with all versions of these files

3. Extract import/from statements by parsing these blobs

4. Use time of the associated commit to determin the first time the import statement was created
