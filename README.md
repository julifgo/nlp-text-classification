# IT Tickets Tagger [NLP]
## Introduction 
[Completar]

## Getting Started
venv: https://docs.python.org/3/library/venv.html
```
$ python -m venv .env

$ source .env/bin/activate
$ pip install -r requirements
$ pip install -e .
$ pip install -e src/ # este instala common, para buildear modelo
$ ...whatever you want...
$ deactivate
```

or (not recommended)

```
$ python -m venv --system-site-packages .env 
# and so on
```

To use environment at jupyter notebooks or lab
```
$ python -m ipykernel install --user --name=<my_env_name>
...
$ jupyter kernelspec list
$ jupyter kernelspec uninstall <my_env_name>
```

### Environment guides: 

https://towardsdatascience.com/create-virtual-environment-using-virtualenv-and-add-it-to-jupyter-notebook-6e1bf4e03415

https://janakiev.com/blog/jupyter-virtual-envs/ 

kernels: http://queirozf.com/entries/jupyter-kernels-how-to-add-change-remove


### structuring python projects: 
https://docs.python-guide.org/writing/structure/#structuring-your-project
https://stackoverflow.com/questions/53676057/setup-py-installing-local-packages  


## Train Model
```
$ python src/clean/Model.py
```

## Serve API
- press F5 in vscode and debug flask app at api/api.py script
- go to localhost:5000 

## TODO's
- validar requirements necesarios  
necesitamos saber las versiones de las libs para utilizarlas en un virtual environment

- agregar alguna lib de 12-factors, like python-dotenv y agregar las variables de entorno allí.  
[ver] No olvidar tener una clase config o un setup.cfg

- borrar todas los modulos de notebooks y usarlos directamente desde src  
probar si ese enfoque funciona bien para dejar el código más limpio

- git hooks para limpiar todas las notebooks (?)   
[aquí](https://mg.readthedocs.io/git-jupyter.html) recomiendan limpiar todas las notebooks y mantener en una carpeta "reports" las cosas, o en notebooks estaticas de reporte. 

```
python3 -m nbconvert --clear-output *.ipynb **/*.ipynb
```

- buscar una mejor explicación o como funcionan los packages en python
Para una mejor utilización de los modulos (siempre hay que crear setup.py? __init__.py? etc)
Necesario una miniguía.

- agregar schema validator en los request:
cerberus o marchmallow

- el path de "stopwords-transformer" no funciona, cuando lo pasás por parámetro siempre lo pone en None
Por algún motivo, se llama dos veces al init del transformer, y la 2da vez se saltean los parámetros.
Ver de armar el pipeline "por columna" directamente, y no por etapas


## Contribute
HAT Team
