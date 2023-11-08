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
}

function App() {

  const [basketProducts, setBasketProducts] = useState<Item[]>([])

  const getProducts = async () => {
    const response = await fetch('http://localhost:8000/basket/')
    const basketJson = await response.json()
    const basketJsonString = JSON.stringify(basketJson)
    const basket: Basket = JSON.parse(basketJsonString)

    const basketItems: Item[] = basket.items

    basketItems.sort((a, b) => a.name.localeCompare(b.name))

    setBasketProducts(basketItems)
  }

  useEffect(() => {
    
    getProducts()
    const interval = setInterval(() => getProducts(), 10000)
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
