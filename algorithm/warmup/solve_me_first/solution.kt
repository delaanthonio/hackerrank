import java.util.Scanner

// Solve Me First
//
// author: Dela Anthonio
// hackerrank: https://www.hackerrank.com/delaanthonio
// problem: https://www.hackerrank.com/challenges/solve-me-first

fun solveMeFirst(a: Int, b: Int): Int {
    return a + b
}

fun main(args: Array<String>) {
    val sc = Scanner(System.`in`)
    val num1 = sc.nextInt()
    val num2 = sc.nextInt()
    val sum = solveMeFirst(num1, num2)
    println(sum)
}
