import React from 'react';
import {
  Accordion, AccordionItem
} from '@chakra-ui/react'
import { Cocktail } from './types'
import CocktailDetails from "./CocktailDetails";

function CocktailList({ cocktails }: { cocktails: Cocktail[] }) {
  return (
      <Accordion allowToggle>
        {cocktails.map(function(cocktail) {
          return (
              <AccordionItem>
                  <CocktailDetails cocktail={cocktail}/>
              </AccordionItem>
          )
        })}
      </Accordion>
  );
}

export default CocktailList;
