# 0x01. Caching

## Description

This project explores the implementation of various caching algorithms using Python. Caching is a key concept in computing that helps improve the efficiency and speed of data retrieval by temporarily storing frequently accessed data. The goal of this project is to build multiple cache classes that extend a common base class and implement different cache replacement policies such as FIFO, LIFO, LRU, and more.

Each caching strategy is built on top of a shared base class (`BaseCaching`) which provides a common interface and cache structure. The project is designed to simulate real-world cache behavior in systems where memory is limited and efficient data access is critical.

## Technologies Used

- Ubuntu 18.04 LTS
- Python 3.7
- Pycodestyle 2.5 (PEP8 compliance)

## Project Requirements

- All Python files must be interpreted/compiled with `python3` (version 3.7).
- Files should end with a new line.
- The first line of all files must be: `#!/usr/bin/env python3`.
- Code must follow `pycodestyle` style (version 2.5).
- All files must be executable.
- Modules, classes, and functions must contain full documentation.
- The length of all files will be tested using `wc`.

## Base Class: `BaseCaching`

All cache classes inherit from `BaseCaching`, which provides the cache structure and method templates:

```python
#!/usr/bin/python3
""" BaseCaching module
"""

class BaseCaching():
    """ BaseCaching defines:
      - constants of your caching system
      - where your data are stored (in a dictionary)
    """
    MAX_ITEMS = 4

    def __init__(self):
        """ Initialize
        """
        self.cache_data = {}

    def print_cache(self):
        """ Print the cache
        """
        print("Current cache:")
        for key in sorted(self.cache_data.keys()):
            print("{}: {}".format(key, self.cache_data.get(key)))

    def put(self, key, item):
        """ Add an item in the cache
        """
        raise NotImplementedError("put must be implemented in your cache class")

    def get(self, key):
        """ Get an item by key
        """
        raise NotImplementedError("get must be implemented in your cache class")

