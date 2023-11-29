import { useState, useEffect } from 'react'

import './App.css'
import BasketList from './BasketList'

interface Basket {
  "name": string;
  "items": Item[];
}

interface Item {
  "name": string;
  "weights": number[];
  "prices": number[];
  "quantity": number,
  "total_price": number,
  "total_weight": number,
  "image": string
}
function App() {

  const [basketProducts, setBasketProducts] = useState<Item[]>([])

  const getProducts = async () => {
    const response = await fetch('http://192.168.178.11:8000/basket/')
    const basketJson = await response.json()
    const basketJsonString = JSON.stringify(basketJson)
    const basket: Basket = JSON.parse(basketJsonString)

    const basketItems: Item[] = basket.items

    basketItems.sort((a, b) => a.name.localeCompare(b.name))

    setBasketProducts(basketItems)
  }

  useEffect(() => {
    
    getProducts()
    const interval = setInterval(() => getProducts(), 1000)
    return () => {
      clearInterval(interval);
    }
}, [])


  return (
    <>
        <BasketList products={basketProducts}/>
    </>
  )
}

export default App
