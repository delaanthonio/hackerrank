{-# LANGUAGE FlexibleInstances, UndecidableInstances, DuplicateRecordFields #-}

module Main where

import Control.Monad
import Data.Array
import Data.Bits
import Data.List
import Data.Set
import Debug.Trace
import System.Environment
import System.IO
import System.IO.Unsafe

helloWorld :: Integer -> IO ()
helloWorld 0 = putStrLn ""
helloWorld cnt = do
  putStrLn "Hello World"
  helloWorld (cnt - 1)

main :: IO()
main = do
    n <- readLn :: IO Integer
    helloWorld n
