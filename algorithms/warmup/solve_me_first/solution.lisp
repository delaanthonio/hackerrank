;;;; Solution for https://www.hackerrank.com/challenges/solve-me-first

(defvar a nil)
(defvar b nil)

;;; "Calculate the sum of two numbers"
(defun solve-me-first (x y)
  (+ x y))

(setq a (read-line))
(setq b (read-line))

(write (solve-me-first (parse-integer a) (parse-integer b)))
