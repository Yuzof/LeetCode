import pandas as pd

def find_products(products: pd.DataFrame) -> pd.DataFrame:
    return pd.DataFrame(products[(products['low_fats'] == 'Y') & (products['recyclable'] == 'Y')]['product_id'])    

prods = pd.DataFrame([{'product_id': 0, 'low_fats': 'Y', 'recycable':'N'}, 
         {'product_id': 1, 'low_fats': 'Y', 'recycable':'Y'}, 
         {'product_id': 2, 'low_fats': 'N', 'recycable':'Y'}, 
         {'product_id': 3, 'low_fats': 'Y', 'recycable':'Y'}, 
         {'product_id': 4, 'low_fats': 'N', 'recycable':'N'}, 
])

print(prods)

print(find_products(prods))