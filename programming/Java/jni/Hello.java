public class Hello
{
    static
    {
        // try
        // {
// 此处即为本地方法所在链接库名
            System.loadLibrary("./libhello.so");
        // }
        // catch(UnsatisfiedLinkError e)
        // {
        //     System.err.println( "Cannot load hello library:\n " +
        //                        e.toString() );
        // }
    }
    public Hello()
    {
    }
// 声明的本地方法
    public native void SayHello(String strName);
}
