<div align="center" id="top"> 
  <img src="./.github/app.gif" alt="Credit System" />

  &#xa0;

  <!-- <a href="https://creditsystem.netlify.app">Demo</a> -->
</div>

<h1 align="center">Credit System</h1>

<p align="center">
  <img alt="Github top language" src="https://img.shields.io/badge/language-Python-red">
  <img alt="Repository size" src="https://img.shields.io/badge/Repository_size-400KB-red">
  <img alt="License" src="https://img.shields.io/badge/License-MIT-red">
  <a href="https://linkedin.com/in/saurabhjdsingh"><img alt="Author" src="https://img.shields.io/badge/Author-Saurabhjdsingh-blue"></a>
</p>

<p align="center">
  <a href="#dart-about">About</a> &#xa0; | &#xa0; 
  <a href="#sparkles-features">Features</a> &#xa0; | &#xa0;
  <a href="#rocket-technologies">Technologies</a> &#xa0; | &#xa0;
  <a href="#white_check_mark-requirements">Requirements</a> &#xa0; | &#xa0;
  <a href="#checkered_flag-starting">Starting</a> &#xa0; | &#xa0;
  <a href="#memo-license">License</a> &#xa0; | &#xa0;
  <a href="https://github.com/saurabhjdsingh" target="_blank">Author</a>
</p>

<br>

## :dart: About ##

A backend app of credit-approval system, which renders data from Excel files and injest data into a database with the help of background workers. 
It consists of different APIs which provide functionalities like: (View screen-recording by clicking below)
- [Import test data from xlsx files](https://drive.google.com/file/d/1SRRRXOyQecO2Anzwzu17vZwoys2Phj78/view?usp=sharing)
- [register](https://drive.google.com/file/d/1VmS9ENNx9coD1c_23mNJPlclnfsJUodL/view?usp=sharing)
- [check credit score & eligibility](https://drive.google.com/file/d/1dQ8EwBaUFBkGkxoVJuaACZNVA0ANKRLi/view?usp=sharing)
- [create loan](https://drive.google.com/file/d/1_1RuSX_XW7da6jVcKreJtMDRCm2gkd2o/view?usp=sharing)
- [View Loan by ID or view all loans of a customer](https://drive.google.com/file/d/1_tQ12auDGr-0x6-2OfQtTsvbq4h3rgbp/view?usp=sharing)
- and more...

## :sparkles: Features ##

:heavy_check_mark: RESTfull APIs;
:heavy_check_mark: Implimentation of background workers;\
:heavy_check_mark: SQL migrations;
:heavy_check_mark: Readability;

## :rocket: Technologies ##

The following tools were used in this project:

- [Python](https://www.python.org/)
- [Django](https://www.djangoproject.com/start/overview/)
- [Rest Framework](https://www.django-rest-framework.org/)
- [Celery](https://docs.celeryq.dev/en/stable/index.html)
- [Postgres](https://www.postgresql.org/docs/)

## :white_check_mark: Requirements ##

Before starting :checkered_flag:, you need to have [Git](https://git-scm.com), [Python](https://www.python.org/) and [Redis](https://redis.io/) installed.

## :checkered_flag: Starting ##

```bash
+ FOR MAC (These commands can be different for non-Linux computers):


# Install Redis (background worker service, used with celery):
brew update
brew install redis

# Set up a virtual env. into parent folder

1. `python3 -m venv env`
2. `source env/bin/active`

# Clone this project (Kindly clone this repository into the parent folder)
$ git clone https://github.com/saurabhjdsingh/Credit-Approval-System

# Go to the project
$ cd Credit-Approval-System

# install dependencies
$ pip install -r requirements.txt

# runserver (In first terminal window)
$ python manage.py runserver

# Start Redis Server (In the second terminal):
$ redis-server

# Start Celery Worker (In the Third terminal):
$ celery -A credit worker --loglevel=info


# The server will initialize in the <http://127.0.0.1:8000/>
```




## :memo: License ##

This project is under license from MIT. For more details, see the [LICENSE](LICENSE.md) file.

Made with :heart: by <a href="https://linkedin.com/in/saurabhjdsingh" target="_blank">Saurabh</a>

&#xa0;

<a href="#top">Back to top</a>
