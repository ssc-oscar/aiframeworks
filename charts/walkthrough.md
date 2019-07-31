# Creating a graph using given modules

## Step 1: Create .first files
To show first-time imports for a given module and language, i.e. Tensorflow under ipynb files, under different repos, run popmods.py:
```
python popmods.py ipynb tensorflow
```
This will create the file `tensorflow.first` that contains a list of repo names and Unix timestamps of their first time imports for Tensorflow.

## Step 2: Graphing info from .first files
Using modtrends.py, you can graph either one module.first file or multiple files to make comparisons over time. 

If we wanted to compare Tensorflow vs. Keras, for example, run:
```
python3.6 modtrends.py tensorflow.first keras.first
```
You will now have a .png file of the graph, `Tensorflow-vs-Keras.png` Running Tensorflow by itself would create `Tensorflow.png`

### Tensorflow-vs-Keras.png
![Tensorflow-vs-Keras](ipynb_charts/Tensorflow-vs-Keras.png)
