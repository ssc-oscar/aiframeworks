import sys
import gzip
'''
Script file that creates <module name>.first files which lists
repositories and the first time(in Unix seconds) that a commit imported a given module.
Program reads from c2bPtaPkgO<lang>.[0-31].gz files to grab the relevant module and time.

ex) huytofu_huytofu.ML_Projects;1548307159

Program usage: python popmods.py language_of_file_extension module

ex) python popmods.py ipynb tensorflow
'''

dict = {}
lang = sys.argv[1].lower()
module = sys.argv[2]

if lang == "cob":
	dir_lang = "Cob"
elif lang == "cs":
	dir_lang = "CS"
elif lang == "c" or lang == "cpp":
	dir_lang = "C"
elif lang == "erlang":
	dir_lang = "Erlang"
elif lang == "fml":
	dir_lang = "Fml"
elif lang == "fortran":
	dir_lang = "F"
elif lang == "go":
	dir_lang = "Go"
elif lang == "ipynb":
	dir_lang = "ipy"
elif lang == "java":
	dir_lang = "java"
elif lang == "julia":
	dir_lang = "jl"
elif lang == "js":
	dir_lang = "JS"
elif lang == "lua":
	dir_lang = "Lua"
elif lang == "lisp":
	dir_lang = "Lisp"
elif lang == "php":
	dir_lang = "php"
elif lang == "pl":
	dir_lang = "pl"
elif lang == "py":
	dir_lang = "PY"
elif lang == "rb":
	dir_lang = "rb"
elif lang == "r":
	dir_lang = "R"
elif lang == "rs":
	dir_lang = "Rust"
elif lang == "scala":
	dir_lang = "Scala"
elif lang == "sql":
	dir_lang = "Sql"
elif lang == "swift":
	dir_lang = "Swift"

times = []
for i in range(32):
	print("Reading gz file number " + str(i))
	file = gzip.open("/data/play/" + dir_lang + "thruMaps/c2bPtaPkgO" + dir_lang + "." + str(i) + ".gz")

	for line in file.readlines():
		entry = str(line).split(";")
		repo, time = entry[1], entry[2]
		if time in times:
			continue
		else:
			times.append(time)
		if repo not in dict.keys() or time < dict[repo]:
			for word in entry[5:]:
				if module in word:
					dict[repo] = time
					break
	file.close()
first_file = module + ".first"
f = open(first_file, "w")

for key, val in dict.items():
	f.write(key + ";" + val + "\n")
f.close()
