import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        
        Scanner sc=new Scanner(System.in);
        String A=sc.next();
        if(A.equals(new StringBuilder(A).reverse().toString())){
        System.out.println("Yes");
        }
        else{
            System.out.println("No");
        }
        /* Enter your code here. Print output to STDOUT. */
        
    }
}
