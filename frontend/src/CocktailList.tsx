import React from 'react';
import {
  Accordion, AccordionItem, AccordionButton, AccordionPanel, AccordionIcon, Box, Button
} from '@chakra-ui/react'
import { Cocktail } from './types'
import CocktailDetails from "./CocktailDetails";

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
  return (
      <Accordion allowToggle>
        {cocktails.map(function(cocktail) {
          return (
              <AccordionItem>
                  <CocktailDetails cocktail={cocktail}/>
                {/*<CocktailHeader cocktail={cocktail} />*/}
                {/*<CocktailBody cocktail={cocktail} />*/}
                {/*<AccordionPanel pb={4}>*/}
                {/* <Button> Buy </Button>*/}
                {/*</AccordionPanel>*/}
              </AccordionItem>
          )
        })}
      </Accordion>
  );
}

export default CocktailList;
