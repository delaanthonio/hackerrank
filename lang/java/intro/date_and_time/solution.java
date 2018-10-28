import java.util.*;

/**
 * Java Date and Time
 *
 * @author Dela Anthonio
 * @hackerrank https://hackerrank.com/delinting
 * @problem https://www.hackerrank.com/challenges/java-date-and-time
 */
public class solution {
	private static final String[] DAYS = { "SUNDAY", "MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY",
			"SATURDAY" };

	public static String findDay(int month, int day, int year) {
		Calendar cal = new GregorianCalendar(year, month - 1, day);
		return DAYS[cal.get(Calendar.DAY_OF_WEEK) - 1];
	}

	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		int month = scan.nextInt();
		int day = scan.nextInt();
		int year = scan.nextInt();

		System.out.println(findDay(month, day, year));
		scan.close();
	}
}
