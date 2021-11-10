# Ebay-Scraping-


The ```ebay-dl.py``` file extracts the name, price, number of items sold, shipping cost, product status, and return status for any product one searches for on Ebay. Depending on what the reader wants, they can choose to see information for how ever many search pages they desire
## How to Run the Code 
The exact command for accessing each file through Python are listed below, and need to be run in the Python terminal. The code is set such that amending the ```--num_pages=``` input will allow you to get results for however many pages you want. For the Tottenham+Hotspur json file, the ```search_term``` input must be written as tottenham+hotspur, to reflect that it is a two word search. If you want to dowload the file as a CSV file, simply add ```--csv a``` to the end of the line. Leaving this out will generate the file as a json file

Download ```car.json```:

```
$python3 ebay-dl.py car --num_pages=10 
```
Download ```car.csv```:

```
$python3 ebay-dl.py car --num_pages=10 --csv a 
```
Download ```racket.json```:

```
$python3 ebay-dl.py racket --num_pages=10

```
Download ```racket.csv```:

```
$python3 ebay-dl.py racket --num_pages=10 --csv a 
```

Download ```tottenham+hotspur.json```:

```
$python3 ebay-dl.py tottenham+hotspur --num_pages=10
```
Download ```tottenham+hotspur.csv```:

```
$python3 ebay-dl.py tottenham+hotspur --num_pages=10 --csv a
```

[Project Instructions](https://github.com/mikeizbicki/cmc-csci040/tree/2021fall/hw_03)
