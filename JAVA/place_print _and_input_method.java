import java.util.Scanner;
//For the ones who don't want to use System.out.print()
//And Scanner class

public class Main
{
    /**Main method
     * @see print
     * @see input
     */
    public static void main(String[] args)
    {
        print("Hello world!");
        String user = input("It's that you want ?")
    }

    /**The print method
     * @param String str
     */
    public static void print(String str)
    {
        System.out.println(str);
    }
    /**The input method
     * @param String str
     * @return a --> the user input
     */
    public static String input(String str)
    {
        print("str");
        Scanner sc = new Scanner(System.in);
        String a = sc.nextLine();
        return a;
    }
    
}
