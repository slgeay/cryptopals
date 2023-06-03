use pyo3::prelude::*;


#[pyfunction]
pub fn challenge02(s: String) -> PyResult<String> {
    let lines = s.split("\n").collect::<Vec<&str>>();
    let string = lines[0];
    let key = lines[1];
    let decoded_string = hex::decode(string).unwrap();
    let decoded_key = hex::decode(key).unwrap();

    let mut result = Vec::new();
    for i in 0..decoded_string.len() {
        result.push(decoded_string[i] ^ decoded_key[i]);
    }

    Ok(hex::encode(result))
}


#[pyfunction]
pub fn challenge02_golf(s: String) -> PyResult<String> {
    let v=s.split("\n").map(hex::decode).map(|x|x.unwrap()).collect::<Vec<Vec<u8>>>();Ok(hex::encode(v[0].iter().zip(v[1].iter()).map(|(a,b)|a^b).collect::<Vec<u8>>()))
}
