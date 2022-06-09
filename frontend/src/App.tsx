import React from 'react';
import CocktailList from './CocktailList'
import { useCocktailMenuFetcher } from "./hooks";

function App() {
  const { cocktails, loading, error } = useCocktailMenuFetcher()

  return (
      <div className="App">
        {cocktails && <CocktailList cocktails={cocktails} />}
      </div>
  );
}

export default App;
