import React from 'react';
import CocktailList from './CocktailList'
import { useCocktailMenuFetcher } from "./hooks";
import {Container, Spinner, VStack} from "@chakra-ui/react";
import ModalComponent from './Modal';

function App() {
  const { cocktails, loading } = useCocktailMenuFetcher()

  return (
      <Container maxW='container.xl' justifyContent='center'>
        {loading &&  <VStack>
          <Spinner />
        </VStack>}
        {cocktails && <CocktailList cocktails={cocktails} />}
        <ModalComponent invoiceUrl={"https://btcpay0.voltageapp.io/invoice?id=U1Nv2cKAjorF1A6Bn4T9sK"}/>
      </Container>
  );
}

export default App;
