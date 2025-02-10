python setup.py sdist /*atualiza as info*/
twine upload dist/* --repository-url https://test.pypi.org/legacy/
twine upload dist/* --repository-url https://upload.pypi.org/legacy/