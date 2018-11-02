;;;; Solution for https://www.hackerrank.com/challenges/solve-me-first

(defun split-by-one-space (string)
  "Returns a list of substrings of string
divided by ONE space each.
Note: Two consecutive spaces will be seen as
if there were an empty string between them."
  (loop for i = 0 then (1+ j)
        as j = (position #\Space string :start i)
        collect (subseq string i j)
        while j))

(defvar n (read-line))
(defvar string-numbers (split-by-one-space (read-line)))
(defvar numbers (mapcar #'parse-integer string-numbers))
(defvar sum (apply '+ numbers))

(format t "~a~%" sum)
