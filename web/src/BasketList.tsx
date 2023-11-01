import { useState, useEffect } from 'react'


interface Basket {
  "name": string;
  "items": Item[];
}

interface Item {
  "name": string;
  "weights": number[];
}

export default function BasketList() {

  useEffect(() => {
    loadItems()
  });

  const [basketProducts, setBasketProducts] = useState<Item[]>([])

  const getProducts = async () => {
    const response = await fetch('http://localhost:8000/basket')
    const basketJson = await response.json()
    const basket: Basket = JSON.parse(basketJson)

    const basketItems: Item[] = basket.items

    basketItems.sort((a, b) => a.name.localeCompare(b.name))

    setBasketProducts(basketItems)
  }

  const loadItems = async () => {
    getProducts()
    setTimeout(loadItems, 10000);
  }  

  return (
    <div>
      <ul>

      {basketProducts.map((item)=> {
      return <>
        <p>Produto: {item.name}</p>
        <p>Quantidade: {item.weights.length}</p>
        <p>Pesos: {item.weights}</p>
      </>
      })}
      </ul>
    </div>
  )
}