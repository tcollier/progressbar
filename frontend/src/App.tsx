import React from 'react';
import CocktailList from './CocktailList'
import { useCocktailMenuFetcher } from "./hooks";
import {Spinner, useColorMode} from "@chakra-ui/react";

function App() {
  const { cocktails, loading } = useCocktailMenuFetcher()
  const { toggleColorMode } = useColorMode()

  return (
      <div className="App">
        { loading &&  <Spinner /> }
        {cocktails && <CocktailList cocktails={cocktails} />}
      </div>
  );
}

export default App;
