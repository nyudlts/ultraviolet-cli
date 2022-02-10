# ultraviolet-cli

Invenio module for custom Ultraviolet commands

## Prerequisites
- [Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
- [Pyenv](https://github.com/pyenv/pyenv#installation)


## Develop locally

- Clone the repository
  ``` sh
  git clone git@github.com:nyudlts/ultraviolet-cli.git && cd ultraviolet-cli
  ```
- Install & use specified python version
  ``` sh
  pyenv install --skip-existing
  ```
- Install python requirements in a project pip environment (pipenv)
  ``` sh
  pip install --upgrade -U pip pipenv
  pipenv install
  ```
- Invoke the `ultraviolet-cli` root command via `pipenv`
  ``` sh
  pipenv run ultraviolet-cli
  ```
