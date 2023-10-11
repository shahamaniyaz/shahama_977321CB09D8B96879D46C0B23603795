def linearSearchProduct(productList,targetProduct):
  indices = []
  for index,product in enumerate(productList):
    if product == targetProduct:
      indices.append(index)
  return indices
products = ["keyboard", "printer", "mouse", "pendrive", "touchpad", "pendrive"]
target = "pendrive"
result = linearSearchProduct(products,target)
print(result)
