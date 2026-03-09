import java.util.Date;


public class Demo02 {
    public static void main(String[] args) {
        // System.out.println("Hello, World!");
        int[] arr=new int[64 *1024 *1024];
        //#1
        Date t0 = new Date();
        for(int i=0;i<arr.length;i++) arr[i]++;
        Date t1 = new Date();
        System.out.println(t1.getTime() - t0.getTime() + " ms");
        //#2
        t0 = new Date();
        for(int i=0;i<arr.length;i+=16) arr[i]++;
        t1 = new Date();
        System.out.println(t1.getTime() - t0.getTime() + " ms");

        int MAX = 20000;//1000;
        final long[][] data= new long[MAX][MAX];
        // #1
        t0 = new Date();
        long suml = 0;
        for(int r = 0; r<MAX; r++)
            for (int c=0;c<MAX;c++) {
                suml += data[r][c];
            }
        t1 = new Date();
        System.out.println(t1.getTime() - t0.getTime() + " ms");
        // #2
        t0 = new Date();
        long sum2 = 0;
        for(int r =0;r< MAX;r++)
            for (int c =0;c< MAX;c++){
                sum2 += data[c][r];
            }
        t1 = new Date();
        System.out.println(t1.getTime() - t0.getTime() + " ms");
    }
}