use std::fs;

// use crate::lexer;

use race::lexer::*;

fn main() {
    // read file
    let file_path = String::from("test/main.race");
    let contents = fs::read_to_string(file_path).expect("Could not read file!");
    println!("With text:\n{contents}");
    //
    let lex = Lexer::new(contents);
    lex.start();
    lex.getsource();
}
