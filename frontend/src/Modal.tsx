import {
    Modal,
    ModalOverlay,
    ModalContent,
    ModalHeader,
    ModalFooter,
    ModalBody,
    ModalCloseButton, Button, useDisclosure,
} from '@chakra-ui/react'
import React from 'react'

function ModalComponent({invoiceUrl} : { invoiceUrl: string}) {
    const { isOpen, onClose } = useDisclosure()
    // @ts-ignore
    return (
        <Modal isOpen={isOpen} onClose={onClose}>
        <ModalOverlay />
        <ModalContent h='650px' w='1000px'>
          <ModalCloseButton />
          <ModalHeader>Invoice</ModalHeader>
          <ModalBody
              h='500px' w='1000px'
          >
            <iframe height="500px" width="400px" src={invoiceUrl}></iframe>
          </ModalBody>
        </ModalContent>
      </Modal>
    )
}

export default ModalComponent