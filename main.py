import os
from curl_cffi import requests
from pydantic import BaseModel, ValidationError
from rich import print

class Specifications(BaseModel):
  a: str # Label
  b: str # Value

class Product(BaseModel):
  productName: str
  finalPrice: str
  url: str
  inventoryStatus: int # Availability Code
  classification: list[Specifications];

class SearchResponse(BaseModel):
  products: list[Product]
  
def new_session():
  session = requests.Session(impersonate='chrome', proxy=os.getenv('stickyproxy'))
  return session

def search_api(session: requests.Session, query: str, size: int):
  url = f'https://openapi.lenovo.com/us/outletus/en/ofp/search/global/cache/products/get/_tsc?fq=&text={query}&rows={size}&sort=relevance&mtRedesign=true&display_tab=Products'
  response = session.get(url)
  response.raise_for_status()
  
  try:
    search = SearchResponse(**response.json()["data"]["data"][0])
  except ValidationError as exc:
    print(repr(exc.errors()[0]['type']))
    raise
  
  return search

def main():
  session = new_session()
  search = search_api(session, 'LEN101T0080', 60)

  for product in search.products:
    product.url = f"https://www.lenovo.com/us/outletus/en{product.url}"
    
    if product.inventoryStatus != 2:
      print(product)
    
if __name__ == '__main__':
  main()