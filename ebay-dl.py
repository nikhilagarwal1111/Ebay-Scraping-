import csv
import json
import argparse
import requests
from bs4 import BeautifulSoup

def parse_itemssold(text):
    '''
    Takes as input a string and returns the number of items sold, as specified in the string

    >>> parse_itemssold('38 sold')
    38
    >>> parse_itemssold('14 watchers')
    0
    >>> parse_itemssold('Almost gone')
    0
    '''

    numbers= ''
    for char in text:
        if char in '1234567890':
            numbers += char
    if 'sold' in text:
        return int(numbers)
    else:
        return None

def parse_price(text):
    
    if 'to' in text:
        text=text.replace(text[:text.index('o')+2],'')
    numbers = ''
    for char in text:
        if char in '1234567890':
            numbers+=char
    if len(numbers)>0:
        return int(numbers)
    else:
        return None

def parse_shipping(text):
    
    numbers = ''
    for char in text:
        if char in '1234567890':
            numbers+=char
    if len(numbers)>0:
        return int(numbers)
    else:
        return 0

#only run code below when python file is run normally where normally means not in the doctests
if __name__=='__main__':
    #get comm[and line arguments
    parser = argparse.ArgumentParser(description='Download information from ebay and covert to JSON.')
    parser.add_argument('search_term')   
    parser.add_argument('--num_pages',default=10)    
    parser.add_argument('--csv', nargs='?')             
    args = parser.parse_args()
    print('args.search_term=', args.search_term)

    # list of all items found in all ebay webpages
    items=[]

    #loop over the ebay webpages
    for page_number in range(1,int(args.num_pages)+1):

        #build the URL
        url='https://www.ebay.com/sch/i.html?_from=R40&_nkw=' 
        url+= args.search_term  
        url+='&_sacat=0&_pgn='
        url+=str(page_number)
        url+='&rt=nc'
        print('url=', url)

        #download the html
        r=requests.get(url)
        status=r.status_code
        print('status=', status)
        html= r.text
        #print('html=', html[:50])

        #process the html
        soup=BeautifulSoup(html, 'html.parser')

        #loop over the items in the page
        tags_items=soup.select('.s-item')
        for tag_item in tags_items:
           
            name = None
            tags_name = tag_item.select('.s-item__title')
            for tag in tags_name:
                name=tag.text
            
            freereturns= False
            tags_freereturns=tag_item.select('.s-item__free-returns')
            for tag in tags_freereturns:
                freereturns=True
            
            items_sold= None
            tags_itemssold=tag_item.select('.s-item__hotness')
            for tag in tags_itemssold:
                items_sold = parse_itemssold(tag.text)
            
            price_sold= None
            tags_pricesold=tag_item.select('.s-item__price')
            for tag in tags_pricesold:
                price_sold = parse_price(tag.text)

            status= None
            tags_status=tag_item.select('.s-item__subtitle')
            for tag in tags_status:
                status=tag.text

            shipping= 0
            tags_shipping=tag_item.select('.s-item__shipping')
            for tag in tags_shipping:
                shipping = parse_shipping(tag.text)
            

                
            item={
                'name': name,
                'free_returns': freereturns,
                'items_sold': items_sold,
                'status=': status,
                'shipping':shipping,
                'price_sold': price_sold
            }
            items.append(item)
        
        
        print('len(tags_items)=',len(items))

    '''

        tags_names=soup.select('.s-item__title')
        for tag in tags_name:
            items.append({
                'name': tag.text
            })
        tags_freereturns=soup.select('.s-item__free-returns')
        for tag in tags_freereturns:
            print('tag=',tag)
        
        print('len(tags_name)=',len(tags_name))
        print('len(tags_freereturn)=',len(tags_freereturns))
        
        '''
    print('len(items)=',len(items))
    for item in items:
        print('item=', item)

    #write the json to a file
    filename=args.search_term+'.json'
    with open(filename,'w',encoding='ascii') as f:
        f.write(json.dumps(items))
    
    if args.csv:
        labels = ['name', 'free_returns', 'items_sold', 'status', 'shipping', 'price_sold']
        print("csv")
        filename = args.search_term+'.csv'
        with open(filename, 'w') as f:
            writer = csv.DictWriter(f, fieldnames=labels)
            writer.writeheader()
            for item in items:
                writer.writerow(item)
    else:
        filename = args.search_term+'.json'
        with open(filename, 'w', encoding= 'ascii') as f:
            f.write(json.dumps(items))

