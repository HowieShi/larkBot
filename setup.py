#!/usr/bin/env python

# coding=utf-8

from setuptools import setup

setup(

    name="larkBot",

    version="1.0",

    author="Howie Shi",

    author_email="weishi827@hotmail.com",

    description="This is a service of larkBot",

    license="GPLv3",

    keywords="larkBot",

    url="https://github.com/HowieShi/larkBot",

    packages=['lark_group_bot'],  # 需要打包的目录列表

    # 需要安装的依赖

    install_requires=[
    ],

    # 添加这个选项，在windows下Python目录的scripts下生成exe文件

    # 注意：模块与函数之间是冒号:

    entry_points={'console_scripts': [
        'run = larkBot.lark_group_bot:main',
    ]},

    # long_description=read('README.md'),

    classifiers=[  # 程序的所属分类列表

        "Development Status :: 3 - Alpha",

        "Topic :: Utilities",

        "License :: OSI Approved :: GNU General Public License (GPL)",

    ],

    # 此项需要，否则卸载时报windows error

    zip_safe=False

)
