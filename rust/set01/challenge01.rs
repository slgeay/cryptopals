use pyo3::prelude::*;
use hex;
use base64::{Engine as _, engine::general_purpose};

#[pyfunction]
pub fn challenge01(s: String) -> PyResult<String> {
    let bytes = hex::decode(s).unwrap();
    let base64 = general_purpose::STANDARD.encode(bytes);
    Ok(base64)
}

#[pyfunction]
pub fn challenge01_golf(s: String) -> PyResult<String> {
    Ok(general_purpose::STANDARD.encode(hex::decode(s).unwrap()))
}
