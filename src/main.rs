// lex files and get tokens
mod lexer;
use crate::lexer::lexer::*;

// read files
use std::fs;

fn main() {
    // read file as vec<u8>
    let contents = fs::read_to_string("test/main.race").expect("couldn't read file");
    // create lexer
    let mut lexer = Lexer::new(&contents);
    Lexer::start(&mut lexer);
}
