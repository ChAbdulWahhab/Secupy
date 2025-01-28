import unittest
from secupy.communication import SecureCommunicator

class TestSecureCommunicator(unittest.TestCase):
    def test_communication(self):
        secret_key = "secret"
        communicator = SecureCommunicator(secret_key)
        message = "test_message"
        signature = communicator.generate_signature(message)
        self.assertTrue(communicator.verify_signature(message, signature))
