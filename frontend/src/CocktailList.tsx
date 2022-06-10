import React from 'react';
import {
  Accordion, AccordionItem, AccordionButton, AccordionPanel, AccordionIcon, Box, Button
} from '@chakra-ui/react'
import { Cocktail } from './types'
import CocktailDetails from "./CocktailDetails";
import { useState } from "react";
import axios from "axios";

function CocktailHeader({ cocktail }: { cocktail: Cocktail }) {
  return (
      <h2>
        <AccordionButton>
          <Box flex='1' textAlign='left'>
            {cocktail.name}
          </Box>
        </AccordionButton>
      </h2>
  );
}

function CocktailBody({ cocktail }: { cocktail: Cocktail }) {
  return (
      <AccordionPanel pb={4}>
        {cocktail.price} sats
      </AccordionPanel>
  );
}
function CocktailList({ cocktails }: { cocktails: Cocktail[] }) {
  const [loading, setLoading] = useState<boolean>(false)
  const [invoice, setInvoice] = useState<any>()

  function createInvoice() {
    setLoading(true)
    axios.get('/btcPay/createInvoice').then(response => {
      console.log(response)
      setInvoice(response)
    }).catch(error => {
      console.warn(error)
      setLoading(false)
    })
  }
  return (
      <Accordion allowToggle>
        {cocktails.map(function(cocktail) {
          return (
              <AccordionItem>
                  <CocktailDetails cocktail={cocktail}/>
                  <AccordionPanel pb={4}>
                    <Button disabled={loading} onClick={createInvoice}> Buy </Button>
                  </AccordionPanel>
                {/*<CocktailHeader cocktail={cocktail} />*/}
                {/*<CocktailBody cocktail={cocktail} />*/}
              </AccordionItem>
          )
        })}
      </Accordion>
  );
}

export default CocktailList;