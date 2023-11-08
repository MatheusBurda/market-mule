import './BasketList.css'

interface Item {
  "name": string;
  "weights": number[];
}

export default function BasketList(props: { products: Item[] }) {

  return (
    <div className="BasketDiv">
      
      <div className="Header">
        <h1>Produtos na cesta</h1>
      </div>

      <div className="item-row">
        <img className="image-box" src={"src/assets/banana.jpg"} />
        <div className="about">
          <h1>Banana</h1>
          <p className='description'>Quantidade: 1</p>
          <p>Peso total: 250g</p>
        </div>
        <div className="amount">
        <h3 className='price'>
            R$ 3.19
          </h3>
        </div>
      </div>

      <div className="item-row">
        <img className="image-box" src={"src/assets/apple.jpg"} />
        <div className="about">
          <h1>Maçã</h1>
          <p className='description'>Quantidade: 1</p>
          <p>Peso total: 70g</p>
        </div>
        <div className="amount">
          <h3 className='price'>
            R$ 5.99
          </h3>
        </div>
      </div>     

      <hr />

      <div className="total">
        <div>
          <h2>Sub-Total</h2>
          <p className='description'>2 itens</p>
        </div>
        <h1 className='totalAmount'>R$ 6.18</h1>
      </div>


      {/* {props.products.map((item:Item) => {
      return <tr key={item.name}>
        <td>{item.name}</td>
        <td className="description">{item.weights.length}</td>
        <td>{item.weights}</td>
      </tr>
    })} */}

    </div>
  )
}

