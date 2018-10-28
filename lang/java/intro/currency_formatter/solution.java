import java.text.DecimalFormat;
import java.text.NumberFormat;
import java.util.Locale;
import java.util.Scanner;

/**
 * Java Currency Formatter
 *
 * @author Dela Anthonio
 * @hackerrank https://hackerrank.com/delaanthonio
 * @problem https://www.hackerrank.com/challenges/java-currency-formatter
 */
public class solution {
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		double payment = scan.nextDouble();

		NumberFormat format = new DecimalFormat();
		Locale indiaLocale = new Locale("en", "IN");
		NumberFormat us = NumberFormat.getCurrencyInstance(Locale.US);
		NumberFormat india = NumberFormat.getCurrencyInstance(indiaLocale);
		NumberFormat china = NumberFormat.getCurrencyInstance(Locale.CHINA);
		NumberFormat france = NumberFormat.getCurrencyInstance(Locale.FRANCE);

		System.out.println("US: " + us.format(payment));
		System.out.println("India: " + india.format(payment));
		System.out.println("China: " + china.format(payment));
		System.out.println("France: " + france.format(payment));
		scan.close();
	}
}
