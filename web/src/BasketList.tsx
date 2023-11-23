import './BasketList.css'

interface Item {
  "name": string;
  "weights": number[];
  "prices": number[];
  "quantity": number,
  "total_price": number,
  "total_weight": number,
  "image": string
}

export default function BasketList(props: { products: Item[] }) {
  return (
    props.products.length === 0 ? <>
    <h1>
      Poxa, não há produtos na cesta no momento!
    </h1>
    <div className='divEmpty'>
      <img className='InstructionsImg' src='./src/assets/show_basket.png'/>
      <div>
        <p>
          1 - Mostre o produto para a câmera
        </p>
        <p>
          2 - Aguarde o produto ser identificado
        </p>
        <p>
          3 - Coloque-o dentro da cesta
        </p>
      </div>
    </div>

    </>
      : (<div className="BasketDiv">
      
      <div className="Header">
        <h1>Produtos na cesta</h1>
      </div>

      {props.products.map((item:Item) => {
        return <div className="item-row" key={item.name}>
          <img className="image-box" src={item.image} />
          <div className="about">
            <h1>{item.name.charAt(0).toUpperCase() + item.name.slice(1)}</h1>
            <p className='description'>Quantidade: {item.quantity}</p>
            <p>Peso total: {item.total_weight.toFixed(0)}g</p>
          </div>
          <div className="amount">
            <h3 className='price'>
              R$ {item.total_price.toFixed(2)}
            </h3>
          </div>
        </div>  
      })}

      <hr />

      <div className="total">
        <div>
          <h2>Sub-Total</h2>
          <p className='description'>{props.products.reduce((a, b) => a + b.quantity, 0).toFixed(0)} itens</p>
        </div>
        <h1 className='totalAmount'>R$ {props.products.reduce((a, b) => a + b.total_price, 0).toFixed(2)}</h1>
      </div>

    </div>)
  )
}

