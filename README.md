# Online Knowledge Sharing Platform

Online Knowledge Sharing Platform

## Setup (Before Installation)
- Follow all steps mentioned in `INSTALLATION.md`
- Edit `oksp/settings/conf.sample.py` to `oksp/settings/conf.py`

## Setting up local machine for development
- Use Python 3.5
- Install and configure virtualenvwrapper https://virtualenvwrapper.readthedocs.org/en/latest/
- In local machine use `pip install -r requirements/local.txt`
- Edit `oksp/settings/conf.py` to your local settings

## Setting up Production server
- Use Python 3.5
- Install and configure virtualenvwrapper https://virtualenvwrapper.readthedocs.org/en/latest/
- In local machine use `pip install -r requirements/production.txt`
- Edit `oksp/settings/conf.py` to add your production level settings
- Set environment variable `DJANGO_SETTINGS_MODULE` to `oksp.settings.production`
- Continue with Django deployment normally
