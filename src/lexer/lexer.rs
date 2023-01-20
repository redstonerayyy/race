use std::iter::Peekable;
use std::str::Chars;

pub struct Lexer<'a> {
    source: Peekable<Chars<'a>>,
}

impl<'a> Lexer<'a> {
    pub fn new(sourcestring: &String) -> Lexer<'a> {
        Lexer {
            source: sourcestring.chars().peekable(),
        }
    }
}
