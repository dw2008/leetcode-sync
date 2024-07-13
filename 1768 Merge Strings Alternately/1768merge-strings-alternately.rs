impl Solution {
    pub fn merge_alternately(word1: String, word2: String) -> String {
        let mut result = String::new();
        let mut char1 = word1.chars();
        let mut char2 = word2.chars();
        loop{
            match(char1.next(), char2.next()){
                (Some(c1), Some(c2)) => { //if char1 and char2 have not run out yet, append alternately
                    result.push(c1);
                    result.push(c2);
                }
                (Some(c1), None) => {
                    result.push(c1);
                    result.push_str(char1.as_str());
                    break;
                }
                (None, Some(c2)) => {
                    result.push(c2);
                    result.push_str(char2.as_str());
                    break;
                }
                (None, None) => break,
            }
        }
        result
    }
}