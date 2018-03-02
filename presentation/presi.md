class:
background-image: url(img/explore.jpg)

---
name: about
class: left
background-image: url(img/about.jpg)

.right-column[
Open Minded

|> Science

|> Craftsman

.footnote[
<i class="fab fa-github-square fa-2x"></i> [cmg-dev](https://github.com/cmg-dev)

<i class="fab fa-twitter-square fa-2x"></i> [@codethonian](https://twitter.com/codethonian)
]
]

???
Coder in natural Environment

---
name: light
class: left
background-image: url(img/light.jpg)

.regular[
# Motivation
]

.footnote[
<i class="fa fa-link fa-1x"></i> [Django 2](https://www.djangoproject.com/)
]
???
nothing

---
name: light
class: left, middle
background-image: url(img/light.jpg)

.example_page_left[
``` plain
src 𝚿 python -c "import this"
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
```
]

---
name: light
class: top, center
background-image: url(img/light.jpg)

# Why Django?

.left-column[
<i class="fa fa-bolt fa-1x"></i> [It's Fast](https://www.djangoproject.com/start/)

<i class="fa fa-lock fa-1x"></i> [It's Secure](https://docs.djangoproject.com/en/2.0/topics/security/)

<i class="fa fa-expand fa-1x"></i> [It's Scalable](https://docs.djangoproject.com/en/2.0/faq/general/#does-django-scale)
]
???
nop

---
name: light
class: middle
background-image: url(img/light.jpg)

.regular[
# Why Django?
]
.left-column[
> "Django was invented to meet fast-moving newsroom deadlines, while satisfying the tough requirements of experienced Web developers." [1]
]


.footnote[
<i class="fa fa-link fa-1x"></i> [[1]](https://www.djangoproject.com/start/overview/)
]

???
nop

---
name: motivation
class: left, middle
background-image: url(img/extinct.jpg)

.example_page_left[
# Django is Old

**Started in 2005**

**Very mature, very robust.**
]

???

BSD License

---
name: motivation
class: left, middle
background-image: url(img/extinct.jpg)

.example_page_left[
# Django is Used by...

<i class="fab fa-instagram fa-1x"></i> [Instagram](https://www.instagram.com)

<i class="fab fa-pinterest fa-1x"></i> [Pinterest](https://www.pinterest.de/)

<i class="fab fa-firefox fa-1x"></i> [Mozilla](https://www.mozilla.org/de/)

... more
]

.footnote[
<i class="fa fa-link fa-1x"></i> [See: 25 Most Popular Python+Django Sites](https://www.shuup.com/blog/25-of-the-most-popular-python-and-django-websites/)
]

---
name: motivation
class: left, middle
background-image: url(img/extinct.jpg)

# ⚠️

.example_page_left[
1. Beware of your habits!

   You do not want your code in `/var/www`.

1. Conflicts may occur.

   Avoid modules names like `django` or `test` or `math`.

1. Put your code in a safe place.

   Like `/home/djangos_palace`.
]

???

Habits: Don't put your code in www/root

---
name: motivation
class: left, top
background-image: url(img/extinct.jpg)

# Building a Site 👷

.example_page_left[
**Foundation**

Django comes with a powerful object-relational mapper [[1]].

The data-model syntax [[2]] - it’s been solving many years’ worth of
database-schema problems.

Start a site with:

```bash
$ django-admin startproject newspaper
```

[1]: https://en.wikipedia.org/wiki/Object-relational_mapping
[2]: https://docs.djangoproject.com/en/2.0/topics/db/models/
]

???

On the foundations of a solid database, we can easily construct a Web
Application for our purposes.

---
name: motivation
class: left, top
background-image: url(img/extinct.jpg)

.example_page_left[
```bash
django2_workshop 𝚿 django-admin startproject newspaper
django2_workshop 𝚿 tree newspaper
newspaper
├── manage.py
└── newspaper
    ├── __init__.py
    ├── settings.py
    ├── urls.py
    └── wsgi.py

1 directory, 5 files
```
]

---
name: motivation
class: left, top
background-image: url(img/extinct.jpg)

.example_page_left[
```diff
1a2
> ├── db.sqlite3
6a8,11
>     ├── __pycache__
>     │   ├── __init__.cpython-36.pyc
>     │   ├── settings.cpython-36.pyc
>     │   └── urls.cpython-36.pyc
11c16
< 2 directories, 6 files
---
> 3 directories, 10 files
```
]

???

1. The outer mysite/ root directory is just a container for your project. Its
   name doesn’t matter to Django; you can rename it to anything you like.

1. manage.py: A command-line utility that lets you interact with this Django
   project in various ways.

1. The inner mysite/ directory is the actual Python package for your project.

1. mysite/__init__.py: An empty file that tells Python that this directory
   should be considered a Python package.

1. mysite/settings.py: Settings/configuration for this Django project.

1. mysite/urls.py: The URL declarations for this Django project

1. mysite/wsgi.py: An entry-point for WSGI-compatible web servers

---
name: motivation
class: left, top
background-image: url(img/extinct.jpg)

# 1. Reporter Model 🕵️

.example_page_left[

We use `demo/news/models.py` and add this:

```python
from django.db import models

class Reporter(models.Model):
    full_name = models.CharField(max_length=70)

    def __str__(self):
        return self.full_name
```

This creates our first model 🎉.
]

???
Explain inheritance in Python

---
name: motivation
class: left, top
background-image: url(img/extinct.jpg)

# 1. Article Model 📰

.example_page_left[
No Reporter without Article:

```python
(...)

class Article(models.Model):
    pub_date = models.DateField()
    headline = models.CharField(max_length=200)
    content = models.TextField()
    reporter = models.ForeignKey(Reporter, on_delete=models.CASCADE)

    def __str__(self):
        return self.headline
```

So we have two models in code.
]

---
name: motivation
class: left, top
background-image: url(img/extinct.jpg)

# 2. Migrate 🐘

.example_page_left[
Too insert the models into a database, we simply type:

```bash
python manage.py migrate
```
]
???

explain manage.py

---
name: motivation
class: left, top
background-image: url(img/extinct.jpg)

# 🍱 There is no free lunch! 🍱

.example_page_left[

**Or is it?**

```python
# Import the models
>>> from demo.models import Reporter, Article

# No reporters are in the system, yet.
>>> Reporter.objects.all()
<QuerySet []>

# Create a new Reporter.
>>> r = Reporter(full_name='Deep Thought')

# Save the Reporter.
>>> r.save()
```

This is basically why I love Python ❤️

]

???

---
name: demo
class: left
background-image: url(img/solo_0.jpg)

.left-column[
# Livecoding Fun

**Let's code Together...**
]

---
name: motivation
class: center, middle
background-image: url(img/math.jpg)

.example_page_left[
# Solving Linear Equations 🙈
]

---
name: motivation
class: center, middle
background-image: url(img/math.jpg)

.example_page_left[
## Solving Linear Equations 🙉

You have been taught 👩‍🏫

```plain
z = a x + b y + c
```

Not too hard, right?
]

---
name: motivation
class: center, middle
background-image: url(img/math.jpg)

.example_page_left[
## Solving Linear Equations 🙊

Nearly there:

We need this:

```plain
z_0 = a_0 x + b_0 y
z_1 = a_1 x + b_1 y
z_2 = a_2 x + b_2 y
```
]

---
name: motivation
class: center, middle
background-image: url(img/math.jpg)

.example_page_left[
## Solving Linear Equations 🐵

Laziness > 9000:

__0__ = __A__ __x__ - __b__

All we need and solve for:

__x__ = __A__^-1 * __b__
]

---
name: motivation
class: left, top
background-image: url(img/math.jpg)

.example_page_left[
## Solving Linear Equations 🐵

```python
def solve(A, b):
    """This solves a given linear equation system.
    Ax - b = 0
    We solve for x = A^-1 * b
    :A: The coefficient matrix for A.
    :B: The result vector b.
    :returns: The solution to this equation system x as np.vector().
    """
    import numpy as np
    import numpy.linalg as mat

    A = np.matrix(A)
    b = np.matrix(b)

    A_inv = mat.inv(A)

    x = A_inv * b

    return x
```
]

---
name: demo
class: left
background-image: url(img/solo_0.jpg)

.left-column[
# Livecoding Fun II

**Let's code Together, again...**
]

---
name: motivation
class: left, middle
background-image: url(img/roadmap.jpg)

.example_page_left[
# Facts to Know

| Release Series   | Latest Release   | End of mainstream support   | End of extended support    |
| ---------------- | ---------------- | --------------------------- | -------------------------- |
| (...)            | (...)            | (...)                       | (...)                      |
| 2.0              | 2.0.2            | August 2018                 | April 2019                 |
| 1.11 LTS         | 1.11.10          | December 2, 2017            | Until at least April 2020  |
| (...)            | (...)            | (...)                       | (...)                      |
]

???
nop

---
name: explore
class: left, middle
background-image: url(img/explore.jpg)

.example_page_left[
# Python ❤️

* Machine Learning
* Computer Vision
* Every Other Programming Language
* Math/ Science/ Cool Stuff
* Excel 😍
]

???
nop

---
name: explore
class: left, middle
background-image: url(img/explore.jpg)

.example_page_left[
# Thanks... and stay Curious!
]
