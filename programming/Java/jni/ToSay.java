// import Hello;
import java.util.*;

public class ToSay
{
    public static void main(String argv[])
    {
        ToSay say = new ToSay();
    }
    public ToSay()
    {
        Hello h = new Hello();
        // 调用本地方法向 John 问好
        h.SayHello("John");
    }
}

