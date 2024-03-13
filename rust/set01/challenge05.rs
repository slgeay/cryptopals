use pyo3::prelude::*;


#[pyfunction]
pub fn challenge05(s: String) -> PyResult<String> {
    let key = "ICE";
    let mut result = String::new();
    for (i, c) in s.chars().enumerate() {
        let key_char = key.chars().nth(i % key.len()).unwrap();
        let xor = c as u8 ^ key_char as u8;
        result.push_str(&format!("{:02x}", xor));
    }
    Ok(result)
}


#[pyfunction]
pub fn challenge05_golf(s: String) -> PyResult<String> {
    Ok(s.chars().enumerate().map(|(i, c)| format!("{:02x}", c as u8 ^ "ICE".chars().nth(i % 3).unwrap() as u8)).collect())
}
