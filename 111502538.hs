-- Practice A
isPalindrome :: Eq a => [a] -> Bool
-- please complete here
isPalindrome xs = checkPalindrome xs 0 (length xs - 1)
  where
    checkPalindrome lst start end
      | start >= end       = True  -- If indices cross, it's a palindrome
      | lst !! start /= lst !! end = False  -- Mismatch found, not a palindrome
      | otherwise          = checkPalindrome lst (start + 1) (end - 1)  -- Recurse inward


testcasesA :: [[Int]]
testcasesA = [[], [5..15], [1,1,1,0], [7,3,7]]

resultA :: [Bool]
resultA = map isPalindrome testcasesA 



-- Practice B
coolDiv :: [Double] -> Either String Double
-- please complete here
coolDiv (x:y:_) 
  | x == 0    = Left "Division by zero"  -- Check if the first element is zero
  | otherwise = Right (y / x)             -- Perform division if safe
coolDiv _ = Left "Too short"              -- Handle cases with fewer than two elements

testcasesB :: [[Double]]
testcasesB = [[], [5..15], [999], [33,9999], [0..9]]

resultB :: [Either String Double]
resultB = map coolDiv testcasesB



main :: IO ()
main = do
  print resultA -- [True,False,False,True]
  print resultB -- [Left "Too short",Right 1.2,Left "Too short",Right 303.0,Left "Division by zero"]
