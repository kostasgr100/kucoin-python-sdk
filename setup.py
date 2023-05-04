#!/usr/bin/python
# -*- coding:utf-8 -*-

from setuptools import setup


setup(
    name='my_kucoin',
    version='v1.0.11',
    packages=['my_kucoin', 'my_kucoin/base_request', 'my_kucoin/margin', 'my_kucoin/market', 'my_kucoin/trade', 'my_kucoin/user',
              'my_kucoin/websocket', 'my_kucoin/ws_token'],
    license="MIT",
    author='Arthur',
    author_email="arthur.zhang@kucoin.com",
    url='https://github.com/kostasgr100/kucoin-python-sdk/',
    description="kucoin-api-sdk",
    install_requires=['requests', 'websockets'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
