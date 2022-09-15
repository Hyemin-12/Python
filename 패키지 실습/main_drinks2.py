# as 키워드로 모듈 이름 변경하여 import
from foods.drinks import milk as m

m.drink()

# # 원래 이름으로는 import 불가
# milk.drink()