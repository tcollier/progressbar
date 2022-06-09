import './App.css';
import React, { useEffect, useState } from 'react';
import axios from 'axios'
import CocktailList from './CocktailList.js'

function toCocktails(response) {
  const cocktails = []
  response.data.objects.forEach(function(object) {
    if (object.type == 'ITEM') {
      const itemData = object.item_data
      cocktails.push(
        {
          id: object.id,
          name: itemData.name,
          image_id: itemData.image_ids[0],
          price: itemData.variations[0].item_variation_data.price_money.amount,
        }
      )
    }
  })
  return cocktails
}
function App() {
  const [cocktails, setCocktails] = useState(null)

  useEffect(()=>{
    axios.get('/cocktails').then(response => {
      setCocktails(toCocktails(response))
    }).catch(error => {
      console.log(error)
    })

  }, [])
  return (
      <div className="App">
        {cocktails && <CocktailList cocktails={cocktails} />}
      </div>
  );
}

export default App;
