use pyo3::prelude::*;

mod set01;

#[pymodule]
fn cryptopals_rust(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(set01::challenge01::challenge01, m)?)?;
    m.add_function(wrap_pyfunction!(set01::challenge01::challenge01_golf, m)?)?;
    Ok(())
}
