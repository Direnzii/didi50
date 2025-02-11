from setuptools import setup

setup(
    name = 'didi50',
    version = '1.0.1',
    author = 'Thiago Direnzi',
    author_email = 'thiagodb13@gmail.com',
    packages = ['didi50'],
    description = 'Is a simple and efficient tool for sending bulk asynchronous requests. It is ideal for testing task scalability, server performance, and other load analysis. (Use at your own risk.)',
    long_description = 'With didi50, you can easily configure the "target" (destination address), set the number of requests to be sent, and choose whether to use proxies. Once the parameters are set, simply press Enter and watch multiple requests being sent simultaneously. The tool is primarily designed for performance testing, stress testing, and server capacity evaluation, but can also be used in other scenarios related to network traffic analysis.',
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
        'Topic :: Scientific/Security :: DOS',
        'Topic :: Test/QA :: Performance test'
    ]
)