
helloWorld :: IO()
helloWorld =
  do putStrLn "Hello World"

main :: IO()
main = do
  helloWorld
