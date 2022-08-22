# Requirements

  * Python 3.9

> This code was developed as the showcase of basic python development.

> 
# Installation
Install the dependencies from the requirements.txt file and then you can run this app. This app requires only the beautifullsoup4 and requests package plus their dependencies.

# Sample Execution & Output

Run the program from its root directory with the one mandatory argument --input to let it download all url 
links at the address and all other "nested" links in to the default depth of third level.

```
python __main__.py "--input-address" "https://www.bbc.com/"
```

Logs from the operation will be displayed and finally an output json file will
be generated to the data folder where all downloaded pages will be stored.

```
Usage: python __main__.py "--input-address" "https://www.bbc.com/" "--depth" "5"
```

For help about the other optional arguments run:

```
python __main__.py "--help"
```


