# Repository Coverage

[Full report](https://htmlpreview.github.io/?https://github.com/Mive667/Education-Victory/blob/python-coverage-comment-action-data/htmlcov/index.html)

| Name                                |    Stmts |     Miss |   Branch |   BrPart |   Cover |   Missing |
|------------------------------------ | -------: | -------: | -------: | -------: | ------: | --------: |
| src/backend/EX/asgi.py              |        4 |        4 |        0 |        0 |      0% |     10-16 |
| src/backend/EX/settings.py          |       41 |        0 |        0 |        0 |    100% |           |
| src/backend/EX/urls.py              |       15 |        0 |        0 |        0 |    100% |           |
| src/backend/EX/wsgi.py              |        4 |        4 |        0 |        0 |      0% |     10-16 |
| src/backend/common/admin.py         |        5 |        0 |        0 |        0 |    100% |           |
| src/backend/common/apps.py          |        4 |        0 |        0 |        0 |    100% |           |
| src/backend/common/models.py        |       17 |        0 |        0 |        0 |    100% |           |
| src/backend/common/serializers.py   |        6 |        0 |        0 |        0 |    100% |           |
| src/backend/common/views.py         |        9 |        2 |        0 |        0 |     78% |     11-12 |
| src/backend/public/admin.py         |        1 |        0 |        0 |        0 |    100% |           |
| src/backend/public/apps.py          |        4 |        0 |        0 |        0 |    100% |           |
| src/backend/public/models.py        |        1 |        0 |        0 |        0 |    100% |           |
| src/backend/public/views.py         |       16 |        8 |        2 |        0 |     44% |7, 11, 15, 19-22, 26-98 |
| src/backend/question/admin.py       |       15 |        0 |        0 |        0 |    100% |           |
| src/backend/question/apps.py        |        4 |        0 |        0 |        0 |    100% |           |
| src/backend/question/models.py      |       67 |        1 |       12 |        0 |     99% |        51 |
| src/backend/question/serializers.py |       30 |        3 |        0 |        0 |     90% |31, 34, 37 |
| src/backend/question/views.py       |       40 |       23 |       10 |        0 |     34% |11-12, 18-23, 29-43, 49-50 |
|                           **TOTAL** |  **283** |   **45** |   **24** |    **0** | **81%** |           |


## Setup coverage badge

Below are examples of the badges you can use in your main branch `README` file.

### Direct image

[![Coverage badge](https://raw.githubusercontent.com/Mive667/Education-Victory/python-coverage-comment-action-data/badge.svg)](https://htmlpreview.github.io/?https://github.com/Mive667/Education-Victory/blob/python-coverage-comment-action-data/htmlcov/index.html)

This is the one to use if your repository is private or if you don't want to customize anything.

### [Shields.io](https://shields.io) Json Endpoint

[![Coverage badge](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/Mive667/Education-Victory/python-coverage-comment-action-data/endpoint.json)](https://htmlpreview.github.io/?https://github.com/Mive667/Education-Victory/blob/python-coverage-comment-action-data/htmlcov/index.html)

Using this one will allow you to [customize](https://shields.io/endpoint) the look of your badge.
It won't work with private repositories. It won't be refreshed more than once per five minutes.

### [Shields.io](https://shields.io) Dynamic Badge

[![Coverage badge](https://img.shields.io/badge/dynamic/json?color=brightgreen&label=coverage&query=%24.message&url=https%3A%2F%2Fraw.githubusercontent.com%2FMive667%2FEducation-Victory%2Fpython-coverage-comment-action-data%2Fendpoint.json)](https://htmlpreview.github.io/?https://github.com/Mive667/Education-Victory/blob/python-coverage-comment-action-data/htmlcov/index.html)

This one will always be the same color. It won't work for private repos. I'm not even sure why we included it.

## What is that?

This branch is part of the
[python-coverage-comment-action](https://github.com/marketplace/actions/python-coverage-comment)
GitHub Action. All the files in this branch are automatically generated and may be
overwritten at any moment.