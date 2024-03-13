use pyo3::prelude::*;

mod set01;

#[pymodule]
fn cryptopals_rust(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(set01::challenge01::challenge01, m)?)?;
    m.add_function(wrap_pyfunction!(set01::challenge01::challenge01_golf, m)?)?;
    m.add_function(wrap_pyfunction!(set01::challenge02::challenge02, m)?)?;
    m.add_function(wrap_pyfunction!(set01::challenge02::challenge02_golf, m)?)?;
    m.add_function(wrap_pyfunction!(set01::challenge03::challenge03, m)?)?;
    m.add_function(wrap_pyfunction!(set01::challenge03::challenge03_golf, m)?)?;
    m.add_function(wrap_pyfunction!(set01::challenge04::challenge04, m)?)?;
    m.add_function(wrap_pyfunction!(set01::challenge04::challenge04_golf, m)?)?;
    m.add_function(wrap_pyfunction!(set01::challenge05::challenge05, m)?)?;
    m.add_function(wrap_pyfunction!(set01::challenge05::challenge05_golf, m)?)?;
    Ok(())
}
