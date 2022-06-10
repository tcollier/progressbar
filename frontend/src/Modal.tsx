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

function ModalComponent({invoiceUrl, clearInvoice} : { invoiceUrl: string, clearInvoice: () => void}) {
    return (
        <Modal isOpen={true} onClose={clearInvoice}>
        <ModalOverlay />
        <ModalContent h='650px' w='1000px'>
          <ModalCloseButton />
          <ModalHeader>Invoice</ModalHeader>
          <ModalBody
              h='500px' w='1000px'
          >
            <iframe height="500px" width="400px" src={invoiceUrl}></iframe>
          </ModalBody>
          <ModalFooter>
            <Button onClick={clearInvoice}>Close</Button>
          </ModalFooter>
        </ModalContent>
      </Modal>
    )
}

export default ModalComponent