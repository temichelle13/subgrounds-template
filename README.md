# subgrounds-template

[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/0xPlaygrounds/subgrounds-template)

This repo contains a simple setup for bootstrapping a project with `subgrounds`. We recommend following our [setup](https://docs.playgrounds.network/subgrounds/faq/setup/) guide to maintain a localized project setup!

## Instructions

Make sure you have Python 3.10+ installed.

> Note: Checkout our [guide](https://docs.playgrounds.network/subgrounds/faq/setup/version_management) for tips on how to do that!

1. "Use this template" > "Create a repository"
2. `python -m venv .venv && source .venv/bin/activate`
   - Check out our guide on environments [here](https://docs.playgrounds.network/subgrounds/faq/setup)
3. `pip install -r requirements.txt`
   - You can use `python -m pip` as well
4. `python main.py`

To deactivate the environment:

```bash
deactivate
```

To update dependencies:

```bash
pip install my-package
pip freeze > requirements.txt  # or manually add your package + version
```

## Important
This repo is licensed as MIT which means using the template will default your repo to MIT. Make sure to change this in a follow up commit (also update the copyright holder, etc).
