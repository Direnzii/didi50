# didi50

**didi50** is a simple and efficient tool for sending bulk asynchronous requests. It is ideal for testing task scalability, server performance, and other load analysis. (Use at your own risk.)


---

## Features

- **Target Configuration**: Easily set the "target" (destination address).
- **Requests Control**: Set the number of requests to be sent.
- **Proxy Support**: Optionally use proxies for requests.
- **Asynchronous Requests**: Send multiple requests simultaneously for testing and evaluation.

This tool is primarily designed for performance testing, stress testing, and server capacity evaluation, but it can also be used in other scenarios related to network traffic analysis.

---

## Installation

To install **didi50**, clone the repository and install the necessary dependencies.

```bash
git clone https://github.com/direnzii/didi50.git
cd didi50
pipenv install
````
---

## By PyPi

Use by public repo [PyPi](https://pypi.org)

[didi50 - PyPi](https://pypi.org/project/didi50/)

````bash
pip install didi50
````
---

## Usage

Once the project is installed, you can start using didi50 from the command line.
- Configure the target (destination address).
- Set the number of requests to send.
- Choose whether to use proxies (optional).
- Press Enter and watch the tool send multiple requests simultaneously.

Example:
`````bash
python didi50.py -u http://example.com -q 100 -p
python didi50.py --url http://example.com --qtd-request 100 --proxies
`````
---

## Technologies

**didi50** is built using the following technologies:

- [aiohttp](https://docs.aiohttp.org/en/stable/) - Asynchronous HTTP client/server framework.
- [asyncio](https://docs.python.org/3/library/asyncio.html) - Python's library to write concurrent code using the async/await syntax.
- [itertools](https://docs.python.org/3/library/itertools.html) - Functions that create iterators for efficient looping.
- [argparse](https://docs.python.org/3/library/argparse.html) - Library to handle command-line arguments.

---

## License

**didi50** is licensed under the [MIT License](LICENSE.txt).

---

## How to Contribute

We welcome contributions! If you'd like to improve **didi50**, please feel free to fork the repository and submit a pull request. Make sure to follow the project's coding standards and write tests for any new features.
