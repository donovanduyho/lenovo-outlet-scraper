# Simple Lenovo Outlet Scraper

## Todo
* Add menu to select codes for specific model lines.
    * LEN101T00XX
    * Example: LEN101T0080 = Thinkpad T14s Gen 4 AMD

## Installation
Step 1: Clone Repo
```
$ git clone [url]
$ cd lenovo-outlet-scraper
```

Step 2: Create Python Virtual Environment
```
$ python -m venv env
$ source /env/bin/activate
```

Step 3: Install [Dependencies](#dependencies)

Step 3: Run
```
$ python main.py
```

## Dependencies
### Pip
```
$ sudo apt install python3-pip 
```
### curl_cffi
```
$ pip install curl_cffi --upgrade
```
### Pydantic
```
$ pip install pydantic
```
### Rich
```
$ pip install rich
```