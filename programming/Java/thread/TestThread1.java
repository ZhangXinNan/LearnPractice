


public class TestThread1 {
    public static void main(String args[]) {
        Runner1 r = new Runner1();
        Thread t = new Thread(r);
        t.start();

        Thread2 t2 = new Thread2();
        t2.start();

        for (int i = 0; i < 100; i++) {
            System.out.println("Main Thread: ------" + i);
        }
    }
}

class Runner1 implements Runnable {
    public void run() {
        for (int i = 0; i < 100; i++) {
            System.out.println("Runner1 : " + i);
        }
    }
}

class Thread2 extends Thread{
    public void run() {
        for (int i = 0; i < 100; i++) {
            System.out.println("Thread2 : " + i);
        }
    }
}