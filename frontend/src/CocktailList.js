import React from 'react';
import {
  Accordion, AccordionItem, AccordionButton, AccordionPanel, AccordionIcon, Box,
} from '@chakra-ui/react'

function CocktailHeader({ cocktail }) {
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

function CocktailBody({ cocktail }) {
  return (
      <AccordionPanel pb={4}>
        {cocktail.price} sats
      </AccordionPanel>
  );
}
function CocktailList({ cocktails }) {
  return (
      <Accordion allowToggle>
        {cocktails.map(function(cocktail) {
          return (
              <AccordionItem>
                <CocktailHeader cocktail={cocktail} />
                <CocktailBody cocktail={cocktail} />
              </AccordionItem>
          )
        })}
      </Accordion>
  );
}

export default CocktailList;
