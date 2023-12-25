from fastapi import APIRouter
from Schema import ProductSchema
from Models import Products, session

router = APIRouter()

p1 = Products(
product_name = 'clinic+',
product_desc = 'powerfull shampoo',
product_price = 2,
product_tax = 1,
product_seller_id = 10,
product_category = 'shampoo'
)

@router.get('/')
def getproducts():
    # pro = session.query(Products).all()
    # session.commit()
    pro = Products.query.filter(Products.product_name == 'clinic+').all()
    product_dicts = [product.as_dict() for product in pro]
    # print(pro)
    return {'status':True, 'products':product_dicts}

@router.get('/{product_id}')
def getproduct(product_id):
    return {'product_id':product_id}

@router.post('/')
def add_product(body : ProductSchema):
    # print(body)
    session.add(p1)
    session.commit()
    return {'status':True}