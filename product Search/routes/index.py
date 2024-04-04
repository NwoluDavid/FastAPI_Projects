from fastapi import  APIRouter ,Query
from controler.read_product import filter_products
from typing import Annotated


router = APIRouter()

@router.get('/product')
async def read_product( product_name: Annotated [str | None,  Query(description = 'Name of the product' , example="backpack")] = None ,
category: Annotated [ str | None , Query(description= "product category" , example="Travel & Accessories")]= None, 
price_range: Annotated [ str | None , Query(description= "The price of the product" , example="20_100")]= None):
   
   """
   
   
   
   we return filer_product else we return error message product not found
   """ 
   product_name =product_name
   category =category
   price_range = price_range
   
   
   message = filter_products(product_name, price_range, category)
   
   return message

