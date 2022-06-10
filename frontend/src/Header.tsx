import React from "react"
import {Box, Flex, Button, Heading, useColorMode, useColorModeValue} from "@chakra-ui/react"
import {MoonIcon} from "@chakra-ui/icons";


const Header = () => {
  const { toggleColorMode } = useColorMode()
  const color = useColorModeValue('gray.100', 'gray.800')

  return (
    <Flex
      as="nav"
      align="center"
      justify="space-between"
      wrap="wrap"
      padding={6}
      bg='orange.400'
      color={color}
    >
      <Flex align="center" mr={5}>
        <Heading as="h1" size="lg" letterSpacing={"tighter"}>
          Progress ₿ar
        </Heading>
      </Flex>

      <Box
        mt={{ base: 4, md: 0 }}
      >
        <Button onClick={toggleColorMode}>
            <MoonIcon />
          </Button>
      </Box>
    </Flex>
  );
};

export default Header
