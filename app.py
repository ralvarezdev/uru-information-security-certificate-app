
import streamlit as st
from cryptography import x509
from cryptography.hazmat.backends import default_backend
import grpc
from ralvarezdev import certificate_pb2
from ralvarezdev import certificate_pb2_grpc

# Set the grpc microservice addressya
GRPC_SERVER_ADDRESS = "localhost:50051"  

channel = grpc.insecure_channel(GRPC_SERVER_ADDRESS)
stub = certificate_pb2_grpc.CertificateStub(channel)


st.title("Digital Certificate Issuer")
st.markdown("""
Welcome! Use the form below to request a digital certificate from the microservice. Fill in all fields and paste a valid public key in PEM format. After issuing, you can download your certificate directly.
""")


with st.form("issue_cert_form"):
    st.subheader("Certificate Request Form")
    common_name = st.text_input("Common Name")
    organization = st.text_input("Organization")
    organizational_unit = st.text_input("Organizational Unit")
    locality = st.text_input("Locality")
    state = st.text_input("State")
    country = st.text_input("Country")
    public_key_pem = st.text_area("Public Key (PEM format)")
    submit = st.form_submit_button("Issue Certificate")

if submit:
    if not all([common_name, organization, organizational_unit, locality, state, country, public_key_pem]):
        st.error("All fields are required.")
    else:
        try:
            public_key_bytes = public_key_pem.encode()
            request = certificate_pb2.IssueCertificateRequest(
                common_name=common_name,
                organization=organization,
                organizational_unit=organizational_unit,
                locality=locality,
                state=state,
                country=country,
                public_key=public_key_bytes
            )
            response_stream = stub.IssueCertificate(request)
            cert_data = None
            for response in response_stream:
                cert_data = response.certificate_content
            if cert_data:
                cert = x509.load_pem_x509_certificate(cert_data, default_backend())
                st.success("Certificate issued successfully!")
                st.markdown("**Certificate Details:**")
                st.write(f"- Subject (Owner): {cert.subject.rfc4514_string()}")
                st.write(f"- Issuer (CA): {cert.issuer.rfc4514_string()}")
                st.write(f"- Valid from: {cert.not_valid_before}")
                st.write(f"- Valid until: {cert.not_valid_after}")
                st.write(f"- Serial number: {cert.serial_number}")
                st.download_button(
                    label="Download Certificate",
                    data=cert_data,
                    file_name="certificado_emitido.pem",
                    mime="application/x-pem-file"
                )
            else:
                st.error("No certificate data received.")
        except Exception as e:
            st.error(f"Error issuing certificate: {e}")
