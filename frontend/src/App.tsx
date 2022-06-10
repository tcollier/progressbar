import React from 'react';
import CocktailList from './CocktailList'
import { useCocktailMenuFetcher } from "./hooks";
import {Button, Spinner, useColorMode} from "@chakra-ui/react";
import { MoonIcon } from "@chakra-ui/icons";

function App() {
  const { cocktails, loading } = useCocktailMenuFetcher()
  const { toggleColorMode } = useColorMode()

  return (
      <div className="App">
        <header>
          <Button onClick={toggleColorMode}>
            <MoonIcon />
          </Button>
        </header>
        { loading &&  <Spinner /> }
        {cocktails && <CocktailList cocktails={cocktails} />}
      </div>
  );
}

export default App;
