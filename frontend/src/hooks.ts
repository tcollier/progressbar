import { useEffect, useState } from "react";
import { Cocktail } from "./types";
import axios from "axios";

function useCocktailMenuFetcher() {
  const [loading, setLoading] = useState<boolean>(true)
  const [error, setError] = useState<any>()
  const [cocktails, setCocktails] = useState<Cocktail[]>()

  useEffect(()=> {
    axios.get('/cocktails').then(response => {
      console.log(response)
      setCocktails(response.data.menuItems as Cocktail[])
    }).catch(error => {
      console.warn(error)
      setError(error)
    }).finally(() =>
      setLoading(false)
    )
  }, [])
  return { cocktails, loading, error }
}

export { useCocktailMenuFetcher }
