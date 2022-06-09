import { useEffect, useState } from "react";
import { Cocktail } from "./types";
import axios from "axios";

function toCocktails(response: any): Cocktail[] {
  const cocktails: Cocktail[] = []
  response.data.forEach(function(object: any) {
    if (object.type === 'ITEM') {
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

function useCocktailMenuFetcher() {
  const [loading, setLoading] = useState<boolean>(true)
  const [error, setError] = useState<any>()
  const [cocktails, setCocktails] = useState<Cocktail[]>()

  useEffect(()=> {
    axios.get('/cocktails').then(response => {
      console.log(response)
      setCocktails(toCocktails(response))
    }).catch(error => {
      console.log(error)
      setError(error)
    }).finally(() =>
      setLoading(false)
    )
  }, [])
  return { cocktails, loading, error }
}

export { useCocktailMenuFetcher }
