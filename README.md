# ivgo-django

## Setup

1. Use Python 3.4+

    ```
    $ python -V
    Python 3.5.1
    ```

2. Download easy\_install and pip

    To download easy\_install, go to the [https://pypi.python.org/pypi/setuptools](Python Package Index \(PyPI\)). 
    You need to download setuptools, which includes easy\_install. Download the package egg (.egg), then install it directly from the file.

    Pip can be installed using easy\_install:

    ```
    $ easy_install pip
    ```

3. Use Git version 1.7+

    ```
    $ git --version
    git version 2.6.0
    ```

4. virtualenv

    Install virtualenv using pip:

    ```
    $ pip install virtualenv
    ```

    Initialise a virtualenv as follows:

    ```
    $ mkdir project
    $ cd project
    $ virtualenv env
    $ source env/bin/activate
    (env) $
    ```

    This creates a sandbox for development purposes. To exit:

    ```
    (env) $ deactivate
    ```

5. Django setup

    If Django is not installed yet:

    ```
    (env) $ pip install django==1.10.5
    ```

    Check the version:

    ```
    (env) $ python
    >>> import django
    >>> django.get_version()
    '1.10.5'
    >>>
    ```
