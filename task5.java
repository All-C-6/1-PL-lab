import java.io.File;
import java.io.IOException;
import java.util.Scanner;

public class task5 {
    public static void main(String[] args) throws IOException {
        File file = new File("lorem.txt");
        Scanner lorem = new Scanner(file);
        String str1 = "";
        while(lorem.hasNext()) {
                str1 += lorem.next();
        }
        int a = 0;
        int[] freq = new int[26];
        char[] arr1 = str1.toLowerCase().toCharArray();
        for (int i = 0; i <= arr1.length-1; i++) {
            if (arr1[i] != '.' && arr1[i] != ',')
                freq[(int)arr1[i]-97]++;
        }
        for (int i = 0; i < 26; i++ ) {
            System.out.printf("Встречаемость буквы %c составляет %d включений%n", (char)i + 97, freq[i]);
        }

    }
}
