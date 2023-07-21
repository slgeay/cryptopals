use pyo3::prelude::*;

#[pyfunction]
pub fn challenge04(s: String) -> PyResult<String> {
    let mut best_score = 0;
    let mut best_string = "".to_string();
    
    let lines = s.split("\n").collect::<Vec<&str>>();
    for l in lines {
        let decoded_string = hex::decode(l).unwrap();
        for k in 0..255 {
            let mut result = Vec::new();
            for i in 0..decoded_string.len() {
                result.push(decoded_string[i] ^ k);
            }
            // try to convert the result to a string
            let string = match String::from_utf8(result) {
                Ok(v) => v,
                Err(_) => continue,
            };

            let mut score = 0;
            for c in string.chars() {
                if "etaoinshrdlu ".contains(c.to_ascii_lowercase()) {
                    score += 1;
                }
            }
            
            if score > best_score {
                best_score = score;
                best_string = string;
            }
        }
    }

    Ok(best_string)
}


#[pyfunction]
pub fn challenge04_golf(s: String) -> PyResult<String> {
    Ok(String::from(""))
}
