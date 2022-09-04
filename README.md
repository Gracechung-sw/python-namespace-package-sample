# Packaging namespace packages

https://packaging.python.org/guides/packaging-namespace-packages/

I have one pacakge set up like this:

```
somestuff_root/
    setup.py
    myutils/
        __init__.py
        a/
            __init__.py
            somestuff.py
```

I have another package setup like this:

```
otherstuff_root/
    setup.py
    myutils/
        __init__.py
        b/
            __init__.py
            otherstuff.py
```

so things are organized in my site-packages/ directory like:

```
myutils/
    a/
        somestuff.py
    b/
        otherstuff.py
```

which is exactly what I want after installing them both with pip.

And you use this package in your code like so:

```
from myutils import a
from myutils import b
```

Namespace packages allow you to split the sub-packages and modules within a single package across multiple, separate distribution packages (referred to as distributions in this document to avoid ambiguity). For example, if you have the following package structure:

📦python-namespace-package-sample  
┣ 📂a_module_pkg  
┃ ┣ 📂mynamespace  
┃ ┃ ┗ 📂a_module  
┃ ┃ ┃ ┣ 📂AI  
┃ ┃ ┃ ┃ ┗ 📜analyze.py  
┃ ┃ ┃ ┗ 📜**init**.py  
┃ ┗ 📜setup.py  
┣ 📂b_module_pkg  
┃ ┣ 📂mynamespace  
┃ ┃ ┗ 📂b_module  
┃ ┃ ┃ ┣ 📂AI  
┃ ┃ ┃ ┃ ┣ 📜**init**.py  
┃ ┃ ┃ ┃ ┗ 📜analyze.py  
┃ ┃ ┃ ┗ 📜**init**.py  
┃ ┗ 📜setup.py  
┣ 📂common_pkg  
┃ ┣ 📂mynamespace  
┃ ┃ ┗ 📂common  
┃ ┃ ┃ ┣ 📂types  
┃ ┃ ┃ ┃ ┗ 📜**init**.py  
┃ ┃ ┃ ┣ 📜**init**.py  
┃ ┃ ┃ ┣ 📜exception.py  
┃ ┃ ┃ ┗ 📜log.py  
┃ ┗ 📜setup.py

Then you can break these sub-packages into two separate distributions:
Each sub-package can now be separately installed, used, and versioned.
Delivery of individual modules without needing all parts of a large project.
Reuse of package names which may not normally be available.

📦mynamespace  
┣ 📂a_module  
┃ ┣ 📂AI  
┃ ┃ ┗ 📜analyze.py  
┃ ┗ 📜**init**.py  
┣ 📂b_module  
┃ ┣ 📂AI  
┃ ┃ ┣ 📜**init**.py  
┃ ┃ ┗ 📜analyze.py  
┃ ┗ 📜**init**.py  
┗ 📂common  
┃ ┣ 📂types  
┃ ┃ ┗ 📜**init**.py  
┃ ┣ 📜**init**.py  
┃ ┣ 📜exception.py  
┃ ┗ 📜log.py

From the root directory, running the following command will install a package

```
python3 -m venv venv && source venv/bin/activate

cd python-namespace-package-sample/a_module_pkg

pip install .

cd python-namespace-package-sample/b_module_pkg

pip install .

cd python-namespace-package-sample/common_pkg

pip install .

python3 example.py
```

Result:

b module  
common log  
b module analyzer  
a module

# PyPI server

If you want to use PyPI server and upload these packages,  
see [[Python] Private PyPI Server 세팅 및 upload and install packages](https://libertegrace.tistory.com/entry/Python-Private-PyPI-Server-%EC%84%B8%ED%8C%85-%EB%B0%8F-upload-and-install-packages)

Start PyPI server using docker-compose.yml file.

```
$ docker-compose up -d --build
```

and go localhost:8080

## Reference

- https://stackoverflow.com/questions/7182117/python-multiple-packages-with-multiple-setup-py-files
- https://sourceweaver.com/post/94805194515/python-namespace-packages
- https://peps.python.org/pep-0420/#nested-namespace-packages
- https://hcnoh.github.io/2019-01-30-python-namespace
