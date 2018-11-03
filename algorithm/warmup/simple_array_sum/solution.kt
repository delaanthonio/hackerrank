import java.util.Scanner

// Simple Array Sum
//
// author: Dela Anthonio
// hackerrank: https://www.hackerrank.com/delaanthonio
// problem: https://www.hackerrank.com/challenges/simple-array-sum

fun simpleArraySum(ar: Array<Int>): Int {
    return ar.reduce { a: Int, b: Int -> a + b }
}

fun main(args: Array<String>) {
    val scan = Scanner(System.`in`)
    val arCount = scan.nextLine().trim().toInt()
    val ar = scan.nextLine().split(" ").map { it.trim().toInt() }.toTypedArray()
    val result = simpleArraySum(ar)
    println(result)
}
