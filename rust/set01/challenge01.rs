use pyo3::prelude::*;
use hex;
use base64::{Engine as _, engine::general_purpose};

#[pyfunction]
pub fn challenge01() -> PyResult<String> {
    let string = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d";
    let bytes = hex::decode(string).unwrap();
    let base64 = general_purpose::STANDARD.encode(bytes);
    Ok(base64)
}

#[pyfunction]
pub fn challenge01_golf() -> PyResult<String> {
    Ok(general_purpose::STANDARD.encode(hex::decode("49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d").unwrap()))
}
