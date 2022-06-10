import React from "react"
import {
  Box,
  Flex,
  Button,
  Heading,
  useColorMode,
  useColorModeValue,
  Container
} from "@chakra-ui/react"
import {MoonIcon} from "@chakra-ui/icons";


const Header = () => {
  const { toggleColorMode } = useColorMode()
  const color = useColorModeValue('gray.100', 'gray.800')

  return (
    <Flex
      as="nav"
      wrap="wrap"
      padding={6}
      bg='orange.400'
      color={color}
      marginBottom={16}
    >
      <Container maxW='container.xl'>
        <Flex justify="space-between">
          <Flex align="center" mr={4}>
            <Heading as="h1" size="lg" letterSpacing={"tighter"}>
              Progress ₿ar
            </Heading>
          </Flex>
          <Box mt={{ base: 4, md: 0 }}>
            <Button onClick={toggleColorMode}>
              <MoonIcon />
            </Button>
          </Box>
        </Flex>
      </Container>
    </Flex>
  );
};

export default Header
