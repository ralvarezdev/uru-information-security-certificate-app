# uru-information-security-certificate-app

**Note:** This repository is archived and read-only.

Certificate generation client, in Python and Streamlit.

Part of a set of Information Security college course (URU) projects forming a secure tender (bid) file submission system, all under `ralvarezdev`:

- **`uru-information-security-certificate-grpc`** — certificate authority gRPC service (port 50053)
- **`uru-information-security-encrypter-grpc`** — encrypts and signs bidder files, forwards them to the decrypter (50051)
- **`uru-information-security-decrypter-grpc`** — receives, stores and decrypts files for the tender owner (50052)
- **`uru-information-security-certificate-app`**, **`-bidder-app`**, **`-admin-app`** — Streamlit UIs to request certificates, submit files and manage files (8503, 8502, 8501)

## What it does

Streamlit UI "Digital Certificate Issuer". A form collects Common Name, Organization, Organizational Unit, Locality, State and Country, requests a certificate from the Certificate gRPC service and offers it as a download.

## Project structure

- **`main.py`** — Streamlit app
- **`microservice/grpc/`** — gRPC client; **`ralvarezdev/`** — generated stubs
- **`certificate-grpc`** — git submodule (see `.gitmodules`) with the service's proto definitions
- **`Dockerfile`** — runs Streamlit on port 8503; `compile_proto.bat` and `update_submodules.bat` are Windows helpers

## Configuration and running

Environment variables (via git-ignored `.env`): `CERTIFICATE_GRPC_HOST`, `CERTIFICATE_GRPC_PORT`.

```bash
git submodule update --init
pip install -r requirements.txt    # may be UTF-16 encoded; convert if pip complains
streamlit run main.py --server.port=8503
```

## License

GNU General Public License v3.0 (see `LICENSE`).
