class Encoder:
    def __init__(self, secrets: bytes):
        """
        You **may not** change the arguments or returns of this function!

        :param secrets: Contents of the secrets file generated by
            ectf25_design.gen_secrets
        """
        # TODO: Parse the secrets data here. Ensure any pre-processing or key 
        # derivation (e.g., cryptographic keys) required for frame encoding is handled here.

        # Load the json of the secrets file
        secrets = json.loads(secrets)

        # Extract necessary data for encoding frames
        self.some_secrets = secrets["some_secrets"]

    def encode(self, channel: int, frame: bytes, timestamp: int) -> bytes:
        """
        The frame encoder function

        :param channel: 32b unsigned channel number
        :param frame: Frame to encode (max 64 bytes)
        :param timestamp: 64b timestamp for encoding
        :returns: The encoded frame, ready for transmission
        """
        # TODO: Perform encoding of frames using channel, timestamp, 
        # and any relevant data from the secrets. Implement encryption if needed.
        return struct.pack("<IQ", channel, timestamp) + frame
