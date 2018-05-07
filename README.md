Install
=======

You can install Calysto Chatbot into the system folders:

```
sudo pip install --upgrade calysto_chatbot
sudo python -m calysto_chatbot install
```

or into the user folder with:

```
pip install --upgrade calysto_chatbot --user
python -m calysto_chatbot install --user
```

Use it in the console, qtconsole, or notebook with Jupyter:

```
jupyter console --kernel calysto_chatbot
jupyter qtconsole --kernel calysto_chatbot
jupyter notebook 
```

Usage
=====

Use "load NAME" to load collection of rules, like:

```
load alice
```

You can also use the %learn magic, like:

```
%learn {AIML_PATH}/standard/startup.xml
load aiml b
```

`{AIML_PATH}` gets expanded to system chatbot rules dictionary.

Requires (installed automatically with pip)
===========================================

* aiml
* jupyter
* Python2 or Python3
* metakernel

