function orderInfo(item, price, quantity) {
  return `You bought ${quantity} ${item}(s) for a total of ${price * quantity} GEL.`;
}

console.log(orderInfo("apple", 2, 5)); 