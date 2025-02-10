from setuptools import setup

setup(
    name = 'didi50',
    version = '1.0.0',
    author = 'Thiago Direnzi',
    author_email = 'thiagodb13@gmail.com',
    packages = ['didi50'],
    description = 'didi50 é uma simples ferramenta de envio de requests em massa de forma assincrona usado para testar scalonamento de tasks, desempenho de servidores, entre outros... (Por sua conta em risco)',
    long_description = 'Com essa ferramenta voce pode indicar qual o "alvo", o numero de requests, e se vai usar proxy,'
                        + ' dar enter e ver as varias requisições serem feitas, usado basicamente para testes de '
                        + 'desempenho e afins.',
    url = 'https://github.com/direnzii/didi50',
    project_urls = {
        'Código fonte': 'https://github.com/Direnzii/didi50',
        'Download': 'https://github.com/Direnzii/didi50'
    },
    license = 'MIT',
    keywords = 'requests dos desempenho performance assync assincrono',
    classifiers = [
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: Portuguese (Brazilian)',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Internationalization',
        'Topic :: Scientific/Engineering :: Physics'
    ]
)