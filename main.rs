fn main() {
    let s: String = String::from("aaaabbbbcccc");
    let t: String = String::from("aabb");
    let length: i32 = lcs_length(s.clone(), t.clone());
    println!("The length of the longest common subsequence between\n s: {} \n and t: {}\n is: {}:", s, t, length);
}

fn lcs_length(text1: String, text2: String) -> i32{
    let len1: usize = text1.len();
        let len2: usize = text2.len();
        let (text1, text2, len2) = if len1 > len2{
            (text1, text2, len2)
        }    
        else{
            (text2, text1, len1)
        };
        let mut memo: Vec<i32> = vec![0; len2 + 1];
        for i in text1.chars(){
            let mut pr = 0;
            let mut prc;
            for (j, d) in text2.chars().enumerate(){
                prc = pr;
                pr = memo[j + 1];
                memo[j + 1] = if i == d {
                    1 + prc
                }else{
                    pr.max(memo[j])
                };
            }
        }
        *memo.last().unwrap_or(&0)
}
