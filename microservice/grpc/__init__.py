import os

from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

# Get gRPC server configuration from environment variables with safe defaults
# If the environment variables are not set, fall back to localhost:50051
CERTIFICATE_GRPC_HOST = os.getenv("CERTIFICATE_GRPC_HOST", "localhost")
try:
	CERTIFICATE_GRPC_PORT = int(os.getenv("CERTIFICATE_GRPC_PORT", "50051"))
except (TypeError, ValueError):
	CERTIFICATE_GRPC_PORT = 50051
