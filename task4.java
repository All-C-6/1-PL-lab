public class task4 {

    public static void main(String[] args) {
        double ex = 0;
        double[] t = new double[10];
        for (int i = 0; i < 10;) {
            t[i] = (Math.random() * ((100 - -100) + 1)) + -100;
            i++;
        }
        for (int out = 9; out >= 1; out--){
            for (int in = 0; in < out; in++){
                if(Math.abs(t[in]%1) > Math.abs(t[in + 1]%1)) {
                    ex = t[in];
                    t[in] = t[in+1];
                    t[in+1] = ex;
                }
            }
        }
        for (int i = 0; i < 10; i++) {
            System.out.println(t[i]);
        }
    }
}
