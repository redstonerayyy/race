// lex files and get tokens
mod lexer;
use crate::lexer::lexer::*;

// read files
use std::fs;

fn main() {
    // read file
    let file_path = String::from("test/main.race");
    let contents = fs::read_to_string(file_path).expect("Could not read file!");

    // lex file
    let lex = Lexer::new(contents);
    lex.start();
}
