use std::iter::Peekable;
use std::str::Chars;

pub struct Lexer<'a> {
    source: Peekable<Chars<'a>>,
}

impl<'a> Lexer<'a> {
    pub fn new(sourcestring: &'a String) -> Lexer<'a> {
        Lexer {
            source: sourcestring.chars().peekable(),
        }
    }

    pub fn start(&mut self) {
        match self.source.next() {
            Some(x) if x.is_alphabetic() => println!("alpha"),
            Some(x) if x.is_numeric() => println!("digit"),
            _ => println!("unknown"),
        }
    }
}
