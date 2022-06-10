import React, {useState} from 'react';
import {
  Box,
  Container,
  Stack,
  Text,
  Image,
  Flex,
  VStack,
  Button,
  Heading,
  SimpleGrid,
  StackDivider,
  useColorModeValue,
  List,
  ListItem, Spinner,
} from '@chakra-ui/react';
import { MdLocalShipping } from 'react-icons/md';
import { Cocktail } from './types'
import axios from "axios";
import ModalComponent from "./Modal";

function CocktailDetails({ cocktail }: { cocktail: Cocktail }) {
  const [loading, setLoading] = useState<boolean>(false)
  const [_invoice, setInvoice] = useState<string>('')

  function createInvoice(id: string, price: number) {
    setLoading(true)
    axios.get(`/btcPay/createInvoice?itemId=${id}&itemPrice=${price}`).then(response => {
      setInvoice(response.data)
    }).catch(error => {
      console.warn(error)
    }).finally(() =>
      setLoading(false)
    )
  }

  function clearInvoice() {
    setInvoice('');
  }

  return (
    <Container maxW={'7xl'}>
      <SimpleGrid
        columns={{ base: 1, lg: 2 }}
        spacing={{ base: 8, md: 10 }}
        py={{ base: 18, md: 24 }}>
        <Flex>
          <Image
            rounded={'md'}
            alt={'product image'}
            src={ cocktail.imageURL }
            fit={'cover'}
            align={'center'}
            w={'100%'}
            h={{ base: '100%', sm: '400px', lg: '500px' }}
          />
        </Flex>
        <Stack spacing={{ base: 6, md: 10 }}>
          <Box as={'header'}>
            <Heading
              lineHeight={1.1}
              fontWeight={600}
              fontSize={{ base: '2xl', sm: '4xl', lg: '5xl' }}>
              { cocktail.name }
            </Heading>
            <Text
              color={useColorModeValue('gray.900', 'gray.400')}
              fontWeight={300}
              fontSize={'2xl'}>
              { cocktail.price } SATS
            </Text>
          </Box>

          <Stack
            spacing={{ base: 4, sm: 6 }}
            direction={'column'}
            divider={
              <StackDivider
                borderColor={useColorModeValue('gray.200', 'gray.600')}
              />
            }>
            <VStack spacing={{ base: 4, sm: 6 }}>
              <Text
                color={useColorModeValue('gray.500', 'gray.400')}
                fontSize={'2xl'}
                fontWeight={'300'}>
                { cocktail.description }
              </Text>
              <Text fontSize={'lg'}>
              </Text>
            </VStack>
            <Box>
              <Text
                fontSize={{ base: '16px', lg: '18px' }}
                color={useColorModeValue('yellow.500', 'yellow.300')}
                fontWeight={'500'}
                textTransform={'uppercase'}
                mb={'4'}>
                Ingredients
              </Text>

              <SimpleGrid columns={{ base: 1, md: 2 }} spacing={10}>
                <List spacing={2}>
                  <ListItem>Chronograph</ListItem>
                  <ListItem>Master Chronometer Certified</ListItem>{' '}
                  <ListItem>Tachymeter</ListItem>
                </List>
                <List spacing={2}>
                  <ListItem>Anti‑magnetic</ListItem>
                  <ListItem>Chronometer</ListItem>
                  <ListItem>Small seconds</ListItem>
                </List>
              </SimpleGrid>
            </Box>
          </Stack>

          <Button
            rounded={'none'}
            w={'full'}
            mt={8}
            size={'lg'}
            py={'7'}
            bg='orange.400'
            color={useColorModeValue('gray.100', 'gray.800')}
            textTransform='uppercase'
            disabled={loading} onClick={() => createInvoice(cocktail.id, cocktail.price)}
            _hover={{
              transform: 'translateY(2px)',
              boxShadow: 'lg',
            }}>
            {loading ? <Spinner size='sm' /> : 'Buy'}
          </Button>

          <Stack direction="row" alignItems="center" justifyContent={'center'}>
            <MdLocalShipping />
            <Text>Instant delivery</Text>
          </Stack>
        </Stack>
      </SimpleGrid>
      { _invoice.length > 0 ? <ModalComponent invoiceUrl={_invoice} clearInvoice={clearInvoice}/> : null }
    </Container>
  );
}

export default CocktailDetails;
