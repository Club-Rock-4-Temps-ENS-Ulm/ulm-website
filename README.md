# Site du Club Rock 4 Temps de l'ENS Ulm

Site développé avec [Pelican](http://getpelican.com/') en Python.


# Dev

Make sure you
* Have Python version 3.6+
* Have cloned this repository
* Have `cd`'ed in this repository

## Install 

* Install Pelican & dependencies

```
pip install --upgrade pip pipenv
pipenv install
```

* Install Pelican plugins

```
git clone https://github.com/getpelican/pelican-plugins
mv pelican-plugins plugins
mkdir data
mv plugins data/ 
```

## Generate / serve

* Enter your virtual env

`pipenv shell`

Generate your content in HTML with:

`make html`

To serve the site so it can be previewed in your browser at http://localhost:8000:

`make serve`

If you’d prefer to have Pelican automatically regenerate your site every time a change is detected (handy when testing locally), use the following command instead:

`make regenerate`

Normally you would need to run make regenerate and make serve in two separate terminal sessions, but you can run both at once via:

`make devserver`

Read more documentation on [Pelican doc](https://docs.getpelican.com/en/3.1.1/getting_started.html)
