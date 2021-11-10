# Ebay-Scraping-


The ```ebay-dl.py``` file extracts the name, price, number of items sold, shipping cost, product status, and return status for any product one searches for on Ebay, through the first 10 pages.

## How to Run the Code 
The exact command for accessing each file through Python are listed below, and need to be run in the Python terminal. The code is set such that it will return results for the first ten pages, however adding ```--num_pages=``` to the end of the code, and inputting a number will return that many search pages. For the Tottenham+Hotspur json file, the ```search_term``` must be written as tottenham+hotspur, to reflect that it is a two word search. 

Download ```car.json```:

```
$python3 ebay-dl.py car 
```

Download ```racket.json```:

```
$python3 ebay-dl.py racket
```

To download ```tottenham+hotspur.json```:

```
$python3 ebay-dl.py tottenham+hotspur 
```

[Project Instructions](https://github.com/mikeizbicki/cmc-csci040/tree/2021fall/hw_03)
