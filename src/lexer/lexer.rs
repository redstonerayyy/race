pub struct Lexer {
    source: String,
}

impl Lexer {
    pub fn new(s: String) -> Self {
        Lexer { source: s }
    }

    pub fn start(&self) -> bool {
        true
    }

    pub fn getsource(&self) -> String {
        self.source.clone()
    }
}
