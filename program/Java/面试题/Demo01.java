import java.util.Date;


public class Demo01 {
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
    }
}