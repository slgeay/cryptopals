use std::env;
use std::fs;
use std::path::PathBuf;

fn main() {
    // get the directory of the build script
    let dir = PathBuf::from(env::var("CARGO_MANIFEST_DIR").unwrap());

    // get the path to the src directory
    let src_dir = dir.join("rust");

    // get all subdirectories in the src directory
    let entries = fs::read_dir(&src_dir).unwrap();
    let subdirs = entries.filter_map(Result::ok)
        .filter(|e| e.path().is_dir())
        .collect::<Vec<_>>();
    
    let mut all_modules = Vec::new();

    // for each subdirectory...
    for subdir in subdirs {
        // get all .rs files in the subdirectory
        let entries = fs::read_dir(&subdir.path()).unwrap();
        let rs_files = entries.filter_map(Result::ok)
            .filter(|e| {
                let path = e.path();
                path.is_file()
                    && path.extension().map_or(false, |s| s == "rs")
                    && path.file_stem().map_or(false, |s| s != "mod")
            })
            .collect::<Vec<_>>();

        // get the names of the .rs files (without the .rs extension)
        let mod_names = rs_files.iter()
            .map(|e| e.file_name())
            .filter_map(|n| n.to_str().map(|s| s.replace(".rs", "")))
            .collect::<Vec<_>>();

        all_modules.push((subdir.file_name().to_str().unwrap().to_string(), mod_names.clone()));

        // write the mod declarations to the mod.rs file
        let mod_rs = subdir.path().join("mod.rs");
        let mut content = String::new();
        for mod_name in mod_names {
            content.push_str(&format!("pub mod {};\n", mod_name));
        }
        fs::write(&mod_rs, content).unwrap();
    }

    // after the loop over subdirs
    let lib_rs = dir.join("rust").join("lib.rs");
    let mut lib_rs_contents = String::from("use pyo3::prelude::*;\n\n");
    
    for (set_name, _mod_names) in &all_modules {
        lib_rs_contents.push_str(&format!("mod {};\n", set_name));
    }
    
    lib_rs_contents.push_str("\n#[pymodule]\nfn cryptopals_rust(_py: Python, m: &PyModule) -> PyResult<()> {\n");
    
    for (set_name, mod_names) in &all_modules {
        for mod_name in mod_names {
            lib_rs_contents.push_str(&format!("    m.add_function(wrap_pyfunction!({}::{}::{}, m)?)?;\n", set_name, mod_name, mod_name));
        }
    }
    
    lib_rs_contents.push_str("    Ok(())\n}\n");
    
    fs::write(&lib_rs, lib_rs_contents).unwrap();
}
